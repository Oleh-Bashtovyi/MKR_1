def read_file(filename: str) -> list[str]:
    """
  Read and return all lines in specified file.
  :return: list of lines
  """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    lines = read_file("test.txt")
    print(lines)
