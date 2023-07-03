# tsparxer

Lexing and Parsing the TypeScript programming language using Python's PLY library.

## Prerequisites

Before you continue, ensure you have met the following requirements:

| Requirement | Version                                                |
| ----------- | ------------------------------------------------------ |
| Python      | 3.10+                                                  |
| Poetry      | [Latest](https://python-poetry.org/docs/#installation) |

## Installation

1. Clone the repository & `cd` into it:

```sh
git clone https://github.com/anntnzrb/tsparxer.git
cd tsparxer/
```

2. Install dependencies using Poetry:

```sh
poetry install
```

## Running the Application

### Terminal

To run the application via terminal, use the following command:

```sh
poetry run app
```

The will present 2 options, the first for testing the **lexer** and the latter
for testing the **parser**.

### GUI

To run the graphical version of the application , use the following command:

```sh
poetry run gui
```

## Running Tests

To run the tests (lexer + parser), use the following command:

```sh
poetry run test
```

## Authors

| Name                  | Contact                                               |
| --------------------- | ----------------------------------------------------- |
| Juan Antonio González | [juangonz@espol.edu.ec](mailto:juangonz@espol.edu.ec) |
| Paul Gudiño           | [pgudino@espol.edu.ec](mailto:pgudino@espol.edu.ec)   |
| Christopher Villa     | [cgvilla@espol.edu.ec](mailto:cgvilla@espol.edu.ec)   |
