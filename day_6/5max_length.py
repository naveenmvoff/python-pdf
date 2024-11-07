#  Given a list of words, find the word with the maximum length and its length.
def lenth(input1):

    store = []
    max_len = 0

    for i in input1:
        a = len(i)
        if a > max_len:
            store = [i]
            max_len = a
    out = "".join(store)
    return out, max_len




input1 = input("Enter: ").split()
word,leng = lenth(input1)
print(f"the longest word is '{word}' and the length of the word is '{leng}'")
