import pytest
from brackets import is_balanced_sequence


@pytest.mark.parametrize(
    'sequence, expected',
    (
        ('(((([{}]))))', 'Последовательность сбалансирована'),
        ('[([])((([[[]]])))]{()}', 'Последовательность сбалансирована'),
        ('{{[()]}}', 'Последовательность сбалансирована'),
        ('}{}', 'Последовательность не сбалансирована'),
        ('{{[(])]}}', 'Последовательность не сбалансирована'),
        ('[[{())}]', 'Последовательность не сбалансирована')
    )
)
def test_is_balanced_sequence(sequence, expected):
    result = is_balanced_sequence(sequence)
    assert result == expected