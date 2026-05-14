import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path


def resolve_project_root():
    return Path(__file__).resolve().parent.parent


def find_first_existing_path(*candidates):
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def load_settings(edition, base_dir):
    settings_path = find_first_existing_path(
        base_dir / "settings" / f"{edition}.json",
        base_dir / f"{edition}.json",
    )
    if not settings_path.exists():
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {settings_path}")

    with open(settings_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_sources(base_dir):
    sources_path = find_first_existing_path(
        base_dir / "data" / "sources.json",
        base_dir / "scripts" / "sources.json",
        base_dir / "sources.json",
    )
    if not sources_path.exists():
        return {}

    with open(sources_path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_articles_markdown(edition_sources):
    if not edition_sources:
        return (
            "### 1. [기사 제목 입력]\n\n"
            "**뉴스**: [내용 요약 입력]\n\n"
            "**왜 중요한가?**: [이유 설명 입력]\n\n"
            "**출처**: [출처명](https://...)\n\n"
            "---"
        )

    blocks = []
    for index, article in enumerate(edition_sources, start=1):
        block = (
            f"### {index}. {article.get('title', '')}\n\n"
            f"**뉴스**: {article.get('summary', '')}\n\n"
            "**왜 중요한가?**: [DJ 톤으로 이유 설명 작성]\n\n"
            f"**출처**: [{article.get('source_name', '출처')}]({article.get('url', '#')})"
        )
        blocks.append(block)

    return "\n\n---\n\n".join(blocks)


def create_draft(edition, target_date):
    base_dir = resolve_project_root()
    settings = load_settings(edition, base_dir)
    template_path = base_dir / "templates" / "newsletter-template.md"

    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    sources_data = load_sources(base_dir)
    edition_sources = sources_data.get(edition, {}).get(target_date, [])

    parsed_date = datetime.strptime(target_date, "%Y-%m-%d")
    next_week = (parsed_date + timedelta(days=7)).strftime("%Y-%m-%d")

    content = template_content.replace("{{date}}", target_date)
    content = content.replace("{{title_kr}}", settings.get("title_kr", edition))
    content = content.replace("{{next_publish_date}}", next_week)
    content = content.replace(
        "{{articles_content}}",
        create_articles_markdown(edition_sources),
    )

    draft_dir = base_dir / "drafts"
    draft_dir.mkdir(exist_ok=True)

    output_path = draft_dir / f"{target_date}-{edition}-weekly.md"
    if output_path.exists():
        print(f"이미 초안이 존재합니다: {output_path}")
        return

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"초안을 생성했습니다: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="주간 뉴스레터 초안을 생성합니다.")
    parser.add_argument(
        "--edition",
        required=True,
        choices=["game", "it", "crypto", "soccer"],
        help="간행지 종류",
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="발행일 (YYYY-MM-DD)",
    )

    args = parser.parse_args()

    try:
        create_draft(args.edition, args.date)
    except Exception as error:
        print(f"오류 발생: {error}")
