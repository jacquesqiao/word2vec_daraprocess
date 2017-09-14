import cPickle
import sys
import os

DICT_FILE = sys.argv[1]
IN_IDR = sys.argv[2]

with open(DICT_FILE, "r") as f:
    word_dict = cPickle.load(f)


def get_files(dir_name):
    files = [file for file in os.listdir(dir_name) if
             file.startswith("englishText") and
             file.endswith("_out")]
    return files


def mapping_words(file_name):
    with open(file_name, 'r') as fin:
        for line in fin:
            # line = line.decode('utf-8')
            yield [word_dict[w] for w in line.strip().split() if w in word_dict]

for file_name_in in get_files(IN_IDR):
    file_name_out = file_name_in + ".pkl"
    cPickle.dump(list(mapping_words(file_name_in)), open(file_name_out, 'wb'), -1)
