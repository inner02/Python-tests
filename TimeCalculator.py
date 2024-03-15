def parse_time(time_str):
    days, hours, minutes = map(int, time_str.split(':'))
    return days, hours, minutes

def format_time(days, hours, minutes):
    return f"{days:02d}:{hours:02d}:{minutes:02d}"

def add_times(time1, time2):
    days1, hours1, minutes1 = parse_time(time1)
    days2, hours2, minutes2 = parse_time(time2)
    
    total_minutes = (days1 + days2) * 24 * 60 + (hours1 + hours2) * 60 + (minutes1 + minutes2)
    
    new_days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    new_hours = remaining_minutes // 60
    new_minutes = remaining_minutes % 60
    
    return format_time(new_days, new_hours, new_minutes)

def difference_between_times(time1, time2):
    days1, hours1, minutes1 = parse_time(time1)
    days2, hours2, minutes2 = parse_time(time2)
    
    total_minutes1 = days1 * 24 * 60 + hours1 * 60 + minutes1
    total_minutes2 = days2 * 24 * 60 + hours2 * 60 + minutes2
    
    difference = abs(total_minutes1 - total_minutes2)
    
    new_days = difference // (24 * 60)
    remaining_minutes = difference % (24 * 60)
    new_hours = remaining_minutes // 60
    new_minutes = remaining_minutes % 60
    
    return format_time(new_days, new_hours, new_minutes)

def convert_to_hours(time):
    days, hours, minutes = parse_time(time)
    total_hours = days * 24 + hours + minutes / 60
    return total_hours

def convert_to_minutes(time):
    days, hours, minutes = parse_time(time)
    total_minutes = days * 24 * 60 + hours * 60 + minutes
    return total_minutes

def convert_minutes_to_time(minutes):
    new_days = minutes // (24 * 60)
    remaining_minutes = minutes % (24 * 60)
    new_hours = remaining_minutes // 60
    new_minutes = remaining_minutes % 60
    return format_time(int(new_days), int(new_hours), int(new_minutes))

def convert_hours_to_time(hours):
    new_days = hours // 24
    remaining_hours = hours % 24
    return format_time(int(new_days), int(remaining_hours), 0)

def convert_days_to_time(days):
    return format_time(int(days), 0, 0)

def main():
    print("Time Calculator")
    print("1- Add 2 times")
    print("2- Find the difference between 2 times")
    print("3- Convert to Hours")
    print("4- Convert to Minutes")
    print("5- Convert Minutes to Time")
    print("6- Convert Hours to Time")
    print("7- Convert Days to Time")
    print("8- Exit")
    
    while True:
        option = input("Enter an option: ")
        
        if option == '1':
            time1 = input("Enter first time (DD:HH:MM): ")
            time2 = input("Enter second time (DD:HH:MM): ")
            print("Sum of times:", add_times(time1, time2))
        elif option == '2':
            time1 = input("Enter first time (DD:HH:MM): ")
            time2 = input("Enter second time (DD:HH:MM): ")
            print("Difference between times:", difference_between_times(time1, time2))
        elif option == '3':
            time = input("Enter time (DD:HH:MM): ")
            print("Converted to hours:", convert_to_hours(time))
        elif option == '4':
            time = input("Enter time (DD:HH:MM): ")
            print("Converted to minutes:", convert_to_minutes(time))
        elif option == '5':
            minutes = int(input("Enter minutes: "))
            print("Minutes converted to time:", convert_minutes_to_time(minutes))
        elif option == '6':
            hours = float(input("Enter hours: "))
            print("Hours converted to time:", convert_hours_to_time(hours))
        elif option == '7':
            days = float(input("Enter days: "))
            print("Days converted to time:", convert_days_to_time(days))
        elif option == '8':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")
main()
