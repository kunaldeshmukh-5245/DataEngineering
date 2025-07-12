# write main block for the salary insights project

from utils.file_utils import read_csv, write_summary
from utils.analysis import (
    get_most_common_names, 
    get_dept_salary_groups, 
    get_high_earners, bucket_salaries, 
    calculate_service_years
)
from utils.decorators import log_function_call


@log_function_call
def main():  
    # Read the CSV file
    data = read_csv("data/employees.csv")
    if not data:
        print("No data to analyze.")
        return
    summay_lines = []
    top_names = get_most_common_names(data)
    summay_lines.append("Most Common Names:\n")
    summay_lines.extend([f"{name}: {count}" for name, count in top_names])
    summay_lines.append("\n")

    avg_salaries = get_dept_salary_groups(data)
    summay_lines.append("Average Salaries by Department:\n")
    summay_lines.extend([f"{dept}: {avg_salary}" for dept, avg_salary in avg_salaries.items()])
    summay_lines.append("\n")

    high_earners = get_high_earners(data,threshold=100000)
    summay_lines.append("High Earners (Salary > 100000):\n")
    if high_earners:
        summay_lines.extend([f"{row['name']}: {row['salary']}" for row in high_earners])
    else:
        summay_lines.append("No high earners found.\n")
    summay_lines.append("\n")

    updated_data = bucket_salaries(data)
    count = {
        "Executive": 0,
        "Manager": 0,
        "Staff": 0
    }
    for row in updated_data:
        count[row['salary_level']] += 1
    summay_lines.append("Salary Levels:\n")
    summay_lines.extend([f"{level}: {count}" for level, count in count.items()])
    summay_lines.append("\n")

    service_years = calculate_service_years(data)
    summay_lines.append("Employee service lines:\n")
    summay_lines.extend([f"{name}: {years} years" for name, years in service_years.items()])
    summay_lines.append("\n")

    # Write the summary to a text file
    write_summary(summay_lines, "summary.txt")



if __name__ == "__main__":
    main()