# 📻 Project Newsletter - 주간 뉴스레터

게임, IT, 코인, 축구에 관한 정확하고 친근한 주간 뉴스레터를 발행하는 프로젝트입니다.

## 🎯 프로젝트 목표

- **정확성**: 팩트 체크된 뉴스만 전달
- **친근함**: 라디오 DJ처럼 편한 톤으로 설명
- **실용성**: 누구나 이해할 수 있는 쉬운 설명
- **정기성**: 매주 일관되게 발행

## 📋 프로젝트 구조

```
Project_Newsletter/
├── docs/                    # 문서 및 가이드
│   └── fact-check-guide.md  # 팩트 체크 방법론
├── data/                    # 구조화된 데이터 보관
│   ├── sources.json         # 뉴스 출처 및 기사 링크 데이터
│   └── factcheck.json       # 팩트체크 기록 및 상태 관리
├── settings/                # 간행지별 설정 파일
│   ├── game.json            # 게임 섹션 설정
│   ├── it.json              # IT 섹션 설정
│   ├── crypto.json          # 코인 섹션 설정
│   └── soccer.json          # 축구 섹션 설정
├── drafts/                  # 뉴스레터 초안
├── published/               # 발행된 뉴스레터
├── templates/               # 뉴스레터 템플릿
├── scripts/                 # 자동화 스크립트
└── README.md               # 이 파일
```

## 🎙️ 톤 가이드

- **라디오 DJ처럼** 자연스럽고 친근한 느낌
- **실용적이면서 친절** 불필요한 건 빼되, 따뜻함 유지
- **쉽게 설명** 초등학생도 이해할 수 있도록
- **정확하게** 팩트는 검증 필수

자세한 가이드는 `TONEGUIDE.md`를 참고하세요.

## 📅 발행 주기

- **발행일**: 매주 (요일 미정)
- **섹션**: 게임, IT, 코인, 축구 4개 분야
- **형식**: Markdown (.md 파일)

## 🔄 작업 흐름

1. **뉴스 수집 및 템플릿 생성** → `data/sources.json`에 뉴스 기록 후 `create_issue.py`로 초안 파일 생성
2. **1차 작성 (Codex)** → `docs/prompts.md`의 템플릿을 사용하여 Codex로 기초 원고 작성
3. **1차 검수 및 수정 (Claude Code)** → `docs/prompts.md`의 윤문 템플릿으로 DJ 톤 앤 매너 반영
4. **정확도 체크 (Perplexity)** → `docs/prompts.md`의 팩트체크 템플릿을 활용해 실시간 교차 검증
5. **피드백 루프** → 4번(Perplexity) 검증 결과 내용이 부정확하다면, 피드백을 바탕으로 3번(Claude Code)으로 돌아가 재작성
6. **발행** → 최종 검수 완료 후 `publish_edition.py` 스크립트로 `published/` 폴더로 이동

## 📝 시작하기

1. `data/sources.json` 파일에 이번 주 다룰 뉴스 정보 저장
2. 터미널을 열고 스크립트 실행하여 초안 생성:
   ```bash
   python scripts/create_issue.py --edition game --date 2026-05-14
   ```
3. `docs/prompts.md`를 참고하여 Codex, Claude, Perplexity를 활용해 `초안 작성 → 윤문 → 팩트체크 및 수정` 루프 진행
4. 검증된 내용을 `data/factcheck.json`에 기록
5. 글 완성 후 발행 스크립트 실행:
   ```bash
   python scripts/publish_edition.py --edition game --date 2026-05-14
   ```

---

**관리자**: 성찬 (aseongchan23@gmail.com)
