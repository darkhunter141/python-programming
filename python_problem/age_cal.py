import datetime
def print_age():
    year = input('Enter your age (YYYY/MM/DD): ')
    day = input('Enter your desired date (yyyy/mm/dd): ')
    try:
        year = [int(i) for i in year.split('/')]
        birth_data = datetime.date(year[0], year[1], year[2])

        #today = datetime.date.today()
        day = [int(i) for i in day.split('/')]
        dday = datetime.date(day[0], day[1], day[2])

        time_diff = dday - birth_data

        print('Your age is: {} year and  days'. format(
            time_diff.days))
    except (ValueError, KeyError):
        # Do your error management here
        print('Please use the format YYYY/MM/DD')

print_age()