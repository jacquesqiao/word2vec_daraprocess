import os
import collections


def get_files(dir):
    files = os.listdir(dir)
    files = filter(lambda path: os.path.isfile(path), files)
    files = [file_name for file_name in files if
             file_name.startswith("englishText") and
             file_name.endswith("_out")]
    return files


def word_count(f, word_dict):
    for l in f:
        for w in l.strip().split():
            if w is not None:
                word_dict[w] += 1
    return word_dict


def dict_to_list(word_dict):
    word_list = [None] * len(word_dict)
    for i, key in enumerate(word_dict):
        word_list[i] = (key, word_dict[key])
    return word_list

word_dict = collections.defaultdict(int)
for file_name in get_files("."):
    with open(file_name, "r") as f:
        word_dict = word_count(f, word_dict)

word_list = dict_to_list(word_dict)
word_list.sort(key=lambda x: x[1], reverse=True)

with open("word_dict", "w") as f:
    for k, v in word_list:
        f.write(str(v) + " " + k + "\n")