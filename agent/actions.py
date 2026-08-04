from tools.search import search_web
from tools.reader import fetch_webpage


def act(question):
    print("🛠️ Searching for information...")

    results = search_web(question)

    print(f"✅ Found {len(results)} search results")

    if not results:
        return ""

    print("\nTop Search Results:")

    for index, result in enumerate(results[:3], start=1):
        print(f"{index}. {result['title']}")

    top_url = results[0]["href"]

    print("\n📖 Reading the top result...")

    page_content = fetch_webpage(top_url)

    print(f"✅ Retrieved {len(page_content)} characters")

    return page_content