"""
This module provides utilities for loading environment variables from a `.env` file.

The `.env` file is a simple text file with each environment variable listed one per line, in the
format of `KEY="Value"`. The lines starting with `#` are ignored.
"""
from dotenv import dotenv_values

config = dotenv_values(".env")
