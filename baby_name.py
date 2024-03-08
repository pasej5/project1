import sys
from datetime import datetime

def baby_name(birthdate):
    # Convert birthdate string to datetime object
    birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
    
    # Define date range
    after_date = datetime(2022, 2, 20)
    
    # Check birthdate against date range
    if birthdate >= after_date:
        return "Congradulations, The baby's name should start with ALX eg Alexa"
    else:
        return "You can choose any other beautiful name"

# Get the birthdate from command-line arguments
if len(sys.argv) != 2:
    print("Usage: python baby_name.py <birthdate>")
    sys.exit(1)

birthdate = sys.argv[1]
print(baby_name(birthdate))

