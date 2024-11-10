# Create a function that takes a list of sentences and writes them to a new text file, each on a new line.

def write_sentences(sen_list, newfile):
    with open(newfile, 'w') as file:
        for i in sen_list:
            file.write(i + '\n')


sen_list = [
    "This is the first sentence.",
    "This is the second sentence.",
    "Python is great for file operations."
]

write_sentences(sen_list, 'sample.txt')

print("The out is writen.")