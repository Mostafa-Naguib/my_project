import datetime

while 1:
    try:
        date = input("Enter the date in the following format YYYY-MM-DD: ")
        date_format = "%Y-%m-%d"
        datetime.datetime.strptime(date, date_format)
        break
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")

print(date)
            