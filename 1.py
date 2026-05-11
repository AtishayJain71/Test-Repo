"""
This is a test file with intentional bugs and code quality issues
for testing the CodeOptimizer code review API
"""

import os
import json
from typing import Dict, List


# Bug 1: Unhandled exception - file might not exist
def load_user_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


# Bug 6: Missing error handling with external API
def fetch_data_from_api(url):
    import requests
    response = requests.get(url)
    return response.json()  # No timeout, no error handling


# Bug 7: Type inconsistency
def divide_numbers(a, b):
    return a / b  # No type checking, b could be string


# Unused imports (already imported os and json at top)
import sys
import warnings


print("This test file contains multiple intentional bugs for API testing")
