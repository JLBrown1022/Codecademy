from datetime import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file
    :param file_path: path to the file
    :return: the creation date of the file
    """
    return datetime.fromtimestamp(os.path.getctime(file_path))

# Creating a date using year, month, day
# Example birthday datetime(yyyy.MM.DD, HH, MM, SS)
birthday = datetime(1960, 10, 22)
birthday.year, birthday.month, birthday.day,
birthday.weekday() # Monday is 0 and Sunday is 6
birthday.date() # datetime.date(1960, 10, 22)

# Creating a date using datetime.now()
datetime.now()
datetime.now() - datetime(1960, 10, 22) # timedelta object
datetime.now() - birthday # timedelta object
datetime(2025, 1, 8) - datetime(1960, 10, 22) # timedelta object

# Parsing a date using strptime()
parsed_date = datetime.strptime('Oct 22, 1960', '%b %d, %Y')
parsed_date.year, parsed_date.month, parsed_date.day

# Creating a date using strftime()
date_string = '2025-01-08'
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
date_string















