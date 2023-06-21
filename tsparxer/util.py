import re
from typing import Any, Dict, List


def read_file(file_path: str) -> str:
    """
    Reads the contents of given file and returns it as string.

    :param file_path: The path of the file to read
    """
    with open(file_path, "r") as file:
        f_content = file.read()

    return f_content


def parse_lex_output(input: str) -> List[Dict[str, Any]]:
    result = []
    pattern = r"LexToken\((\w+),('(.*?)'|(\d+)),(\d+),(\d+)\)"
    for line in input.splitlines():
        match = re.match(pattern, line)
        if match:
            t_type, t_val = match.group(1), match.group(3) or match.group(4)
            result.append({"type": t_type, "value": t_val})
    return result


def parse() -> None:
    # specify input and output files
    FILE_IN: str = "data/lex_data.in"
    FILE_OUT: str = "data/parsed.out"

    # read input & write to file
    with open(FILE_IN, "r") as file:
        lex_output = file.read()

    with open(FILE_OUT, "w") as file:
        for item in parse_lex_output(lex_output):
            file.write(str(item) + "\n")

    print("Parsing successful, be wary of strings and numbers mixing.")
