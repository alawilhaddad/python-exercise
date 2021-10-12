# https://www.hackerrank.com/test/ch1k00qp1cn/questions/dk2bt0fq4fg

import string


def transformSentence(sentence):
    alphabet = list(string.ascii_lowercase)
    words = sentence.split(' ')
    for j, word_utd in enumerate(words):
        word = list(word_utd)
        for i, char in enumerate(word):
            if i == 0: pass
            else:
                if alphabet.index(word[i].lower())+1 > alphabet.index(word[i-1].lower())+1:
                    word[i] = word[i].upper()
                elif alphabet.index(word[i].lower())+1 < alphabet.index(word[i-1].lower())+1:
                    word[i] = word[i].lower()
                elif alphabet.index(word[i].lower())+1 == alphabet.index(word[i-1].lower())+1:
                    pass
        words[j] = "".join(word)
    return " ".join(words)


if __name__ == '__main__':
    sentence = input()

    print(transformSentence(sentence))
