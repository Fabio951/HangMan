import numpy as np

# from nltk.corpus import words
# word_list = np.asarray(words.words())


def load_vocabulary(vocabulary):
    with open(f"dictionaries/{vocabulary}", "r") as f:
        vocabulary = np.asarray(f.read().split("\n"))

    f_check_format = np.vectorize(lambda word: word.isascii() and word.isalpha())
    f_upper_words = np.vectorize(lambda word: word.upper())

    vocabulary = np.asarray(list(vocabulary))
    vocabulary = f_upper_words(vocabulary[f_check_format(vocabulary)])
    vocabulary = np.asarray(list(set(vocabulary)))

    return vocabulary


def guess_word(word_guess, vocabulary):

    f_filter_length = np.vectorize(lambda word: len(word) == len(word_guess))
    f_set_words = np.vectorize(lambda word: "".join(set(word)))

    list_filtered = vocabulary[f_filter_length(vocabulary)]

    guessed_letters = []
    last_guess_letter = ""
    last_guess_indexes = []
    fails = 0

    while not all([letter in guessed_letters for letter in word_guess]) and fails<9:

        try:

            all_letters = list("".join(f_set_words(list_filtered)))
            letters_ordered = [letter for letter, _ in sorted(zip(*np.unique(all_letters, return_counts=True)), key=lambda x: -x[1])]

            if all([letter in guessed_letters for letter in letters_ordered]):
                fails = 9
                break

            for letter in letters_ordered:
                if letter in guessed_letters:
                    continue
                else:
                    guessed_letters.append(letter)

                if letter in word_guess:
                    last_guess_letter = letter
                    last_guess_indexes = [index for index, l in enumerate(word_guess) if l==letter]
                    break
                else:
                    fails += 1
                    if fails>=9:
                        break

            filter_letter = np.vectorize(lambda word: all([word[index]==last_guess_letter for index in last_guess_indexes]))
            list_filtered = list_filtered[filter_letter(list_filtered)]

        except:
            fails = 9
            break

    return fails