def unique_words(text, ignore_case=False):
    if ignore_case:
        text = text.lower()

    words = set(text.split())
    return words


text = """
    hello Hello hi hi Hi HI
    """

res = unique_words(text, ignore_case=True)
print(res)
