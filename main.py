import datetime
import time
from application.salary import calculate_salary
from application.db.people import get_employees

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
TimeCreation = time.strftime("%H:%M:%S")
print("Время сейчас: ", TimeCreation + "\nДата: " + DateCreation, "\n")
if __name__ == '__main__':
    calculate_salary()
    get_employees()
