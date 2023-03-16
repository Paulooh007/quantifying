import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Create the filename with the current datetime
filename = f"{timestamp}.txt"

# Open the file and write today's date to it
with open(filename, "w") as f:
    f.write(now.strftime("%Y-%m-%d"))
