def unique_words(text):
    """
    list of unique words in the text
    :param text: string
    :return:
    """
    words = set(text.split())
    return words


text = """
    A laser beam used for welding
    Red (660 & 635 nm), green (532 & 520 nm) and blue-violet (445 & 405 nm) lasers
    A laser is a device that emits light through a process of optical amplification 
    based on the stimulated emission of electromagnetic radiation. The term "laser" 
    originated as an acronym for "light amplification by stimulated emission of 
    radiation".[1][2] The first laser was built in 1960 by Theodore H. Maiman at 
    Hughes Research Laboratories, based on theoretical work by Charles Hard Townes 
    and Arthur Leonard Schawlow.
    """

res = unique_words(text)
print(res)
