from typing import List
from string import digits


PUNCTUATIONS ='.!?:;"\'_-[]=|%/'

def remove_numbers(data: List[str]) -> List[str]:
    remove_digits = str.maketrans('', '', digits)
    removed_numbers_data = [item.translate(remove_digits) for item in data]
    return removed_numbers_data


def remove_punctuations(data: List[str]) -> List[str]:
    punctuations_removed_data = [item.translate(str.maketrans('', '', PUNCTUATIONS)).strip() for item in data]
    return punctuations_removed_data
