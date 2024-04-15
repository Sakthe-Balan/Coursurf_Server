import csv
import mysql.connector

# MySQL database configuration
db_config = {
    'host': 'coursurfdatabase.cf4isu2imje6.us-east-1.rds.amazonaws.com',
    'user': 'coursurf',
    'password': 'coursurf',
    'database': 'CoursurfDB'
}

# CSV file path
csv_file_path = 'Course_Info(Final)1.csv'

def load_csv_to_mysql(csv_file, db_config):
    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Read CSV data from file
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Get the column names from the CSV file
            columns = reader.fieldnames
            
            # Construct SQL query to create table
            create_table_query = f"CREATE TABLE IF NOT EXISTS Udemy ("
            for col in columns:
                create_table_query += f"{col} VARCHAR(255), "  # Assuming all columns are VARCHAR(255)
            create_table_query = create_table_query[:-2]  # Remove the trailing comma and space
            create_table_query += ");"
            
            # Execute table creation query
            cursor.execute(create_table_query)

            # Insert data into the table
            for row in reader:
                # Construct and execute INSERT statement
                placeholders = ', '.join(['%s'] * len(row))
                print(placeholders)
                sql = f"INSERT INTO Udemy ({', '.join(row.keys())}) VALUES ({placeholders})"
                cursor.execute(sql, list(row.values()))
                print(list(row.values()))
        # Commit the transaction
        conn.commit()
        print("Data loaded successfully.")

    except mysql.connector.Error as error:
        print("MySQL error:", error)
        conn.rollback()
    except Exception as error:
        print("General error:", error)
        conn.rollback()

    finally:
        # Close communication with the MySQL database
        cursor.close()
        conn.close()

if __name__ == "__main__":
    load_csv_to_mysql(csv_file_path, db_config)
