import random
import logging

# ლოგირების კონფიგურაცია
logging.basicConfig(
    encoding='utf-8',
    filename='lottery.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

class LotteryGame:
    def __init__(self, jackpot):
        self.jackpot = jackpot
        self.winning_numbers = set(random.sample(range(1, 50), 6))

    def calculate_prize(self, matches):
        # ლოგიკა მოგების გამოსათვლელად
        if matches == 6:
            return self.jackpot
        elif matches == 5:
            return self.jackpot * 0.60
        elif matches == 4:
            return self.jackpot * 0.40
        elif matches == 3:
            return self.jackpot * 0.20
        return 0

    def play(self, player):
        matches = len(self.winning_numbers.intersection(player.numbers))
        prize = self.calculate_prize(matches)
        
        # ლოგირება
        log_entry = f"მოთამაშე: {player.name}, რიცხვები: {sorted(list(player.numbers))}, დამთხვევები: {matches}, მოგება: {prize}"
        logging.info(log_entry)
        
        return matches, prize

class Player:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = set(numbers)

# --- პროგრამის გაშვება ---

# 1. მოთამაშის მონაცემების შეყვანა
name = input("შეიყვანეთ თქვენი სახელი: ")
user_input = input("შეიყვანეთ 6 რიცხვი (1-49), მძიმით გამოყოფილი: ")
user_nums = [int(x.strip()) for x in user_input.split(',')]

player = Player(name, user_nums)
game = LotteryGame(1000000)

# 2. თამაშის პროცესი
matches, prize = game.play(player)

# 3. შედეგის გამოსახვა
print(f"\n--- გათამაშების შედეგები ---")
print(f"გამარჯვებული რიცხვები: {sorted(list(game.winning_numbers))}")
print(f"თქვენი რიცხვები: {sorted(list(player.numbers))}")
print(f"დამთხვევების რაოდენობა: {matches}")
print(f"თქვენ მოიგეთ: {prize} ლარი")