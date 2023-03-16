import datetime
import os
# Get the current date and time
now = datetime.datetime.now()

CWD = os.path.dirname(os.path.abspath(__file__))

# Format the date and time as a string
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Create the filename with the current datetime
filename = f"{timestamp}.txt"
test_path = os.path.join(CWD, filename)
# Open the file and write today's date to it
with open(test_path, "w") as f:
    f.write(now.strftime("%Y-%m-%d"))
