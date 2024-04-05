import pytest
import os


@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        lines = ['this is tEsting example\n',
                 'with uinTestng fixture\n',
                 'that creates prepared file\n',
                 'that must be Tested and\n',
                 'and Idk what to say more\n',
                 'except RetesTing\n']
        file.writelines(lines)
    return target_file


@pytest.fixture(autouse=True)
def prepare_text_file_to_write(tmp_path):
    target_file = os.path.join(tmp_path, 'filter.txt')
    return target_file


def lists_equal(list1: list[str], list2: list[str]):
    if len(list1) != len(list2):
        return False

    for str1, str2 in zip(list1, list2):
        if str1 != str2:
            return False
    return True
