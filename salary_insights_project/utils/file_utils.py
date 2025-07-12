import csv

def read_csv(file_path):
    """
    Read a csv file and return its contents as a list of dictionaries.
    """
    try:
        with open(file_path, mode="r") as file:
            file_reader = csv.DictReader(file)
            data = [row for row in file_reader]
            if not data:
                raise ValueError("The CSV file is empty.")
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"Error: Could not read the file {file_path}. {e}")
        return []

def write_summary(data,file_path="summary.txt"):
    """
    Write a list of dictionaries to a text file.
    """
    try:
        with open(file_path,mode="w") as file:
            for row in data:
                file.write(str(row)+"\n")
        print(f"Summary written to {file_path}")
    except Exception as e:
        print(f"Error: Could not write to file {file_path}. {e}")