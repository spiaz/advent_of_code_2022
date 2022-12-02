#%%
from typing import Dict, List, Literal
from pydantic import BaseModel
from pathlib import Path

Shape = Literal["rock", "scissor", "paper"]

winner_to_loser: Dict[Shape, Shape] = {
    "rock": "scissor",
    "scissor": "paper",
    "paper": "rock",
}

shape_value: Dict[Shape, int] = {"rock": 1, "paper": 2, "scissor": 3}


class Round(BaseModel):
    elf: Shape
    me: Shape

    def process(self) -> int:
        value = 0
        if self.me == self.elf:
            value = 3
        if winner_to_loser[self.me] == self.elf:
            value = 6
        return value + shape_value[self.me]


def process_rounds(rounds: List[Round]) -> int:
    return sum([x.process() for x in rounds])


def parse_strategy(s: str) -> List[Round]:
    correspondance = {
        "A": "rock",
        "B": "paper",
        "C": "scissor",
        "X": "rock",
        "Y": "paper",
        "Z": "scissor",
    }
    for orig, val in correspondance.items():
        s = s.replace(orig, val)

    rounds_s = [x.split() for x in s.splitlines()]
    return [Round(elf=x[0], me=x[1]) for x in rounds_s]


def total_score(strategy: str) -> int:
    rounds = parse_strategy(strategy)
    return process_rounds(rounds)


test = """A Y
B X
C Z"""


assert total_score(test) == 15
# %%
strategy = Path("input.txt").read_text()

total_score(strategy)
# %%  Part 2

loser_to_winner = {y: x for x, y in winner_to_loser.items()}


def parse_strategy2(s: str) -> List[Round]:
    correspondance = {
        "A": "rock",
        "B": "paper",
        "C": "scissor",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    for orig, val in correspondance.items():
        s = s.replace(orig, val)

    expectations = [x.split() for x in s.splitlines()]

    rounds = []
    for elf, outcome in expectations:
        if outcome == "draw":
            me = elf
        elif outcome == "win":
            me = loser_to_winner[elf]
        elif outcome == "lose":
            me = winner_to_loser[elf]
        rounds.append(Round(elf=elf, me=me))

    return rounds


def total_score2(strategy: str) -> int:
    rounds = parse_strategy2(strategy)
    return process_rounds(rounds)


assert total_score2(test) == 12

# %%
total_score2(strategy)


# %%
