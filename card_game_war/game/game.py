class Game(object):
    class Suit(object):
        SPADE = 0
        CLUB = 1
        DIAMOND = 2
        HEART = 3

    suits = (Suit.SPADE, Suit.CLUB, Suit.DIAMOND, Suit.HEART)

    class Rank(object):
        JACK = 11
        QUEEN = 12
        KING = 13
        ACE = 14

    ranks = tuple(i for i in range(2, 11)) + (Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE)

    cards = [(rank, suit) for suit in suits for rank in ranks]

    def play(self, player1_cards, player2_cards):
        over = False
        winner = None

        while not over:
            card1 = player1_cards.pop(0)
            card2 = player2_cards.pop(0)

            if self.play_round(card1, card2) == 0:
                player1_cards.append(card1)
                player1_cards.append(card2)

                if not player2_cards:
                    winner = 1
                    over = True
            else:
                player2_cards.append(card1)
                player2_cards.append(card2)

                if not player1_cards:
                    winner = 2
                    over = True

        return winner

    def play_round(self, player1_card, player2_card):
        if player1_card[0] > player2_card[0]:
            return 1
        elif player1_card[0] < player2_card[0]:
            return 2
        else:
            return int(player1_card[1] < player2_card[1]) + 1
