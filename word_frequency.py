import os

word_frequency = dict()

files = os.listdir(".")
files = [file for file in files if
         file.startswith("englishText") and
         file.endswith("_out")]

for file in files:
    with open(file, "r") as f:
        content = f.read().replace("\n", " ")
        words = content.split(" ")
        for word in words:
            if word_frequency.has_key(word):
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

with open("word_dict", "w") as f:
    for k in word_frequency:
        f.write(str(word_frequency[k]) + " " + k + "\n")


