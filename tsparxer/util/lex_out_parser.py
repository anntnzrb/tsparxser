"""
This module allows parsing lex output and write the parsed results to a file.
"""

import re
from typing import Any, Dict, List

def parse_lex_output(input: str) -> List[Dict[str, Any]]:
    result = []
    pattern = r"LexToken\((\w+),('(.*?)'|(\d+)),(\d+),(\d+)\)"
    for line in input.splitlines():
        match = re.match(pattern, line)
        if match:
            token_type, value = match.group(1), match.group(3) or match.group(4)
            result.append({"type": token_type, "value": value})
    return result

def parse() -> None:
    # specify input and output files
    FILE_IN: str = "data/lex_data.in"
    FILE_OUT: str = "data/parsed.out"

    # read input & write to file
    with open(FILE_IN, 'r') as file:
        lex_output = file.read()

    with open(FILE_OUT, 'w') as FILE_OUT:
        for item in parse_lex_output(lex_output):
            FILE_OUT.write(str(item) + '\n')