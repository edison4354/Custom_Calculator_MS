from datetime import date, datetime
# Algorithm:
# 1. Data Needed: User birthday, Unit of time, Current Date
# 2. Ask for the data needed through inputs
# 2.1 collect all the second elements of the student sub-lists to a# new list
# 3. Return the sorted new list
def user_input():
    """Returns the user input of their birthday as a string into integers"""
    birthday = input("What is your birthday (Please format it by mm/dd/yyyy): ")
    year = int(birthday.strip().split("/")[2])
    day = int(birthday.strip().split("/")[1])
    month = int(birthday.strip().split("/")[0])
    return year, month, day

def current_date():
    """Convert the the current date from a string to a list of integers"""
    unformat_date = datetime.today().strftime('%Y-%m-%d')
    current_date = unformat_date.split('-')
    year = int(current_date[0])
    month = int(current_date[1])
    day = int(current_date[2])
    return year, month, day

def find_length_of_live():
    live_unit = input("Do you want to know how many seconds, mintues, hours, or days you lived: ")
    b_year, b_month, b_day = user_input()
    year, month, day = current_date()
    difference = date(year, month, day) - date(b_year, b_month, b_day)
    days_live = difference.days
    if live_unit == 'seconds':
        print(days_live * 86400)
    elif live_unit == 'mintues':
        print(days_live * 1440)
    elif live_unit == 'hours':
        print(live_unit * 24)
    elif live_unit == 'days':
        print(days_live)
    else:
        live_unit = input("Do you want to know how many seconds, mintues, hours, or days you lived: ")


def main():
    find_length_of_live()

if __name__ == "__main__":
    main()

