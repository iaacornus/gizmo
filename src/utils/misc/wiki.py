from wikipediaapi import Wikipedia, ExtractFormat, WikipediaPage # type: ignore


def fetch_wiki(word: str) -> tuple[str, str] | None:
    """Fetch the wikipedia page of the given word.

    Args:
        word -- the query

    Returns:
        The title of the page and the summary of the page.
    """

    wiki: Wikipedia = Wikipedia(
            "en",
            extract_format=ExtractFormat.WIKI
        )
    page_py: WikipediaPage = wiki.page(word)

    if page_py.exists():
        return page_py.title, page_py.summary
    else:
        return None
