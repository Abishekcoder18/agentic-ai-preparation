from tools.search import search_web
from tools.reader import fetch_webpage


def act(question):
    print("🛠️ Searching for information...")

    results = search_web(question)

    if not results:
        print("⚠️ Search failed. Will retry in the next iteration.")
        return None, ""

    print(f"✅ Found {len(results)} search results")

    print("\nTop Search Results:")

    for index, result in enumerate(results[:5], start=1):
        print(f"{index}. {result['title']}")

    print("\n📖 Trying search results...")

    for index, result in enumerate(results[:5], start=1):
        url = result.get("href", "")

        if not url:
            continue

        print(f"\n🔗 Trying result {index}: {result['title']}")

        page_content = fetch_webpage(url)

        if page_content:
            print(f"✅ Retrieved {len(page_content)} characters")
            print(f"🔗 Source: {url}")

            return page_content, url

        print("⚠️ Could not read this result. Trying the next result...")

    print("❌ Could not retrieve any webpage from the search results.")
    return None, ""