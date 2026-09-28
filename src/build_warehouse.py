from pathlib import Path

import duckdb

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "warehouse.duckdb"

with duckdb.connect(str(DATABASE_PATH)) as con:
    con.execute("CREATE SCHEMA IF NOT EXISTS raw_tournaments")
    con.execute("CREATE SCHEMA IF NOT EXISTS raw_tournaments_leaderboard")

    con.sql("SELECT 'DuckDB is working!' AS message").show()
