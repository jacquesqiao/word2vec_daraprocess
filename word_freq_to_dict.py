import cPickle
import sys

IN_FILE = sys.argv[1]
OUT_FILE = sys.argv[2]

word_dict = dict()
index = 0
f = open(IN_FILE, "r")
for line in f:
    freq, word = line.strip().split(" ")
    word_dict[word] = index
    index += 1

with open(OUT_FILE, "w") as f:
    cPickle.dump(word_dict, f)
