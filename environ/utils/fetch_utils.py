"""
Functions to query the subgraph for data.
"""

import time
from typing import Union

import requests


def run_query(http: str, query_scripts: str) -> dict[str, Union[int, str]]:
    """
    execute query without variable parameters
    """
    while True:
        try:
            # endpoint where you are making the request
            request = requests.post(
                http, "", json={"query": query_scripts}, timeout=120
            )
            if request.status_code == 200:
                return request.json()
        except:  # pylint: disable=bare-except
            time.sleep(10)


def run_query_var(
    http: str, query_scripts: str, var: dict[str, Union[int, str]]
) -> dict[str, Union[int, str]]:
    """
    execute query with variable parameters
    """
    while True:
        try:
            # endpoint where you are making the request
            request = requests.post(
                http, "", json={"query": query_scripts, "variables": var}, timeout=120
            )
            if request.status_code == 200:
                return request.json()
        except:  # pylint: disable=bare-except
            time.sleep(10)
