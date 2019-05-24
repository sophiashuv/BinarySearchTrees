import time
import random
from linkedbst import LinkedBST


def read_file(filename):
    """
    Reads words from dictionary and returns a list of them
    """
    with open(filename) as f:
        lines = f.readlines()
    return lines


def random_words(dict_lst):
    """
    Randoms 1000 words form list of all words
    """
    words = []
    while len(words) <= 1000:
        word = random.choice(dict_lst)
        words.append(word)
    return words


def search_list(lst, words):
    """
    Search words in lst
    """
    for i in words:
        lst.index(i)


def search_tree(tree, words):
    """
    Search words by  binary tree
    """
    for i in words:
        tree.find(i)


def search_bst(tree, words):
    """
    Search цщкви by balanced binary tree
    """
    if not tree.isBalanced():
        tree.rebalance()
    for i in words:
        tree.find(i)


def main():
    lst = read_file("words.txt")
    words = random_words(lst)
    tree = LinkedBST(words)
    s1 = time.time()
    search_list(lst, words)
    e1 = time.time()
    s2 = time.time()
    search_tree(tree, words)
    e2 = time.time()
    s3 = time.time()
    search_bst(tree, words)
    e3 = time.time()
    print('Search list:', e1 - s1)
    print('Search tree:', e2 - s2)
    print('Search balanced tree:', e3 - s3)


main()
