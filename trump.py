"""Trump.py
    
    Trump card for python

"""
import random
from collections import deque
DECK = [
    ("SPD", "A"), ("SPD", "2"), ("SPD", "3"), ("SPD", "4"), ("SPD", "5"),
    ("SPD", "6"), ("SPD", "7"), ("SPD", "8"), ("SPD", "9"), ("SPD", "10"),
    ("SPD", "J"), ("SPD", "Q"), ("SPD", "K"),
    ("DIA", "A"), ("DIA", "2"), ("DIA", "3"), ("DIA", "4"), ("DIA", "5"),
    ("DIA", "6"), ("DIA", "7"), ("DIA", "8"), ("DIA", "9"), ("DIA", "10"),
    ("DIA", "J"), ("DIA", "Q"), ("DIA", "K"),
    ("HRT", "A"), ("HRT", "2"), ("HRT", "3"), ("HRT", "4"), ("HRT", "5"),
    ("HRT", "6"), ("HRT", "7"), ("HRT", "8"), ("HRT", "9"), ("HRT", "10"),
    ("HRT", "J"), ("HRT", "Q"), ("HRT", "K"),
    ("CLV", "A"), ("CLV", "2"), ("CLV", "3"), ("CLV", "4"), ("CLV", "5"),
    ("CLV", "6"), ("CLV", "7"), ("CLV", "8"), ("CLV", "9"), ("CLV", "10"),
    ("CLV", "J"), ("CLV", "Q"), ("CLV", "K"),
]


class Trump:
    def __init__(self, contain_joker=False, doshufflefirst=True):
        self.deck = deque(DECK)
        if contain_joker:
            self.deck.appendleft(("JOKER", "JOKER"))
        if doshufflefirst:
            self.shuffle()

    def choice(self) -> tuple:
        return self.deck.popleft()

    def choices(self, count: int):
        result = [self.choice() for _ in range(count)]
        return result

    def dispense(self, count: int):
        result = []
        for i in range(count):
            code = f"""player_{i} = list(self.deck)[{i}::{count}];result.append(player_{i})
            """
            exec(code)
        return result

    def shuffle(self):
        random.shuffle(self.deck)
