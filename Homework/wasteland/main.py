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


# ---------------------------------------------------------------------------------

# Answer the question 2

# Auxiliary function 1
def word_spliter(text: str):
    for i in """ ! , . ? ( ) * & ^ % $ # @ _ - + = < > ' " : ; """:
        text = text.replace(i, " ")
        all_words = text.lower().split()
    return all_words


# Auxiliary function 2
def extract_text_of_file(filename):
    with open(filename) as fr:
        text = fr.read()
    return text


# If we want to extract the text from the file:
# def word_ferequency(filename):
#    text = extract_text_of_file(filename)
#    out = {}
#    for i in set(word_spliter(text)):
#        out[i] = out.keys()
#        n = all_words.count(i)
#        out[i] = n + 1
#
#    return out


# Main Function
def dic_word_frequency(text: str):
    out = {}
    for i in set(word_spliter(text)):
        out[i] = out.keys()
        number_of_repeat = all_words.count(i)
        out[i] = number_of_repeat + 1

    return out


text = fr
# print(dic_word_frequency(text))


# --------------------------------------------------------------------------------------------

# try for question 3


def list_of_the_maximum_of_values(dic: dict, n: int = 10 ** 10):
    """
    :param dic:
    :param n: numbers of the words with the most frequent in the dictionary
    :return: a list of "n" numbers of the "values" with maximum value
    """
    out = []
    for i in dic.values():
        out.append(i)
        out.sort()
        out = out[::-1]
        out = out[0:n]
    return out


# counter = 1
# for i in out:
#    print(counter,".",[word for word, number in dic.items() if number is i], i)
#    counter+=1
#

#

# def extract_keys_from_values(dic: dict, value_lst):
#    list_of_keys = list(dic.keys())
#    # list_of_specific_values = value_lst
#    m = 0
#    out = []
#    for i in value_lst:
#        out.append(list_of_keys[m])
#        m += 1
#    return out


dic = dic_word_frequency(text)
list1 = list_of_the_maximum_of_values(dic, 10)

# in ye tabe' hast ke dictionary va liste value haye mored nazar ro behesh midim,
# khoruji kelid haye marbout be value haa ast... amma nemidunam koja irad dare?!!!!!!!

def extract_keys_by_values(dic: dict, lst:list):
    i = 0
    out = []
    for k in list(dic.keys()):
        if dic[k] == lst[i]:
            i += 1
            out.append(k)

    return out


#test
f = extract_keys_by_values(dic, list1)
print(f)

dic = dic_word_frequency(text)
a = list_of_the_maximum_of_values(dic, 10)

print(a)

# print("\n", out)

