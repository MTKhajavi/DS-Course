from test_helper import *
from task import *

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    words1_1 = ["ac", "abd", "b"]
    words1_2 = ["ae", "bd"]
    tests = list()
    tests.append((words1_1, words1_2, 3))

    words2_1 = ["ab", "abcde"]
    words2_2 = ["abc", "abcd", "abcdef"]
    tests.append([words2_1, words2_2, 5])

    words3_1 = ["abcd"]
    words3_2 = ["abcde", "abcdf", "aa", "ad"]
    tests.append([words3_1, words3_2, 3])

    for test in tests:
        test_function(test[2], main, test[0], test[1])
