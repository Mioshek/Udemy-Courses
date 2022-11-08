import random as Random
import time
# Two useful variables for creating Cards.
suite = '♥ ♣ ♦ ♠'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck():
    def __init__(self):
        print("Creating New Ordered Deck")
        self.deck = [(s+r) for s in suite for r in ranks]

    def shuffle_cards(self):
        Random.shuffle(self.deck)

    def split_equally(self):
        self.player1_cards = self.deck[:26]
        self.player2_cards = self.deck[26:]


class Hand():
    def __init__(self, cards):
        self.hand = cards

    def add_card(self, added_cards):
        self.hand.extend(added_cards)

    def remove_card(self):
        return self.hand.pop(0)

    def display_current_deck(self):
        print(self.hand)

    def check_size_of_player_deck(self):
        print(len(self.hand))


class Player():
    def __init__(self, hand, player_name):
        self.hand = hand
        self.player_name = player_name

    def __str__(self):
        return self.hand

    def check_player_has_cards(self):
        return False if len(self.hand.hand) == 0 else True

    def play_card(self):
        self.played_card = self.hand.remove_card()
        print("{} has placed {}".format(self.player_name, self.played_card))
        return self.played_card

    def play_three_cards(self):
        self.war_cards = []
        for i in range(0, 4):
            if self.check_player_has_cards(): self.war_cards.append(self.hand.remove_card())
            else: return self.war_cards
        return self.war_cards


class Value():
    def __init__(self, played_cards_arr,):
        self.played_cards_arr = played_cards_arr
        self.variety_of_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def value_case1(self):
        return self.variety_of_cards[self.played_cards_arr[0][-1]]
    """value in case if there is (2-9) value or non int cards in 0 place of played_cards_arr"""

    def value_case2(self):
        return self.variety_of_cards[self.played_cards_arr[0][-2:]]
    """value in case if there is (10) value in 0 place of played_cards_arr"""

    def value_case3(self):
        return self.variety_of_cards[self.played_cards_arr[1][-1]]
    """value in case if there is (2-9) value or non int cardsin 1 place of played_cards_arr"""

    def value_case4(self):
        return self.variety_of_cards[self.played_cards_arr[1][-2:]]
    """value in case if there is (10) value in 0 place of played_cards_arr"""

    def who_loses(self):
        if self.played_cards_arr[0][-2] == '1':  value_of_played_card1 = 10
        else: value_of_played_card1 = self.value_case1() if self.played_cards_arr[0][-2] == '♥' or '♣' or '♦' or '♠' else self.value_case2()
        if self.played_cards_arr[1][-2] == '1':  value_of_played_card2 = 10
        else: value_of_played_card2 = self.value_case3() if self.played_cards_arr[1][-2] == '♥' or '♣' or '♦' or '♠' else self.value_case4()  
        if value_of_played_card1 > value_of_played_card2: return 2
        elif value_of_played_card1 < value_of_played_card2:return 1
        else: return 0


# ######################
# #### GAME PLAY #######
# ######################
print("Welcome to War, let's begin...")

# create a deck and split in half
def change_current_player(current_player,player1, player2):
    return player1 if current_player == player2 else player2

def tie_case(current_player, player1, player2,played_cards_arr) -> int:
    war_cards_arr = []
    war_cards_arr.append(current_player.play_three_cards())
    second_player = change_current_player(current_player,player1,player2)
    war_cards_arr.append(second_player.play_three_cards())
    played_cards_arr = (war_cards_arr[0][-1][-2:], war_cards_arr[1][-1][-2:])
    print(war_cards_arr)
    played_cards_arr = Value(played_cards_arr)
    which_player_lost_id = played_cards_arr.who_loses()
    print(which_player_lost_id)
    time.sleep(2)
    if which_player_lost_id == 1: current_player.hand.add_card(played_cards_arr)
    elif which_player_lost_id == 2: current_player = change_current_player(current_player, player1, player2); current_player.hand.add_card(played_cards_arr)
    else: return which_player_lost_id

def main():
    random_sequence_arr = [1, 2]
    deck = Deck()
    deck.shuffle_cards()
    deck.split_equally()
    p1_cards = deck.player1_cards
    p2_cards = deck.player2_cards
    #splited and shuffled
    # naming players
    player1 = Player(Hand(p1_cards), "Computer")
    name = input("Name yourself \n")
    player2 = Player(Hand(p2_cards), name)
    # counting
    war_streak = 0
    round_counter = 0
    # selecting a player
    which_player_starts = Random.choice(random_sequence_arr)
    current_player = player1 if which_player_starts == 1 else player2
    while player1.check_player_has_cards() and player2.check_player_has_cards():
        played_cards_arr = []
        round_counter += 1
        played_cards_arr.append(current_player.play_card())
        current_player = change_current_player(current_player,player1,player2)
        played_cards_arr.append(current_player.play_card())
        current_player = change_current_player(current_player,player1,player2)
        value = Value(played_cards_arr)
        which_player_lost_id = value.who_loses()
        print(which_player_lost_id)
        while which_player_lost_id == 0 and player1.check_player_has_cards() and player2.check_player_has_cards():
            which_player_lost_id =  tie_case(current_player, player1, player2, played_cards_arr)

        which_player_lost_name = current_player if which_player_lost_id == 1 else change_current_player(current_player,player1,player2)
        which_player_lost_name.hand.add_card(played_cards_arr)
        print(" ")
        print("It is time for a new round! \n Here are the current standings: ")
        print(player1.player_name + "'s " +str(len(player1.hand.hand)) + " current cards are:")
        player1.hand.display_current_deck()
        print(" ")
        print(player2.player_name + "'s " +str(len(player2.hand.hand)) + " current cards are:")
        player2.hand.display_current_deck()
        print("Both players played a card!")
        print("___________________________")
        print('')

main()