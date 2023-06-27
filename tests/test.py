#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
test.py: Run all tests.
"""

import subprocess


def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -m unittest discover`
    """
    subprocess.run(["python", "-m", "unittest", "discover"])
