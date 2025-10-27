import csv
import psycopg2


# Get logger
def get_logger():
    pass


# Read CSV file
def process_csv():
    file_path = "data/sample.csv"
    mode = "r"

    conn = postgres_connection()
    cursor = conn.cursor()
    with open(file_path, mode) as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)  # Skip header row

        for row in csv_reader:
            print(row)

    cursor.close()
    conn.close()


# Connect to Postgres
def postgres_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword",
    )
    return conn


# For basic Main setup
def main():
    process_csv()


if __name__ == "__main__":
    main
