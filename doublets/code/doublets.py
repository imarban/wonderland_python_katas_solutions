from copy import deepcopy


class DoubletSolver(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.tracked = []

    def get_doublet(self, word1, word2):
        return Solver(deepcopy(self.dictionary)).find_ladders(word1, word2)


class Solver(object):
    def __init__(self, wordlist):
        self.tracked = []
        self.wordlist = wordlist

    @staticmethod
    def differ_by_one(word1, word2):
        differ = 0

        if max(len(word1), len(word2)) - min(len(word1), len(word2)) > 1:
            return False

        for i in xrange(len(word1)):
            if word1[i] != word2[i]:
                differ += 1
                if differ > 1:
                    return False
        return True

    def find_mutations(self, word):
        possible_mutations = []

        for dictword in self.wordlist:
            if self.differ_by_one(word, dictword):
                possible_mutations.append(dictword)

        return possible_mutations

    def remove_words(self, words):
        for word in words:
            self.wordlist.remove(word)

    def find_ladders(self, begin_word, end_word):

        paths = [WordTracked(begin_word)]
        i = 0

        while i < len(paths):
            path = paths[i]

            if path.is_word(end_word):
                return len(path.tracked), path.tracked

            possible_mutations = self.find_mutations(path.word)

            for possible in possible_mutations:
                new_path = deepcopy(path)
                new_path.add(possible)
                paths.append(new_path)
            else:
                if self.differ_by_one(path.word, end_word):
                    path.tracked.append(end_word)
                    return path.tracked

            self.remove_words(possible_mutations)

            i += 1

        return []


class WordTracked(object):
    def __init__(self, word):
        self.word = word
        self.tracked = [word]

    def add(self, word):
        self.word = word
        self.tracked.append(word)

    def is_word(self, word):
        return self.word == word

    def __repr__(self):
        return ', '.join(self.tracked)
