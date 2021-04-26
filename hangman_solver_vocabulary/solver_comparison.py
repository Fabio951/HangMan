from tqdm import tqdm
from random_word import RandomWords

from utils import load_vocabulary, guess_word


vocabularies = {
    "small": load_vocabulary("american-english-small"),
    "normal": load_vocabulary("american-english"),
    "large": load_vocabulary("american-english-large"),
    "insane": load_vocabulary("american-english-insane"),
    "english_normal": load_vocabulary("english_words.txt"),
    "english_large": load_vocabulary("english_words_complete.txt"),
}

for key1, voc1 in vocabularies.items():
    for key2, voc2 in vocabularies.items():
        if key2==key1: continue
        diff1 = set(voc1).difference(set(voc2))
        diff2 = set(voc2).difference(set(voc1))
        sum_ = set(voc1).union(set(voc2))

        print()
        print(key1, " >>> ", len(voc1))
        print(key2, " >>> ", len(voc2))
        print(key1 + " - " + key2, " >>> ", len(diff1))
        print(key2 + " - " + key1, " >>> ", len(diff2))
        print(key1 + " + " + key2, " >>> ", len(sum_))

a = b

for key, vocab in vocabularies.items():
    print(key, " >>> ", len(vocab))

cumulative_fails = {
    key: 0 for key in vocabularies
}

n_words = 300
r = RandomWords()
for _ in tqdm(range(n_words)):

    while True:
        word = r.get_random_word()
        if word is None: continue
        if word.isalpha() and word.isascii():
            break
    word = word.upper()
    print()
    print(word)
    print()

    for key, vocabulary in vocabularies.items():
        fails = guess_word(word, vocabulary)
        print("\t" + key, " >>> ", fails)
        cumulative_fails[key] += fails

print("\n\n\n")
for key, cum_fails in cumulative_fails.items():
    print(key, " >>> ", cum_fails/n_words)
