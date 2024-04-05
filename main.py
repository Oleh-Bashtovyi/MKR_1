def read_file(filename: str) -> list[str]:
    """
    Read and return all lines in specified file.
    :return: list of lines
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def filter_lines(lines: list[str], keyword: str, case_sensetive: bool = True) -> list[str]:
    """
    Select lines that contain specified keyword.
    :param case_sensetive: is case sensetive filtering
    :param lines: lines that must be filtered
    :param keyword:  filter by keyword
    :return:  list of string that contain keyword
    """
    filtered_lines = []

    if not case_sensetive:
        keyword = keyword.lower()

    for line in lines:
        if (case_sensetive and keyword in line) or keyword in line.lower():
            filtered_lines.append(line)

    return filtered_lines


def write_lines_to_file(filename: str, lines: list[str]):
    """
    Write all lines to specified file
    """
    with open(filename, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    lines = read_file("test.txt")
    print(lines)
    filtered_lines = filter_lines(lines, "REQ")
    print(filtered_lines)
    filtered_lines = filter_lines(lines, "rEq", False)
    print(filtered_lines)
    write_lines_to_file("filtered.txt", filtered_lines)
