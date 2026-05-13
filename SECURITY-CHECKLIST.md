# 📋 보안 검토 및 이동 체크리스트

## 🚨 심각도별 문제 정리

### ⛔ Level 1: 심각 (즉시 조치 필요)

#### 1. OneDrive 클라우드 동기화 문제
```
상태: ❌ 위험
위치: C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter

문제:
- 모든 파일이 Microsoft OneDrive에 자동 업로드
- 초안, 팩트체크, 개인 메모까지 클라우드 저장
- git과 OneDrive 충돌 가능성

해결:
✅ C:\Project_Newsletter 로 이동
✅ 로컬 저장소만 사용
✅ git으로 버전 관리
```

### ⚠️ Level 2: 중요 (이동 후 처리)

#### 1. 환경 설정 노출 위험
```
상태: ⚠️ 미설정
파일: .env

문제:
- API 키, 비밀번호 등이 설정되면 git에 커밋될 수 있음

해결:
✅ .env 파일 생성 (git 무시)
✅ .env.example만 git에 커밋
✅ 모든 민감 정보는 .env에만 저장
```

#### 2. 파일 권한 관리 미흡
```
상태: ⚠️ 기본값 사용
문제:
- 모든 파일이 동일한 권한
- 민감 파일이 노출될 수 있음

해결:
✅ 민감 파일: 소유자만 읽기 (600)
✅ 프로젝트 폴더: 그룹 읽기 가능 (755)
```

### ℹ️ Level 3: 정보 (선택사항)

#### 1. 버전 관리 체계
```
상태: ℹ️ git 준비됨

추천:
✅ git init 실행
✅ 초기 커밋: "Initial commit: project setup"
✅ (선택) GitHub에 업로드
```

---

## ✅ 단계별 이동 계획

### Step 1: 폴더 복사 (지금 당장)

```bash
# Windows 파일 탐색기에서:
1. C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter 열기
2. 모든 파일 선택 (Ctrl+A)
3. 복사 (Ctrl+C)
4. C:\ 드라이브 열기
5. 마우스 우클릭 → 새 폴더 → "Project_Newsletter" 생성
6. 폴더 열기
7. 모든 파일 붙여넣기 (Ctrl+V)
```

**또는 PowerShell 사용:**

```powershell
# PowerShell을 관리자로 실행
Copy-Item -Path "C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter\*" `
          -Destination "C:\Project_Newsletter" -Recurse -Force

# 확인
Get-ChildItem C:\Project_Newsletter
```

### Step 2: VSCode에서 새 위치 열기

```
VSCode 실행
→ File → Open Folder
→ C:\Project_Newsletter 선택
→ Select Folder
```

### Step 3: Git 초기화

```bash
# VSCode 터미널 열기 (Ctrl + `)
cd C:\Project_Newsletter

# Git 초기화
git init

# 파일 추가
git add .

# 초기 커밋
git commit -m "Initial commit: Project Newsletter setup"
```

### Step 4: .env 설정

```bash
# PowerShell 또는 Git Bash
cd C:\Project_Newsletter

# .env.example 복사해서 .env 생성
Copy-Item .env.example .env

# .env 편집 (자신의 정보로)
notepad .env
```

### Step 5: 원본 정리 (선택사항)

```bash
# OneDrive 폴더가 더 이상 필요 없으면 삭제
# 하지만 git으로 버전 관리하니 삭제해도 OK
Remove-Item -Recurse -Force "C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter"
```

---

## 📊 현재 상태 vs 개선 후

### 현재 구조
```
C:\Users\ahnse\OneDrive\문서\Claude\Projects\Project_Newsletter
  ├── 자동 클라우드 동기화 ❌
  ├── 느린 접근 속도 ⚠️
  ├── git 충돌 위험 ⚠️
  └── 백업: OneDrive (자동)
```

### 개선 후 구조
```
C:\Project_Newsletter
  ├── 로컬 저장소만 사용 ✅
  ├── 빠른 접근 속도 ✅
  ├── git 완벽 호환 ✅
  ├── 백업: git (수동 또는 자동)
  ├── 환경 설정: .env (보안) ✅
  └── 버전 관리: git ✅
```

---

## 🔒 보안 체크리스트

### 이동 전
- [x] 보안 가이드 문서 작성 (SECURITY-GUIDE.md)
- [x] 개선된 .gitignore 생성
- [x] .env.example 템플릿 생성
- [ ] 현재 폴더 백업 확인

### 이동 중
- [ ] 파일 복사 완료 확인
- [ ] 파일 개수 일치 확인 (원본과 사본)
- [ ] 주요 파일 내용 확인

### 이동 후
- [ ] C:\Project_Newsletter 에서 파일 접근 테스트
- [ ] VSCode 열기 테스트
- [ ] git init 실행
- [ ] .env 파일 생성 및 설정
- [ ] 초기 커밋 완료
- [ ] OneDrive 원본 삭제 (선택)

### 정기 점검
- [ ] 매월 1회: .gitignore 검토
- [ ] 매월 1회: 민감 파일 확인
- [ ] 필요시: 파일 권한 점검

---

## 📝 파일 권한 설정 (Windows)

### 방법 1: 파일 탐색기 사용

```
1. 파일 우클릭 → 속성
2. 보안 탭 → 편집
3. 자신의 계정 선택 → 완전 제어 ✓
4. 다른 사용자는 읽기 권한만 또는 거부
5. 적용 → 확인
```

### 방법 2: PowerShell 사용

```powershell
# 소유자만 읽기/쓰기 (민감 파일)
icacls "C:\Project_Newsletter\.env" /inheritance:r /grant:r "$env:USERNAME:F"

# 모두 읽기 가능 (발행 파일)
icacls "C:\Project_Newsletter\published" /grant:r "Users:R"
```

---

## 🎯 결론

| 구분 | 현재 | 개선 후 |
|------|------|--------|
| **저장 위치** | OneDrive | C:\ |
| **클라우드 동기화** | 자동 (위험) | 없음 (안전) |
| **접근 속도** | 느림 | 빠름 |
| **git 호환성** | 충돌 위험 | 완벽 호환 |
| **보안** | 약함 | 강함 |
| **환경 설정** | 없음 | .env 사용 |
| **버전 관리** | 없음 | git |

### 즉시 조치 사항
1. ✅ C:\Project_Newsletter 로 이동
2. ✅ git init 실행
3. ✅ .env 파일 생성
4. ✅ .gitignore 확인

---

**마지막 검토**: 2026-05-14  
**상태**: ✅ 개선 방안 완성  
**다음 단계**: 폴더 이동 및 git 초기화
