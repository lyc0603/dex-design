"""
Function to fetch pair data from the graph
"""

import pandas as pd

from environ.constants import UNISWAP_V2_HTTP, QUERY_PAIRS_FIRST_BATCH
from environ.utils.fetch_utils import run_query, run_query_var


def fetch_first_batch(
    query_script: str = QUERY_PAIRS_FIRST_BATCH,
    http: str = UNISWAP_V2_HTTP,
) -> pd.DataFrame:
    """
    Fetch the first batch of pairs from the graph
    """
    data = run_query(http, query_script)
    pairs = data["data"]["pairs"]

    return pd.DataFrame(pairs)


if __name__ == "__main__":
    print(fetch_first_batch())
