from ddgs import DDGS


def search_web(query):
    """
    Search the web using DDGS and return clean webpage results.
    """

    try:
        with DDGS() as ddgs:
            results = list(
                ddgs.text(
                    query,
                    max_results=10
                )
            )

        clean_results = []

        for result in results:
            url = result.get("href", "")

            if not url:
                continue

            # Skip obvious advertising/redirect URLs
            if "aclick?" in url:
                continue

            if "adurl" in url.lower():
                continue

            clean_results.append(result)

            if len(clean_results) == 5:
                break

        return clean_results

    except Exception as e:
        print(f"Search failed: {e}")
        return []