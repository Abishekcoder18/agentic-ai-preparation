from tools.search import search_web
from tools.reader import fetch_webpage


def act(question):
    print("🛠️ Searching for information...")

    results = search_web(question)

    if not results:
        print("⚠️ Search failed. Will retry in the next iteration.")
        return ""

    print(f"✅ Found {len(results)} search results")

    print("\nTop Search Results:")

    for index, result in enumerate(results[:3], start=1):
        print(f"{index}. {result['title']}")

    top_url = results[0]["href"]

    print("\n📖 Reading the top result...")

    page_content = fetch_webpage(top_url)

    if not page_content:
        print("⚠️ Failed to read webpage. Will retry in the next iteration.")
        return ""

    print(f"✅ Retrieved {len(page_content)} characters")

    return page_content