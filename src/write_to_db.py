import duckdb as db

def write_to_db(data, table_name):
    """
    Write data to DuckDB database.

    Args:
        data (list of dict): The data to be written to the database.
        table_name (str): The name of the table to write the data to.
    """
    # Connect to DuckDB
    con = db.connect(database='warehouse.duckdb', read_only=False)

    # Create a temporary table in DuckDB
    con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM (SELECT * FROM data) LIMIT 0")

    # Insert data into the table
    con.execute(f"INSERT INTO {table_name} SELECT * FROM data")

    # Commit and close the connection
    con.commit()
    con.close()
