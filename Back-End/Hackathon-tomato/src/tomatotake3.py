def main():
    temperature_readings = [] # this is an empty list that will store the values that will be printed for the final output
    watering_counts = [] #final output, empty list that will be filled by this function
    counter = 0

    while True:
        temperature = get_temperature_reading()
        if temperature is None:
            break

        counter += 1
        watering_counts.append(counter)
        print("Watering count:", counter)

        input_str = ""
        while input_str.lower() not in ("y", "n"):
            input_str = input("Did you water the plant? (y/n): ")
        if input_str.lower() == "y":
            counter = 0

        temperature_readings.append(temperature)

        userInputStop = input("Would you like to stop taking care of the plant? (y/n): ")
        if userInputStop.lower() == "y":
            break

    print("Temperature readings:", temperature_readings)
    print("Watering counts:", watering_counts)
    print("  Temperature below 65: ", watering_counts.count(0))
    print("  Temperature within 65-85: ", watering_counts.count(1))
    print("  Temperature above 85: ", watering_counts.count(2))


def get_temperature_reading():
    while True:
        temperature = float(input("Enter temperature reading (F): "))
        if temperature < 50:
            print("The plant won't grow at this temperature.")
            return None
        elif temperature >= 50 and temperature < 65:
            print("Water the plant once, every other day. ")
        elif temperature >= 85 and temperature < 95:
            print("It's a hot day, water the plant twice.")
            return temperature
        elif temperature >= 65 and temperature <= 85:
            print("Temperature is within ideal range. Water the plant once in the morning, daily.")
            return temperature
        elif temperature >= 95:
            print("It's too hot, water the plant three times.")
            return temperature


if __name__ == "__main__":
    main()