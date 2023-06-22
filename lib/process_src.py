import subprocess


def format() -> None:
    """
    Format all project files using black formatter.
    """
    subprocess.run(["black", "."])


def lint() -> None:
    """
    Lint all project files using flake8.
    """
    subprocess.run(["flake8", ".", "--count", "--show-source", "--statistics"])
    subprocess.run(
        [
            "flake8",
            ".",
            "--count",
            "--exit-zero",
            "--max-complexity=10",
            "--max-line-length=127",
            "--statistics",
        ]
    )
