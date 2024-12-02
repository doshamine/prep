from stack import Stack

def is_balanced_sequence(sequence: str) -> str:
    """
    Проверяет, является ли последовательность скобок сбалансированной.

    Входные параметры:
    sequence - строка, состоящая из скобок (,[,{,},],).

    Возвращаемое значение:
    "Последовательность сбалансирована" - если последовательность сбалансирована
    "Последовательность не сбалансирована" - если последовательность не сбалансирована
    """
    stack = Stack()
    left_brackets = '{[('
    right_brackets = '}])'
    correct_pairs = '{}', '[]', '()'

    for bracket in sequence:

        if left_brackets.count(bracket) != 0:
            stack.push(bracket)
        elif right_brackets.count(bracket) != 0:
            if stack.is_empty():
                return 'Последовательность не сбалансирована'
            paired_bracket = stack.pop()

            if paired_bracket + bracket not in correct_pairs:
                return 'Последовательность не сбалансирована'

    return 'Последовательность сбалансирована'