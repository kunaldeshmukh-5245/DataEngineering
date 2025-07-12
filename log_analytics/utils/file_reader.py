import json
import os

def read_json_logs(file_path):
    """
    Reads line-delimited JSON logs from a file and returns a list of dictionaries.
    each line in the file should be a valid JSON object.
    """
    logs = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        for line in file:
            try:
                logs.append(json.loads(line.strip()))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from line: {line.strip()}. Error: {e}")
    return logs

def read_text_logs(file_path):
    """
    Reads a text log file and returns a list of lines.
    """
    logs = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        for line in file:
            parsed_line = line.strip()
            if parsed_line:  # Only add non-empty lines
                logs.append(parsed_line)
    return logs
