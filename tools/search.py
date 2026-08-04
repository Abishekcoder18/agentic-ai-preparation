from ddgs import DDGS


def search_web(query):
    """
    Search the web using DDGS.

    Args:
        query (str): Search query

    Returns:
        list: Search results
    """

    try:
        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        return results

    except Exception as e:

        print(f"Search failed: {e}")

        return []