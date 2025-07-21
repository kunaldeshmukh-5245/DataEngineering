import logging

logging.basicConfig(
        filename = "/Users/kunaldeshmukh/Documents/dataEngineer/DataEngineringPractitice/DataEngineering/dataWrangling/logging/logfile.log",
        level = logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )

def read_file_and_write_lines(input_file,output_file):
    logging.info("Starting to read file and write lines.")
    with open(input_file,"r") as read_obj, open(output_file, "w") as write_obj:
        for line in read_obj:
            logging.info("Processing line: %s", line.strip())
            if 'WARNING' in line or 'ERROR' in line:
                print(line.strip())
                logging.info("Writing line to output file: %s", line.strip())
                write_obj.write(line.strip() + "\n")
    logging.info("Finished processing file.")

def extract_date_with_type(innput_file, output_file):
    logging.info("Starting to extract date with type from file.")
    with open(innput_file,"r") as read_obj,open(output_file, "w") as write_obj:
        for line in read_obj:
            if 'ERROR' in line or 'WARNING' in line:
                logging.info("Processing line for date extraction: %s", line.strip())
                print(line.strip())
                split_part = line.split(" ")
                newLine = " ".join([split_part[0],split_part[1],split_part[2].upper()])
                print(newLine.strip())
                logging.info("Writing extracted date to output file: %s", newLine.strip())
                write_obj.write(newLine + "\n")
    logging.info("Finished extracting date with type from file.")

if __name__ == "__main__":
    logging.info("Script started.")
    read_filename = "/Users/kunaldeshmukh/Documents/dataEngineer/DataEngineringPractitice/DataEngineering/dataWrangling/files/sample_log.txt"
    write_filename = "/Users/kunaldeshmukh/Documents/dataEngineer/DataEngineringPractitice/DataEngineering/dataWrangling/files/output.txt"
    result = read_file_and_write_lines(read_filename,write_filename)
    logging.info("File reading and writing completed.")
    extract_filename = "/Users/kunaldeshmukh/Documents/dataEngineer/DataEngineringPractitice/DataEngineering/dataWrangling/files/sample_log.txt"
    extract_output_filename = "/Users/kunaldeshmukh/Documents/dataEngineer/DataEngineringPractitice/DataEngineering/dataWrangling/files/extract_output.txt"
    extract_result = extract_date_with_type(extract_filename, extract_output_filename)
    logging.info("Date extraction completed.")
    print("Processing completed.")
