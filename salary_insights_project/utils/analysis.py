from collections import Counter,defaultdict
from datetime import datetime

def get_most_common_names(data):
    """
    Get the most common names from the data.
    Returns a list of tuples with the name and its count.
    """

    names = [row['name'] for row in data if 'name' in row]
    return Counter(names).most_common(3)

def get_dept_salary_groups(data):
    """
    Group salaries by department and return a dictionary with department names as keys
    and lists of salaries as values.
    """
    dept_salary_groups = defaultdict(list)
    for row in data:
        if 'department' in row and 'salary' in row:
            dept_salary_groups[row['department']].append(float(row['salary']))
    return {dept: sum(salaries)//len(salaries) for dept, salaries in dept_salary_groups.items() if salaries}

def get_high_earners(data, threshold=100000):
    """
    Get a list of high earners from the data.
    Returns a list of dictionaries for employees with salaries above the threshold.
    """
    return [row for row in data if 'salary' in row and float(row['salary'])> threshold]

def bucket_salaries(data):
    """
    Bucket salaries into ranges defined by the bucket size.
    Returns a dictionary with salary ranges as keys and counts as values.
    """
    for row in data:
        if 'salary' in row and 'name' in row:
            if int(row['salary']) >= 150000:
                row['salary_level'] = "Executive"
            elif int(row['salary']) >= 80000:
                row['salary_level'] = "Manager"
            else:
                row['salary_level'] = "Staff"
    return data

def calculate_service_years(data):
    """
    Get the number of years each employee has been with the company.
    Returns a dictionary with employee names as keys and years of service as values.
    """
    service_years = defaultdict(str)
    for row in data:
        if 'name' in row and 'joining_date' in row:
            start_year = int(row['joining_date'].split('-')[0])
            current_year = int(datetime.now().year)  # Assuming current year is 2023
            service_years[row['name']] = current_year - start_year
    return service_years

def get_salary_statistics(data):
    """
    Calculate basic salary statistics: average, median, and total salary.
    Returns a dictionary with the statistics.
    """
    salaries = [float(row['salary']) for row in data if 'salary' in row]
    if not salaries:
        return {'average': 0, 'median': 0, 'total': 0}
    
    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    median_salary = sorted(salaries)[len(salaries) // 2] if len(salaries) % 2 != 0 else \
        (sorted(salaries)[len(salaries) // 2 - 1] + sorted(salaries)[len(salaries) // 2]) / 2
    
    return {
        'average': average_salary,
        'median': median_salary,
        'total': total_salary
    }   