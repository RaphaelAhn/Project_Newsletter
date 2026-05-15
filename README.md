# Project Newsletter

게임, IT, 크립토, 축구 주제를 다루는 주간 뉴스레터 프로젝트입니다.

이 저장소는 여러 PC에서 같은 구조로 이어서 작업하기 쉽게, 비교적 단순한
루트 중심 구조로 정리되어 있습니다.

## Quick Start

```powershell
cd C:\
git clone https://github.com/RaphaelAhn/Project_Newsletter.git
cd C:\Project_Newsletter
```

`.env.example`을 참고해 로컬용 `.env`를 준비합니다.

## Current Structure

```text
Project_Newsletter/
├─ .env
├─ .env.example
├─ .gitignore
├─ README.md
├─ SECURITY-CHECKLIST.md
├─ SECURITY-GUIDE.md
├─ TONEGUIDE.md
├─ settings.json
├─ game.json
├─ it.json
├─ crypto.json
├─ soccer.json
├─ .vscode/
│  └─ settings.json
├─ docs/
│  ├─ PROJECT-STRUCTURE.md
│  ├─ edition-strategy.md
│  ├─ fact-check-guide.md
│  └─ prompts.md
├─ drafts/
│  └─ SAMPLE-2026-05-14.md
├─ scripts/
│  ├─ create_issue.py
│  ├─ publish_edition.py
│  └─ sources.json
└─ templates/
   └─ newsletter-template.md
```

구조 설명은 [docs/PROJECT-STRUCTURE.md](C:/Project_Newsletter/docs/PROJECT-STRUCTURE.md:1)에서
조금 더 자세히 볼 수 있습니다.

## Workflow

1. `scripts/sources.json`에 발행일 기준 기사 소스를 정리합니다.
2. 초안을 생성합니다.

```powershell
python scripts/create_issue.py --edition game --date 2026-05-14
```

3. `docs/prompts.md`, `TONEGUIDE.md`, `docs/fact-check-guide.md`를 참고해 문안을 다듬고 검증합니다.
4. 발행 완료 후 초안을 발행 폴더로 이동합니다.

```powershell
python scripts/publish_edition.py --edition game --date 2026-05-14
```

`published/` 폴더는 처음 발행할 때 자동으로 생성됩니다.

## Editions

- `game.json`
- `it.json`
- `crypto.json`
- `soccer.json`

각 파일은 에디션 이름, 표시용 제목, 기본 기사 수, 발행 요일, 톤 가이드를 담는
기본 설정 파일입니다.

## Environment

- `.env`는 로컬 전용 파일입니다.
- `.env.example`은 공유 가능한 템플릿입니다.
- API 키, 토큰, 개인 비밀값은 `.env`에만 두는 것을 권장합니다.

## Notes

- `.vscode/settings.json`은 선택 사항입니다.
- `drafts/SAMPLE-2026-05-14.md`는 예시 초안으로 유지 중입니다.
- 빈 상태였고 현재 워크플로에 연결되지 않던 `scripts/factcheck.json`은 정리했습니다.

## Git

```powershell
git add .
git commit -m "Update newsletter workflow"
git push
```

최신 변경 사항을 받으려면:

```powershell
git pull
```
