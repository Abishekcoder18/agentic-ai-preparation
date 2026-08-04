from tools.search import search_web
from tools.reader import fetch_webpage

results = search_web("What is Agentic AI?")

if results:

    url = results[0]["href"]

    print("Reading:")

    print(url)

    content = fetch_webpage(url)

    print("\nFirst 500 characters:\n")

    print(content[:500])

else:

    print("No search results found.")