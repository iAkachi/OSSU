def main():
    # Prompt user for current and departure times
    current_time = input("What is the current time (in 24-hour format, e.g., 14:30)? ").strip()
    departure_time = input("What is the departure time (in 24-hour format, e.g., 18:45)? ").strip()
    
    try:
        # Convert both times to floats
        current_floated = convert_to_float(current_time)
        departure_floated = convert_to_float(departure_time)

        # Calculate time to leave and print result
        print(time_to_leave(current_floated, departure_floated))
    except ValueError:
        print("Invalid time format. Please enter time as HH:MM (e.g., 14:30).")

    
def convert_to_float(time):
    """Converts a time string (HH:MM) to float hours."""
    hours, minutes = map(int, time.split(":"))
    if not (0 <= hours < 24) or not (0 <= minutes < 60):
        raise ValueError("Invalid time provided")
    return hours + minutes / 60

def time_to_leave(current_float, leave_float):
    """Calculates the time difference between current time and departure time."""
    
    if current_float == leave_float:
        return "0 hours and 0 minutes left until departure."
    
    # Handle departure next day scenario
    if current_float > leave_float:
        leave_float += 24
    
    time_diff = leave_float - current_float
    
    # Convert time difference to hours and minutes
    hours = int(time_diff)
    minutes = int((time_diff - hours) * 60)
    
    return f"{hours} hours and {minutes} minutes left until departure."

main()
