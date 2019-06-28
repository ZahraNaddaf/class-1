def open_file(fname):
    with open(fname) as fr:
        text = fr.read()
    return text


def edit_text(text: str):
    text = text.lower()
    for c in '!?.;,"\'()-':
        text = text.replace(c, " ")
    return text





text = open_file('wasteland.txt')
edited = edit_text(text)
words = edited.split()
uniq = set(words)
print(len(words))
print(len(uniq))
