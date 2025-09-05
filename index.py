import random
from typing import List, Tuple
from collections import Counter


class FDJGame:
    def __init__(
        self,
        name: str,
        main_numbers: int,
        main_range: int,
        extra_numbers: int = 0,
        extra_range: int = 0,
    ):
        self.name = name
        self.main_numbers = main_numbers
        self.main_range = main_range
        self.extra_numbers = extra_numbers
        self.extra_range = extra_range

    def generate_numbers(self) -> Tuple[List[int], List[int]]:
        main_draw = random.sample(range(1, self.main_range + 1), self.main_numbers)
        extra_draw = (
            random.sample(range(1, self.extra_range + 1), self.extra_numbers)
            if self.extra_numbers > 0
            else []
        )
        return main_draw, extra_draw

    def __str__(self) -> str:
        main_draw, extra_draw = self.generate_numbers()
        result = f"{self.name} Draw: {sorted(main_draw)}"
        if extra_draw:
            result += f" + {sorted(extra_draw)}"
        return result


class Loto(FDJGame):
    def __init__(self):
        super().__init__("Loto", 5, 49, 1, 10)


class EuroMillions(FDJGame):
    def __init__(self):
        super().__init__("EuroMillions", 5, 50, 2, 12)


class EuroDream(FDJGame):
    def __init__(self):
        super().__init__("EuroDream", 6, 40, 1, 5)


class GrandLoto(FDJGame):
    def __init__(self):
        super().__init__("GrandLoto", 5, 49, 1, 10)


class Keno(FDJGame):
    def __init__(self):
        super().__init__("Keno", 10, 70, 0, 0)


class FDJGameAI(FDJGame):
    def __init__(
        self,
        name: str,
        main_numbers: int,
        main_range: int,
        extra_numbers: int = 0,
        extra_range: int = 0,
    ):
        super().__init__(name, main_numbers, main_range, extra_numbers, extra_range)
        self.previous_results = []

    def simulate_previous_results(self, num_results: int):
        for _ in range(num_results):
            self.previous_results.append(self.generate_numbers())

    def analyze_trends(self) -> Tuple[List[int], List[int]]:
        main_numbers = [num for result in self.previous_results for num in result[0]]
        extra_numbers = [num for result in self.previous_results for num in result[1]]
        main_counter = Counter(main_numbers)
        extra_counter = Counter(extra_numbers)

        most_common_main = [
            num for num, _ in main_counter.most_common(self.main_numbers)
        ]
        most_common_extra = [
            num for num, _ in extra_counter.most_common(self.extra_numbers)
        ]

        return most_common_main, most_common_extra

    def generate_ai_numbers(self) -> Tuple[List[int], List[int]]:
        main_draw, extra_draw = self.analyze_trends()

        # Fill with random numbers if we don't have enough common numbers
        while len(main_draw) < self.main_numbers:
            num = random.randint(1, self.main_range)
            if num not in main_draw:
                main_draw.append(num)

        while len(extra_draw) < self.extra_numbers:
            num = random.randint(1, self.extra_range)
            if num not in extra_draw:
                extra_draw.append(num)

        return sorted(main_draw), sorted(extra_draw)

    def __str__(self) -> str:
        main_draw, extra_draw = self.generate_ai_numbers()
        result = f"{self.name} AI Draw: {main_draw}"
        if extra_draw:
            result += f" + {extra_draw}"
        return result


def main():
    games = [
        FDJGameAI("EuroMillions", 5, 50, 2, 12),
        FDJGameAI("EuroDream", 6, 40, 1, 5),
        FDJGameAI("Loto", 5, 49, 1, 10),
        FDJGameAI("GrandLoto", 5, 49, 1, 10),
        FDJGameAI("Keno", 10, 70, 0, 0),
    ]
    for game in games:
        game.simulate_previous_results(10)  # Simulate 100 previous results
        print(game)


if __name__ == "__main__":
    main()
