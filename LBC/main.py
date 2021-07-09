import os
import re

def compute_term_frequency(sentence):
    """
    Compute the frequency of each word in the sentence and return
    each occurence probability
    :param sentence: a sentence - a string
    :return: a list wich contains term frequency
    """
    sentence_ = re.sub("[^\w]", " ", sentence).split()
    n = len(sentence_)
    word_count = {}
    for word in sentence_:
        if word in word_count:
            word_count[word] += 1/n
        else:
            word_count[word] = 1/n
    return [(word, count) for word, count in word_count.items()]


def get_file_path(filename):
    """

    :param filename: name of the file to find
    :return: absolute path to file
    """
    return [
        os.path.join(root, filename)
        for root, dir, files in os.walk(os.getcwd())
        if filename in files
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(compute_term_frequency('deep learning, is the new black  deep   orange'))
    print(get_file_path("fake_file.txt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
