#%%
from pathlib import Path
from typing import Dict, Tuple

example01 = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def count_calories(log: str) -> Dict[int, int]:
    log_by_elf = [x for x in log.split("\n\n")]

    elf_to_cal = {}

    for elf, cals in enumerate(log_by_elf, 1):
        elf_to_cal[elf] = sum([int(x) for x in cals.split()])

    return elf_to_cal


assert 24000 == count_calories(example01)[4]


def elf_max_cals(cnt: dict) -> Tuple[int, int]:
    max_elf = max(cnt, key=cnt.get)
    return max_elf, cnt[max_elf]


def count_and_max(log: str) -> Tuple[int, int]:
    cnt = count_calories(log)
    return elf_max_cals(cnt)


assert (4, 24000) == count_and_max(example01)

# %%

input = Path("input.txt").read_text()

count_and_max(input)
# %%
# Part 2


def sum_max_n_cals(log: str, n=3) -> int:
    cnt = count_calories(log)
    cals = 0
    for i in range(n):
        elf, cal = elf_max_cals(cnt)
        cals += cal
        cnt.pop(elf)
    return cals


assert sum_max_n_cals(example01) == 45000

# %%
sum_max_3_cals(input)
# %%
