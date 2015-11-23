import unittest
from card_game_war.game.game import Game


class TestGame(unittest.TestCase):
    def get_card(self, rank=2, suit=0):
        return Game.cards[rank - 2 + 13 * suit]

    def test_play_game(self):
        g = Game()

        player1 = [self.get_card(10, 1), self.get_card(11, 1), self.get_card(12, 1)]
        player2 = [self.get_card(9, 2), self.get_card(12, 2), self.get_card(13, 2)]

        self.assertEqual(2, g.play(player1, player2), "the player loses when they run out of cards")

    def test_play_round(self):
        g = Game()

        self.assertEqual(2, g.play_round(self.get_card(8), self.get_card(10)),
                         msg="the highest rank wins the cards in the round")

        self.assertEqual(1, g.play_round(self.get_card(Game.Rank.QUEEN), self.get_card(Game.Rank.JACK)),
                         msg="queens are higher rank than jacks")

        self.assertEqual(1, g.play_round(self.get_card(Game.Rank.ACE), self.get_card(Game.Rank.KING)),
                         msg="aces are higher rank than kings")

        self.assertEqual(2, g.play_round(self.get_card(9, Game.Suit.SPADE), self.get_card(9, Game.Suit.CLUB)),
                         msg="if the ranks are equal, clubs beat spades")

        self.assertEqual(1, g.play_round(self.get_card(9, Game.Suit.DIAMOND), self.get_card(9, Game.Suit.CLUB)),
                         msg="if the ranks are equal, diamonds beat clubs")

        self.assertEqual(1, g.play_round(self.get_card(9, Game.Suit.HEART), self.get_card(9, Game.Suit.DIAMOND)),
                         msg="if the ranks are equal, hearts beat diamonds")


if __name__ == '__main__':
    unittest.main()
