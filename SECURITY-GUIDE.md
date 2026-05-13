# 🔒 보안 가이드 및 설정 검토

## 🚨 발견된 보안 문제점

### 1. **OneDrive 클라우드 동기화 문제** (심각)

**문제 내용:**
```
현재 위치: C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter
↓
자동으로 Microsoft OneDrive 서버에 업로드됨
↓
뉴스레터 초안, 팩트체크, 출처 등 모든 정보가 클라우드 저장
```

**왜 위험한가?**
- ❌ 개인 작업 데이터가 의도치 않게 클라우드에 저장
- ❌ 동기화 지연으로 인한 작업 방해
- ❌ 클라우드 저장소 증가
- ❌ git과 OneDrive 동시 사용 → 파일 권한 충돌 가능

**해결 방법:**
```
✅ C:\Project_Newsletter 에 이동
→ 로컬 저장소만 사용
→ git으로 버전 관리
→ 필요한 파일만 수동 백업
```

---

### 2. **git 사용 시 주의사항**

**현재 설정 검토:**
```
.gitignore에 포함된 항목:
- secrets.json      ✅ 옳음 (API 키 보호)
- credentials.json  ✅ 옳음 (인증 정보 보호)
- .env             ✅ 옳음 (환경변수 보호)
```

**추가 권장사항:**
```
✅ .gitignore에 추가할 항목:
- *.log             (로그 파일)
- node_modules/     (설치 패키지)
- __pycache__/      (Python 캐시)
- .DS_Store         (Mac OS 파일)
```

---

### 3. **파일 권한 관리**

**현재 상태:**
```
프로젝트 폴더: 일반 사용자 접근 가능 ✅
민감 파일: 보호 필요 ⚠️
```

**권장 설정:**
```
C:\Project_Newsletter\
├── .env              → 소유자만 읽기 (개인 설정)
├── secrets.json      → 소유자만 읽기
└── published/        → 모두 읽기 가능 (발행 파일)
```

---

### 4. **데이터 유출 위험**

**뉴스레터에 포함될 정보:**
- ✅ 안전: 공개 뉴스, 출처 URL, 일반 정보
- ⚠️ 주의: 팩트체크 프로세스, 내부 메모
- ❌ 위험: 개인 의견, 민감한 주석

**체크리스트:**
```
[ ] 초안에 개인정보 포함되지 않음
[ ] 팩트체크 기록에 민감 정보 없음
[ ] 발행 전 모든 URL 확인
[ ] 출처 명시 (저작권 준수)
```

---

## 📋 권장 설정

### 1. **폴더 위치 변경**

```bash
# 현재 위치
C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter

# 권장 위치
C:\Project_Newsletter
또는
C:\Users\[username]\Documents\Project_Newsletter  (OneDrive 아님)
```

### 2. **.gitignore 업데이트**

```
# 운영 체제
.DS_Store
Thumbs.db
*.swp
*.swo

# IDE
.vscode/*
!.vscode/settings.json
.idea/

# Python
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/

# 환경 설정
.env
.env.local
secrets.json
credentials.json

# 임시 파일
*.tmp
*.bak
*~
*.log

# 빌드
dist/
build/

# 테스트
test_*
*_test.md
```

### 3. **.env 파일 생성** (git에서 무시됨)

```bash
# .env (저장소에 커밋되지 않음)
# 개인 설정 예시:

# API 키 (필요시)
API_KEY=your_key_here

# 발행 스케줄
PUBLISH_DAY=Tuesday
PUBLISH_TIME=09:00

# 개인 정보
AUTHOR_EMAIL=aseongchan23@gmail.com
```

---

## 🔐 단계별 보안 체크리스트

### Phase 1: 폴더 이동
- [ ] C:\Project_Newsletter 생성
- [ ] OneDrive 폴더에서 파일 복사
- [ ] OneDrive 원본 폴더 삭제 (선택)
- [ ] VSCode에서 새 위치로 열기

### Phase 2: git 설정
- [ ] git init 실행
- [ ] .gitignore 확인
- [ ] 초기 커밋
- [ ] (선택) GitHub 연결

### Phase 3: 환경 설정
- [ ] .env 파일 생성 (권한: 소유자만)
- [ ] secrets.json 템플릿 생성
- [ ] 개인 설정 정보 입력

### Phase 4: 정기 보안 점검
- [ ] 월 1회: .gitignore 검토
- [ ] 월 1회: 민감 파일 확인
- [ ] 필요시: 파일 권한 재설정

---

## 📊 위치별 비교

| 항목 | C:\ | Documents | OneDrive |
|------|-----|-----------|----------|
| **클라우드 동기화** | ❌ | ❌ | ✅ ⚠️ |
| **빠른 접근** | ✅ | ✅ | ⚠️ |
| **git 호환성** | ✅ | ✅ | ⚠️ |
| **백업** | 수동 | 수동 | 자동 |
| **보안** | 우수 ✅ | 우수 ✅ | 주의 ⚠️ |

**추천**: **C:\Project_Newsletter** 또는 **C:\Users\[username]\Documents\Project_Newsletter**

---

## 🚀 다음 단계

1. **폴더 이동** → C:\ 루트에 생성
2. **git 초기화** → `git init`
3. **.env 설정** → 개인 설정 저장
4. **첫 커밋** → `git add . && git commit`
5. **온라인 백업** → GitHub 연결 (선택)

---

**마지막 수정**: 2026-05-14  
**작성자**: 성찬 (Claude Agent)
