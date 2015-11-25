import unittest
from doublets.code.doublets import DoubletSolver
from doublets.test import words


class DoubletsTester(unittest.TestCase):
    def test_small_input(self):
        ds = DoubletSolver(["hit", "hot", "dot", "dog", "lot", "log", "cog"])

        self.assertEqual([], ds.get_doublet("ye", "freezer"))
        self.assertEqual(['hit', 'hot', 'dot', 'dog', 'cog'], ds.get_doublet("hit", "cog"))

    def test_large_input(self):
        ds = DoubletSolver(words.dictionary)  # Replace for list of words (dictionary)

        self.assertEqual(["head", "heal", "teal", "tell", "tall", "tail"], ds.get_doublet("head", "tail"))
        self.assertEqual(["door", "boor", "book", "look", "lock"], ds.get_doublet("door", "lock"))
        self.assertEqual(["bank", "bonk", "book", "look", "loon", "loan"], ds.get_doublet("bank", "loan"))
        self.assertEqual(["wheat", "cheat", "cheap", "cheep", "creep", "creed", "breed", "bread"],
                         ds.get_doublet("wheat", "bread"))

        self.assertEqual([], ds.get_doublet("ye", "freezer"))
