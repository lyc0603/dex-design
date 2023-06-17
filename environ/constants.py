"""
Script to store all the constants used in the project
"""

from environ.settings import PROJECT_ROOT

# Path to the data folder
RAW_DATA_PATH = PROJECT_ROOT / "raw_data"

# The graph http
UNISWAP_V2_HTTP = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"

# The graph query scripts
QUERY_PAIRS_FIRST_BATCH = """
query {
  pairs(first: 1000, orderBy: id, orderDirection: asc) {
    id
    token0 {
      decimals
      id
      name
      symbol
    }
    token1 {
      decimals
      id
      name
      symbol
    }
  }
}
"""
