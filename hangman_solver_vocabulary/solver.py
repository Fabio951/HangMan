import numpy as np
from tqdm import tqdm
from random_word import RandomWords

from utils import load_vocabulary, guess_word


vocabulary = load_vocabulary("american-english-insane")

n_words = 300
r = RandomWords()

cumulative_fails = 0
for _ in tqdm(range(n_words)):

    while True:
        word = r.get_random_word()
        if word is None: continue
        if word.isalpha() and word.isascii():
            break
    word = word.upper()

    fails = guess_word(word, vocabulary)
    print(word, " >>> ", fails)
    cumulative_fails += fails

print("\n\n\n")
print("Average_fails: ", np.round(cumulative_fails / n_words, 2))
