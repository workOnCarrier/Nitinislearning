from playwright.sync_api import sync_playwright
import csv
import time

NEETCODE_URL = "https://neetcode.io/practice/practice/neetcode150"
OUTPUT_CSV = "neetcode150.csv"


def extract_problems(page):
    # Let the page fully load JS content
    page.wait_for_timeout(5000)

    # Try to grab any React/JS data structure that looks like a list of problems
    problems = page.evaluate(
        """
        () => {
            const results = [];

            // Helper to normalise a problem object
            const normalise = (p) => {
                if (!p || typeof p !== 'object') return null;

                const title =
                    p.title ||
                    p.name ||
                    p.problemTitle ||
                    p.questionTitle ||
                    '';

                const slug =
                    p.slug ||
                    p.leetcodeSlug ||
                    p.titleSlug ||
                    p.problemSlug ||
                    '';

                if (!title && !slug) return null;

                const leetcode_url = slug
                    ? `https://leetcode.com/problems/${slug}/`
                    : '';

                return { title, slug, leetcode_url };
            };

            // Scan window for arrays of objects that look like problems
            for (const key of Object.keys(window)) {
                let value;
                try {
                    value = window[key];
                } catch (e) {
                    continue;
                }

                if (!value) continue;

                if (Array.isArray(value)) {
                    for (const item of value) {
                        const norm = normalise(item);
                        if (norm) results.push(norm);
                    }
                } else if (typeof value === 'object') {
                    // Look inside nested arrays on objects
                    for (const subKey of Object.keys(value)) {
                        const subVal = value[subKey];
                        if (Array.isArray(subVal)) {
                            for (const item of subVal) {
                                const norm = normalise(item);
                                if (norm) results.push(norm);
                            }
                        }
                    }
                }
            }

            // Deduplicate by leetcode_url + title
            const seen = new Set();
            const unique = [];
            for (const r of results) {
                const key = (r.leetcode_url || '') + '|' + (r.title || '');
                if (seen.has(key)) continue;
                seen.add(key);
                unique.push(r);
            }

            return unique;
        }
        """
    )

    return problems


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(NEETCODE_URL, wait_until="networkidle")
        time.sleep(3)  # extra safety wait

        problems = extract_problems(page)

        browser.close()

    if not problems:
        print("No problems found. The page structure may have changed.")
        return

    # Write to CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "slug", "leetcode_url"])
        for p in problems:
            writer.writerow([
                p.get("title", ""),
                p.get("slug", ""),
                p.get("leetcode_url", ""),
            ])

    print(f"Wrote {len(problems)} problems to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
