from enum import Enum
from typing import List
import random

class Grade(Enum):
    """
    enum which links grades to their minimum score (inclusive)
    """
    DISTINCTION = 80
    UPPER_MERIT = 65
    LOWER_MERIT = 50
    PASS = 40
    UNSUCCESSFUL = 0

    @classmethod
    def from_result(cls, result: float) -> str:
        """
        method to convert a result to a grade
        """
        return [g.name.lower() for g in cls if g.value >= result][0]


def get_count_in_range(results: List[int], min_result: int = None, max_result: int = None) -> int:
    """
    function which returns the number of items in a list which fall within a range (inclusive)
    """
    if not min_result:
        min_result = min(results)
    if not max_result:
        max_result = max(results)

    return len([r for r in results if r >= min_result and r <= max_result])


def get_longest_increasing_run(results: List[int]) -> List[int]:
    """
    function that returns a subset of the list representing the longest run of increasing values
    """
    longest = run = [results[0]]  # the first value will always be added, and we want to safely check the previous value during iteration

    i = 1
    while i < len(results):
        if results[i] > results[i - 1]: # as above, i - 1 would crash if we started at 0
            run.append(results[i])
        elif len(run) > len(longest):   # assuming that equal lengths do not supercede previous best
            longest = run
            run = [results[i]]
        else:
            run = [results[i]]
        
        i = i + 1

    return longest


# results = [39,32,62,88,51,62,64,81,77]
results = random.sample(range(1, 101), 30)
print(results)

arithmetic_mean = round(sum(results)/len(results), 2)
print("The mean percentage mark is", arithmetic_mean)

grade = Grade.from_result(arithmetic_mean)
print("The grade for the average result is", grade)

min_result = min(results)
max_result = max(results)
print(f"The lowest score is {min_result}\nThe highest score is {max_result}")

below_forty_count = get_count_in_range(results, max_result=39)
between_fifty_and_seventy_nine = get_count_in_range(results, 50, 79)
print(f"The number of scores below 40 is {below_forty_count}\nThe number of scores between 50 and 79 is {between_fifty_and_seventy_nine}")

longest_run = get_longest_increasing_run(results)
print(f"The longest run of increases is {longest_run}")
