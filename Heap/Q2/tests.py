from test_helper import run_common_tests, failed, passed, get_answer_placeholders, test_function
from task import find_difference


if __name__ == '__main__':
    tests = [
        (0, [20, 8, 22, 4, 12, 10, 14], 7, 7),
        (9, [1, 2, 3, 4, 5, 6], 5, 4),
        (57, [-6, -55, 2], 3, 1)
    ]
    for test in tests:
        test_function(test[0], find_difference, test[1], test[2], test[3])
