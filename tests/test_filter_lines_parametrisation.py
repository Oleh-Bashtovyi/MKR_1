from main import filter_lines
import pytest


def lists_equal(list1: list[str], list2: list[str]):
    if len(list1) != len(list2):
        return False

    for str1, str2 in zip(list1, list2):
        if str1 != str2:
            return False
    return True


@pytest.mark.parametrize("input_list, keyword, case_sensetive, expected_list",
                         [
                             (["this is To be honestly", "an interestingly honeStler",
                               "You arHonest pers", "my badhoneSt reaction",
                               "This is not contain honeRt"], "honeS", True,
                              ["an interestingly honeStler", "my badhoneSt reaction"]),
                             (["this is To be honestly", "an interestingly honeStler",
                               "You arHonest pers", "my badhoneSt reaction",
                               "This is not contain honeRt"], "honeS", False,
                              ["this is To be honestly", "an interestingly honeStler",
                               "You arHonest pers", "my badhoneSt reaction"]),
                         ])
def test_filtering(input_list, keyword, case_sensetive, expected_list):
    filtered_lines = filter_lines(input_list, keyword, case_sensetive)
    assert lists_equal(filtered_lines, expected_list)
