# Answer the question 1
with open('wasteland.txt', 'r') as fr:
    fr = fr.read()
    all_words = fr.lower().split()
    non_repetitive_words = set(all_words)
    count_of_all_words = len(fr.split())
    count_of_non_repetitive_words = len(set(fr.split()))

with open('out_words_count.txt', 'w') as fw:
    fw.write("Number of all words: ")
    fw.write(str(count_of_all_words))
    fw.write("\nNumber of non repetitive words: ")
    fw.write(str(count_of_non_repetitive_words))


# Answer the question 2

# Auxiliary function 1
def word_spliter(text: str):
    for i in " ! , . ? ( ) * & ^ % $ # @ _ - + = < > ' : ; ":
        text = text.replace(i, " ")
        all_words = text.lower().split()
    return all_words


# Auxiliary function 2
def extract_text_of_file(filename):
    with open(filename) as fr:
        text = fr.read()
    return text


# If we want to extract the text from the file:
#def word_ferequency(filename):
#    text = extract_text_of_file(filename)
#    out = {}
#    for i in set(word_spliter(text)):
#        out[i] = out.keys()
#        n = all_words.count(i)
#        out[i] = n + 1
#
#    return out






# Main Function
def word_frequency(text: str):
    out = {}
    for i in set(word_spliter(text)):
        out[i] = out.keys()
        number_of_repeat = all_words.count(i)
        out[i] = number_of_repeat + 1

    return out


text = fr
print(word_frequency(text))

