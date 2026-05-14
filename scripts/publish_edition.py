import argparse
import os
from datetime import datetime
from pathlib import Path

def publish_draft(edition, target_date):
    base_dir = Path(__file__).parent.parent
    draft_dir = base_dir / "drafts"
    published_dir = base_dir / "published"
    
    file_name = f"{target_date}-{edition}-weekly.md"
    draft_path = draft_dir / file_name
    published_path = published_dir / file_name
    
    # 1. 파일 존재 여부 확인
    if not draft_path.exists():
        print(f"❌ 초안 파일을 찾을 수 없습니다: {draft_path}")
        return

    published_dir.mkdir(exist_ok=True)
    
    # 2. 파일 내용 읽기
    with open(draft_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 3. 상태 텍스트 변경
    old_status = "상태: 📝 작성 중"
    new_status = "상태: ✅ 발행됨"
    
    if old_status in content:
        content = content.replace(old_status, new_status)
    
    # 4. 발행 폴더에 저장
    with open(published_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 5. 기존 초안 삭제 (이동 완료)
    draft_path.unlink()
    
    print(f"🎉 성공적으로 발행되었습니다!\n이동 완료: {published_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="작성 완료된 초안을 발행 폴더로 이동시킵니다.")
    parser.add_argument("--edition", required=True, choices=["game", "it", "crypto", "soccer"], help="간행지 종류")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="발행일 (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    try:
        publish_draft(args.edition, args.date)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")