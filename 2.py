import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['J', 'Q', 'K']: return 10
        elif self.rank == 'A': return 11
        return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ["♠", "♣", "♥", "♦"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        score = sum(card.value() for card in self.cards)     
        return score

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

def play_game():
    deck = Deck()
    player = Hand()
    computer = Hand()

    for _ in range(2):
        player.add_card(deck.deal())
        computer.add_card(deck.deal())

    while True:
        print("\n" + "="*50)
        print(f"თქვენი კარტები: {player} | ქულა: {player.get_score()}")
        print("="*50)
        print("1. დამატება | 2. გაჩერება")
        choice = input("აირჩიეთ მოქმედება: ")

        if choice == '1':
            player.add_card(deck.deal())
            if player.get_score() > 21:
                print(f"\n[!] თქვენი კარტები: {player} (ქულა: {player.get_score()})")
                print(">> 21 გადააცილეთ! თქვენ წააგეთ.")
                return
        elif choice == '2':
            break
        else:
            print("არასწორი არჩევანი!")

    # კომპიუტერის სვლები
    while computer.get_score() < 17:
        computer.add_card(deck.deal())

    print(f"\n[!] კომპიუტერის კარტები: {computer} (ქულა: {computer.get_score()})")
    
    p_score, c_score = player.get_score(), computer.get_score()
    
    if c_score > 21 or (p_score <= 21 and p_score > c_score):
        print(">> თქვენ მოიგეთ!")
    elif p_score == c_score:
        print(">> ფრეა! თავიდან ვარიგებთ.")
        play_game()
    else:
        print(">> თქვენ წააგეთ!")

if __name__ == "__main__":
    play_game()