import pytest
import os


@pytest.fixture(autouse=True)
def prepare_text_file_1(tmp_path):
    target_file = os.path.join(tmp_path, 'test_1.txt')
    with open(target_file, 'w') as file:
        lines = ['this\n',
                 'si\n',
                 'prepeared\n',
                 'text\n']
        file.writelines(lines)
    return target_file
