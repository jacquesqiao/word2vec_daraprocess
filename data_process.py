import multiprocessing
import os
import math

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

stopword_map = dict((k, 1) for k in stopwords.words('english'))


def process_file(in_files):
    for in_file in in_files:
        out_file = in_file + "_out"
        tokenizer = RegexpTokenizer(r'\w+')

        with open(in_file, "r") as in_f:
            in_content = in_f.read()
            tokens = tokenizer.tokenize(in_content)
            words = [w.lower() for w in tokens if 
                     w.isalpha()
                     and w != ""
                     and not w.isdigit()
                     and w.lower() not in stopword_map]
            with open(out_file, "w") as out_f:
                out_f.write(" ".join(words) + "\n")


def get_filenames(dir_name):
    files = [file for file in os.listdir(dir_name) if
             file.startswith("englishText") and
             file.endswith("0000")]
    return files


if __name__ == "__main__":
    num_process = 10
    file_names = get_filenames(".")

    num_file_per_process = int(math.ceil(float(len(file_names))/num_process))
    start_index = 0
    for i in range(num_process):
        files = file_names[start_index:start_index + num_file_per_process]
        start_index += num_file_per_process
        process = multiprocessing.Process(target=process_file, args=(files,))
        process.start()
