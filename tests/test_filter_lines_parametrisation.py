from main import filter_lines
from tests.conftest import lists_equal
import pytest


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
