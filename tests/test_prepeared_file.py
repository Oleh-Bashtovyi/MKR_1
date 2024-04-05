from main import filter_lines, read_file, write_lines_to_file
from .conftest import lists_equal


def test_read_file(prepare_text_file):
    lines = read_file(prepare_text_file)
    expected_lines = ['this is tEsting example\n',
                      'with uinTestng fixture\n',
                      'that creates prepared file\n',
                      'that must be Tested and\n',
                      'and Idk what to say more\n',
                      'except RetesTing\n']
    assert lists_equal(lines, expected_lines)


def test_read_file_filter_case_sensetive(prepare_text_file):
    lines = read_file(prepare_text_file)
    filtred_lines = filter_lines(lines, "Test", True)
    expected_filtred_lines = ['with uinTestng fixture\n',
                              'that must be Tested and\n', ]
    assert lists_equal(filtred_lines, expected_filtred_lines)


def test_read_file_filter_case_insensetive(prepare_text_file):
    lines = read_file(prepare_text_file)
    filtred_lines = filter_lines(lines, "Test", False)
    expected_filtred_lines = ['this is tEsting example\n',
                              'with uinTestng fixture\n',
                              'that must be Tested and\n',
                              'except RetesTing\n']
    assert lists_equal(filtred_lines, expected_filtred_lines)


def test_read_file_filter_case_sensetive_write(prepare_text_file, prepare_text_file_to_write):
    lines = read_file(prepare_text_file)
    filtred_lines = filter_lines(lines, "Test", True)
    write_lines_to_file(prepare_text_file_to_write, filtred_lines)
    writen_lines = read_file(prepare_text_file_to_write)
    expected_filtred_lines = ['with uinTestng fixture\n',
                              'that must be Tested and\n', ]
    assert lists_equal(expected_filtred_lines, writen_lines)
