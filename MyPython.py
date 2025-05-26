import sys
from datetime import datetime

def calculate_age(dob):
    today = datetime.today()
    dob = datetime.strptime(dob, '%Y-%m-%d')
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

if __name__ == "__main__":
    dob = sys.argv[1]
    print(f"Age: {calculate_age(dob)}")
