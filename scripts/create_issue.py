import argparse
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

def load_settings(edition, base_dir):
    settings_path = base_dir / "settings" / f"{edition}.json"
    if not settings_path.exists():
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {settings_path}")
    with open(settings_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_sources(base_dir):
    sources_path = base_dir / "data" / "sources.json"
    if not sources_path.exists():
        return {}
    with open(sources_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_draft(edition, target_date):
    base_dir = Path(__file__).parent.parent
    
    # 1. 설정 및 템플릿 로드
    settings = load_settings(edition, base_dir)
    template_path = base_dir / "templates" / "newsletter-template.md"
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
        
    # 소스 데이터 로드
    sources_data = load_sources(base_dir)
    edition_sources = sources_data.get(edition, {}).get(target_date, [])

    # 2. 날짜 계산
    parsed_date = datetime.strptime(target_date, "%Y-%m-%d")
    next_week = (parsed_date + timedelta(days=7)).strftime("%Y-%m-%d")

    # 3. 플레이스홀더 치환
    content = template_content.replace("{{date}}", target_date)
    content = content.replace("{{title_kr}}", settings.get("title_kr", edition))
    content = content.replace("{{next_publish_date}}", next_week)
    
    # 기사 목록 Markdown 생성
    articles_md = ""
    if not edition_sources:
        # 데이터가 없을 경우 기본 템플릿 블록 생성
        articles_md += f"### 1. [기사 제목 입력]\n\n**뉴스**: [내용 요약 입력]\n\n**왜 중요한가요?**: [이유 설명 입력]\n\n**출처**: [출처명](https://...)\n\n---\n"
    else:
        for idx, article in enumerate(edition_sources, 1):
            articles_md += f"### {idx}. {article.get('title', '')}\n\n"
            articles_md += f"**뉴스**: {article.get('summary', '')}\n\n"
            articles_md += f"**왜 중요한가요?**: [DJ 톤으로 이유 설명 작성]\n\n"
            articles_md += f"**출처**: [{article.get('source_name', '출처')}]({article.get('url', '#')})\n\n"
            if idx < len(edition_sources):
                articles_md += "---\n\n"

    content = content.replace("{{articles_content}}", articles_md.strip())

    # 4. 파일 저장
    draft_dir = base_dir / "drafts"
    draft_dir.mkdir(exist_ok=True)
    
    file_name = f"{target_date}-{edition}-weekly.md"
    output_path = draft_dir / file_name
    
    if output_path.exists():
        print(f"⚠️ 이미 초안이 존재합니다: {output_path}")
        return
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"✅ 성공적으로 초안이 생성되었습니다: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="새 간행지 초안을 생성합니다.")
    parser.add_argument("--edition", required=True, choices=["game", "it", "crypto", "soccer"], help="간행지 종류")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="발행일 (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    try:
        create_draft(args.edition, args.date)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")