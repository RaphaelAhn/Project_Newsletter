# Project Newsletter

게임, IT, 코인, 축구 주제를 다루는 주간 뉴스레터 프로젝트입니다.

이 저장소는 경로 의존성을 최소화해서, 다른 PC에서도 `C:\Project_Newsletter` 같은 위치에 그대로 내려받아 이어서 작업할 수 있게 구성합니다.

## 다른 PC에서 이어서 작업하기

Windows PowerShell 기준:

```powershell
cd C:\
git clone https://github.com/RaphaelAhn/Project_Newsletter.git
cd C:\Project_Newsletter
```

원하는 위치가 꼭 `C:\Project_Newsletter`일 필요는 없지만, 여러 PC에서 같은 경로를 쓰고 싶다면 위 방식이 가장 단순합니다.

## 현재 폴더 구조

```text
Project_Newsletter/
├── docs/                      # 작업 가이드 문서
├── drafts/                    # 작성 중인 초안
├── published/                 # 발행 완료본
├── scripts/                   # 보조 스크립트 및 데이터
├── templates/                 # 뉴스레터 템플릿
├── crypto.json                # 코인 섹션 설정
├── game.json                  # 게임 섹션 설정
├── it.json                    # IT 섹션 설정
├── soccer.json                # 축구 섹션 설정
├── .env.example               # 환경 변수 예시
├── .gitignore
├── README.md
├── SECURITY-CHECKLIST.md
├── SECURITY-GUIDE.md
└── TONEGUIDE.md
```

## 작업 흐름

1. `scripts/sources.json`에 이번 회차 기사 후보를 정리합니다.
2. 초안을 생성합니다.

```powershell
python scripts/create_issue.py --edition game --date 2026-05-14
```

3. `docs/prompts.md`와 `TONEGUIDE.md`를 참고해 초안을 다듬습니다.
4. 팩트체크 내용을 정리합니다.
5. 발행본으로 이동합니다.

```powershell
python scripts/publish_edition.py --edition game --date 2026-05-14
```

## 경로 관련 원칙

- 스크립트는 프로젝트 루트를 기준으로 상대경로를 사용합니다.
- 다른 PC에서는 저장소만 그대로 클론하면 됩니다.
- 개인 PC 경로, OneDrive 경로, 사용자명 같은 절대경로를 코드에 넣지 않는 것을 권장합니다.

## Git 사용 기본

다른 PC에서 작업한 뒤 변경사항을 다시 올릴 때:

```powershell
git add .
git commit -m "Update newsletter workflow"
git push
```

현재 PC에서 최신 내용을 받을 때:

```powershell
git pull
```
