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

    f_errcode_ignores: str = "--ignore=E501,W503"

    subprocess.run(
        [
            "flake8",
            ".",
            f_errcode_ignores,
            "--count",
            "--show-source",
            "--statistics",
        ]
    )
    subprocess.run(
        [
            "flake8",
            ".",
            f_errcode_ignores,
            "--count",
            "--exit-zero",
            "--max-complexity=10",
            "--max-line-length=127",
            "--statistics",
        ]
    )
