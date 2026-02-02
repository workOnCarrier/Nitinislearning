from playwright.sync_api import sync_playwright
import json

NEETCODE_URL = "https://neetcode.io/practice/practice/neetcode150"

def extract_leetcode_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(NEETCODE_URL, wait_until="networkidle")

        # This JS depends on NeetCode's front-end structure and may need tweaking
        # It searches React props / global variables for problem data
        data = page.evaluate(
            """
            () => {
                // Try common places where NeetCode stores problem data
                // 1) Check if there's a global variable with problems
                const candidates = [];

                for (const k of Object.keys(window)) {
                    try {
                        const v = window[k];
                        if (v && typeof v === 'object') {
                            // Heuristic: look for arrays of objects with title/slug/leetcode* fields
                            const maybeArr = Array.isArray(v) ? v : null;
                            if (maybeArr && maybeArr.length && typeof maybeArr[0] === 'object') {
                                const keys = Object.keys(maybeArr[0]);
                                if (keys.some(x => x.toLowerCase().includes('title')) &&
                                    keys.some(x => x.toLowerCase().includes('slug') || x.toLowerCase().includes('leetcode'))) {
                                    candidates.push(maybeArr);
                                }
                            }
                        }
                    } catch (e) {}
                }

                // 2) Also scan data attributes / script tags if needed
                // (kept simple here; add more heuristics if nothing is found)

                // Flatten candidates and normalise
                const out = [];
                for (const arr of candidates) {
                    for (const prob of arr) {
                        if (!prob) continue;
                        const title = prob.title || prob.name || '';
                        const slug =
                            prob.slug ||
                            prob.leetcodeSlug ||
                            prob.titleSlug ||
                            '';
                        if (!slug && !title) continue;
                        out.push({
                            title,
                            slug,
                            leetcode_url: slug
                                ? `https://leetcode.com/problems/${slug}/`
                                : null,
                        });
                    }
                }

                // Deduplicate by URL
                const seen = new Set();
                const unique = [];
                for (const p of out) {
                    const key = p.leetcode_url || p.title;
                    if (!key || seen.has(key)) continue;
                    seen.add(key);
                    unique.push(p);
                }
                return unique;
            }
            """
        )

        browser.close()
        return data

if __name__ == "__main__":
    problems = extract_leetcode_links()
    with open("neetcode150_leetcode_links.json", "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)

    # Also write a simple text file with just URLs
    with open("neetcode150_leetcode_links.txt", "w", encoding="utf-8") as f:
        for p in problems:
            if p.get("leetcode_url"):
                f.write(p["leetcode_url"] + "\n")
