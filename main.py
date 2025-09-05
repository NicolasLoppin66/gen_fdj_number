import random
from typing import List, Tuple

class FDJGame:
    def __init__(self, name: str, main_numbers: int, main_range: int, extra_numbers: int = 0, extra_range: int = 0):
        self.name = name
        self.main_numbers = main_numbers
        self.main_range = main_range
        self.extra_numbers = extra_numbers
        self.extra_range = extra_range

    def generate_numbers(self) -> Tuple[List[int], List[int]]:
        main_draw = random.sample(range(1, self.main_range + 1), self.main_numbers)
        extra_draw = random.sample(range(1, self.extra_range + 1), self.extra_numbers) if self.extra_numbers > 0 else []
        return main_draw, extra_draw

    def __str__(self) -> str:
        main_draw, extra_draw = self.generate_numbers()
        result = f"{self.name} Draw: {sorted(main_draw)}"
        if extra_draw:
            result += f" + {sorted(extra_draw)}"
        return result

class Loto(FDJGame):
    def __init__(self):
        super().__init__('Loto', 5, 49, 1, 10)

class EuroMillions(FDJGame):
    def __init__(self):
        super().__init__('EuroMillions', 5, 50, 2, 12)

def main():
    games = [Loto(), EuroMillions()]
    for game in games:
        print(game)

if __name__ == "__main__":
    main()
