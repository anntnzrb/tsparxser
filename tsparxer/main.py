#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
main.py: Entry point for the TypeScript Lexer + Parser implementation
"""

from typing import List
from ply.lex import LexToken
from tkinter import *
from tkcode import CodeEditor

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
    root = Tk()
    root.title("GUI")
    root.geometry("1280x720")
    root.configure(bg="#323846")
    root.resizable(False, False)

    # create lexer and parser
    lexer: TSLexer = TSLexer()
    parser: TSParser = TSParser(lexer)

    def run_lex():
        # clear output windows beforehand
        code_output.delete("1.0", END)

        lexer = TSLexer()

        data = code_input.get("1.0", "end-1c")
        lexed: List[LexToken] = lexer.lex(data)

        for t in lexed:
            # Insert lexed token at the end of the text widget
            code_output.insert(END, t)
            # Add a newline after each token
            code_output.insert(END, "\n")

    def run_syntax():
        # clear output windows beforehand
        code_output.delete("1.0", END)

        lexer = TSLexer()

        data = code_input.get("1.0", "end-1c")
        try:
            parser.parse(data)
            code_output.insert("1.0", "All syntax is correct")
        except ParserSyntaxError as e:
            code_output.insert(END, e)

    def clear():
        code_input.delete("1.0", END)

    # Text Label
    insert_str = StringVar()
    input_label = Label(
        root,
        textvariable=insert_str,
        relief=RAISED,
        bd="0px",
        bg="#305265",
        fg="#fff",
    )
    insert_str.set("Insert Code")
    input_label.pack()
    input_label.place(x=70, y=10, width=200, height=50)

    # Syntax label to run
    syntax_str = StringVar()
    syntax_label = Label(
        root,
        textvariable=syntax_str,
        relief=RAISED,
        bd="0px",
        bg="#305265",
        fg="#fff",
    )
    syntax_str.set("Run Syntax")
    syntax_label.pack()
    syntax_label.place(x=850, y=5, width=100, height=50)

    # Lex label to run
    lex_str = StringVar()
    lex_label = Label(
        root,
        textvariable=lex_str,
        relief=RAISED,
        bd="0px",
        bg="#305265",
        fg="#fff",
    )
    lex_str.set("Run Lex")
    lex_label.pack()
    lex_label.place(x=1060, y=5, width=50, height=50)

    # code input
    code_input = CodeEditor(
        root,
        language="TypeScript",
        background="black",
        highlighter="dracula",
        font="consolas",
        autofocus=True,
        blockcursor=True,
        insertofftime=0,
    )

    # code_input.pack(fill="both", expand=True)
    code_input.place(x=50, y=50, width=1200, height=300)
    code_input.configure(bg="#000", insertbackground="#fff")

    # output
    code_output = Text(
        root, font="consolas 15", bg="#1D2722", fg="lightgreen", wrap=WORD
    )
    code_output.place(x=50, y=370, width=1200, height=300)
    code_output.insert("1.0", "-OUTPUT-")

    # Lex button
    lex_btn = PhotoImage(file="./lib/assets/play_btn.png")
    Button(root, image=lex_btn, bg="#323846", bd=0, command=run_lex).place(
        x=1000, y=5, width=64, height=64
    )

    # Syntax button
    syntax_btn = PhotoImage(file="./lib/assets/play_btn.png")
    Button(root, image=lex_btn, bg="#323846", bd=0, command=run_syntax).place(
        x=800, y=5, width=64, height=64
    )

    # Clear button
    clear_btn = PhotoImage(
        file="./lib/assets/clear.png",
    )
    Button(
        root, image=clear_btn, bg="#323846", bd=0, command=clear, text="Clean"
    ).place(x=700, y=5, width=64, height=64)

    # files-bar
    files_bar = Canvas(bg="#403C3E", height=720, width=45, bd=0, borderwidth=0)
    files_bar.place(x=0, y=0)

    # file_icon
    file_icon = PhotoImage(file="./lib/assets/file.png")
    Button(root, image=file_icon, bg="#323846", bd=0).place(
        x=8, y=5, width=32, height=32
    )

    root.mainloop()


if __name__ == "__main__":
    main()
