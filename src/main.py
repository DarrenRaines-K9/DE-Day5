import csv
import psycopg2

# Get logger
def get_logger():
    pass


# Read CSV file
def process_csv():
    file_path = "data/sample.csv"
    mode = "r"
    with open(file_path, mode) as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)  # Skip header row

        for row in csv_reader:
            print(row)


# Connect to Postgres
def postgress_connection():
    try:
        conn = psycopg2.connect(
        host ="localhost",
        database ="mydatabase",
        user ="myuser",
        password ="mypassword"
        )
    except:
    # TODO: log error
    pass

# For basic Main setup
def main():
    process_csv()
    postgress_connection()  


if __name__ == "__main__":
    main
