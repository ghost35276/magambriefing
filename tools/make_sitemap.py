#!/usr/bin/env python3
"""site/js/posts.js 를 읽어 site/sitemap.xml 을 생성한다.

사용: 저장소 루트에서  python3 tools/make_sitemap.py
- Cloudflare Pages 는 /about.html 을 /about 으로 리다이렉트하므로
  사이트맵에는 확장자 없는 주소를 기록한다.
- 새 글을 js/posts.js 에 추가한 뒤 이 스크립트를 실행하고 함께 커밋한다.
"""
import re
import sys
from datetime import date
from pathlib import Path

DOMAIN = "https://magambriefing.com"
ROOT = Path(__file__).resolve().parent.parent / "site"

STATIC = ["", "archive", "about", "membership", "products", "privacy", "disclaimer"]


def read_posts():
    text = (ROOT / "js" / "posts.js").read_text(encoding="utf-8")
    # 주석 줄 제거 후 date/url 쌍 추출
    lines = [l for l in text.splitlines() if not l.strip().startswith("//")]
    body = "\n".join(lines)
    pairs = re.findall(r'date:\s*"(\d{4}-\d{2}-\d{2})"[^}]*?url:\s*"([^"]+)"', body)
    return pairs


def main():
    today = date.today().isoformat()
    urls = []
    for path in STATIC:
        loc = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
        urls.append((loc, today))
    for d, url in read_posts():
        slug = url[:-5] if url.endswith(".html") else url
        urls.append((f"{DOMAIN}/{slug}", d))

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        out.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    out.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"sitemap.xml: {len(urls)} URLs")


if __name__ == "__main__":
    sys.exit(main())
