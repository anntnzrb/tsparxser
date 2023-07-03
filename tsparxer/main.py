#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
main.py: Entry point for the TypeScript Lexer + Parser implementation
"""

from typing import List
from ply.lex import LexToken
import PySimpleGUI as sg

from .util import read_file
from .lexer import Lexer as TSLexer
from .parser import Parser as TSParser
from tsparxer.parser import ParserSyntaxError


def main():
    samples_dir: str = "data"
    file: str = f"{samples_dir}/data.txt"
    data: str = read_file(file)

    # numerical menu
    print("1: Lex (Read contents of file)")
    print("2: Yacc (Interactive prompt)")
    choice = int(input("Choose an option: "))

    # create lexer and feed data
    lexer: TSLexer = TSLexer()
    lexed: List[LexToken] = lexer.lex(data)

    # option 1 : lex
    if choice == 1:
        # show tokens
        for t in lexed:
            print(t)

    # option 2 : yacc
    elif choice == 2:
        parser: TSParser = TSParser(lexer)
        parser.run_loop("TSParser> ")
    else:
        print("Invalid choice")


def clear_windows(*windows):
    for window in windows:
        window.update("")


def gui() -> None:
    layout = [
        [sg.Text("Enter code to parse:")],
        [
            sg.Input(tooltip="Input data to parse"),
            sg.Button("Parse", bind_return_key=True),
        ],
        [
            sg.Column(
                [
                    [
                        sg.Output(
                            size=(20, 20),
                            tooltip="Tokens are shown here",
                            key="-OUT-TOKENS-",
                        )
                    ],
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Output(
                            size=(20, 20),
                            tooltip="Parsing errors are shown here",
                            key="-OUT-PARSED-",
                        )
                    ],
                ]
            ),
        ],
        [sg.Button("Quit")],
    ]

    window = sg.Window("TSParxer", layout, finalize=True)

    # create lexer and parser
    lexer: TSLexer = TSLexer()
    parser: TSParser = TSParser(lexer)

    while True:
        ev, val = window.read()
        if ev == sg.WINDOW_CLOSED or ev == "Quit":
            break

        # process input when 'Parse' button or 'Enter' key is pressed
        if ev == "Parse":
            data = val[0]
            lexed: List[LexToken] = lexer.lex(data)

            # clear output windows beforehand
            clear_windows(window["-OUT-TOKENS-"], window["-OUT-PARSED-"])

            # show tokens
            for t in lexed:
                print(t, file=window["-OUT-TOKENS-"])

            try:
                parser.parse(data)
            except ParserSyntaxError as e:
                print(str(e), file=window["-OUT-PARSED-"])

    window.close()


if __name__ == "__main__":
    main()
