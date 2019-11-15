from .eliminate_zeros import eliminate_zeros
from .sort_descending import sort_descending
from .check_length import check_length
from .eliminate_front import eliminate_front


def hh(answers):
    while True:
        eliminate_zeros(answers)
        if not answers:
            return True

        sort_descending(answers)
        N = answers.pop(0)
        if check_length(N, answers):
            return False

        eliminate_front(N, answers)
