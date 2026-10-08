# 마감 브리핑 사이트 운영 가이드

정적 HTML 사이트입니다. 서버 프로그램이 없고, 호스팅 비용은 도메인 비용 중심입니다.

## 폴더 구성

| 경로 | 용도 |
|---|---|
| index.html | 메인 |
| archive.html | 전체 글 목록 (일일/주간 필터) |
| briefings/_template-daily.html | 일일 마감 브리핑 템플릿 |
| briefings/_template-weekly.html | 주간 증권가 뉴스 템플릿 |
| js/posts.js | 글 목록 (새 글 작성 시 한 줄 추가) |
| membership.html | 유료 멤버십 안내 (결제 연동 전) |
| products.html | 디지털 상품 및 제휴 링크 |
| about.html / privacy.html / disclaimer.html | 소개, 개인정보처리방침, 면책 고지 |
| ads.txt / robots.txt / sitemap.xml | 애드센스, 검색 로봇, 사이트맵 |
| (저장소 루트) tools/make_sitemap.py | posts.js 기반 사이트맵 생성 |

## 글 작성 절차

1. 템플릿을 `briefings/2026-10-08.html` 형식으로 복사합니다. 주간 글은 `weekly-2026-10-11.html` 형식입니다.
2. `{{ }}` 부분을 확정 수치로 채웁니다. 확정되지 않은 수치는 행을 삭제합니다.
3. 해시태그는 10개 이내로 작성합니다.
4. `js/posts.js` 배열 맨 앞에 해당 글 한 줄을 추가합니다.

## 배포 (Cloudflare Pages + GitHub)

도메인: `magambriefing.com` (Cloudflare Registrar, 2026-10-07 등록)

1. GitHub에 저장소를 만들고 이 압축 파일의 `site/`, `tools/` 폴더를 올립니다.
2. Cloudflare 대시보드의 Workers & Pages에서 Pages 프로젝트를 만들고 GitHub 저장소를 연결합니다.
3. 빌드 명령은 비우고, 빌드 출력 디렉터리는 `site`로 지정합니다.
4. 배포가 끝나면 프로젝트의 Custom domains에서 Set up a domain을 선택해 `magambriefing.com`을 추가합니다. (수동 CNAME을 먼저 만들면 522 오류가 날 수 있으므로 대시보드에서 먼저 연결)
5. Cloudflare Pages는 `/about.html`을 `/about`으로 리다이렉트합니다. 사이트맵은 확장자 없는 주소로 생성됩니다.

## 사이트맵 갱신

새 글을 `js/posts.js`에 추가한 뒤 저장소 루트에서 실행하고, 변경된 `site/sitemap.xml`을 함께 올립니다.

    python3 tools/make_sitemap.py

## 검색 등록 (배포 후)

- Google Search Console에 `magambriefing.com`을 등록하고 `https://magambriefing.com/sitemap.xml`을 제출합니다.
- 소유권 확인 방법은 Search Console 화면의 안내를 따릅니다.

## 애드센스 신청 전 점검

- 구글의 승인 기준과 심사 기간은 구글 애드센스 고객센터의 최신 안내를 따릅니다. 승인 여부와 수익은 보장되지 않습니다.
- 신청 전 확인할 것: 개인정보처리방침·소개·문의처 페이지 존재(포함됨), 직접 작성한 글의 충분한 누적, 사이트 탐색 가능 상태.
- 승인 후: `index.html`과 템플릿의 `<head>`에 애드센스 스크립트를 넣고, `ads.txt`의 게시자 ID를 교체한 뒤 `.ad-slot` 영역에 광고 단위 코드를 넣습니다.
- 데이터 출처(한국거래소 등)의 이용 조건을 확인한 뒤 수치를 게재하세요.

## 유료 콘텐츠·상품 판매 전 확인

- 유료로 투자 정보를 제공하면 유사투자자문업 신고 대상에 해당할 수 있습니다. 금융감독원 등에서 해당 여부를 확인하세요.
- 온라인 판매는 통신판매업 신고가 필요할 수 있습니다. 관할 지자체 또는 정부24에서 확인하세요.
- 제휴 링크는 수수료를 받는다는 사실을 링크 근처에 표기합니다. (products.html에 문구 포함)

## 해야 할 치환 항목

- `{{운영자 이메일 주소}}` (about.html, privacy.html)
- `{{YYYY-MM-DD}}` 시행일 (privacy.html)
- `ca-pub-XXXXXXXXXXXXXXXX` (index.html, ads.txt) — 승인 후

(robots.txt의 Sitemap 주소는 `magambriefing.com`으로 반영되어 있습니다.)
