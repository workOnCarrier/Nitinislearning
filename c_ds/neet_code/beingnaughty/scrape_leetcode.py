from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

LOCAL_HTML = "/Users/nitinsharma/tmp/neetcode150.html"   # change to your path
OUTPUT_CSV = "neetcode150_from_local.html.csv"

def main():
    # Read the local HTML file
    with open(LOCAL_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Collect all anchor tags
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        text = a.get_text(strip=True)

        links.append({
            "text": text,
            "href": href,
        })

    # Filter for LeetCode problem links
    leetcode_links = [
        l for l in links
        if "leetcode.com/problems/" in l["href"]
    ]

    # Save to CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "href"])
        for l in leetcode_links:
            writer.writerow([l["text"], l["href"]])

    print(f"Found {len(leetcode_links)} LeetCode links")

if __name__ == "__main__":
    main()
