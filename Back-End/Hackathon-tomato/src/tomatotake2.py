def get_temperature_reading():
    while True:
        temperature = float(input("Enter temperature reading (F): "))
        if temperature < 50:
            print("The plant won't grow at this temperature.")
            return None
        elif temperature >= 50 and temperature < 65:
            print("The plant will grow, but is not in the ideal temperature. Water the plant once, every other day.")
            diff = 65 - temperature
            print("Increase temperature by", diff, "degrees to reach the ideal range.")
        elif temperature >= 85 and temperature < 95:
            print("It's a hot day, water the plant twice.")
            diff = temperature - 85
            print("Decrease temperature by", diff, "degrees to reach the ideal range.")
            return temperature
        elif temperature >= 65 and temperature <= 85:
            print("Temperature is within ideal range. Water the plant once in the morning, daily.")
            return temperature
        elif temperature >= 95:
            print("It's too hot, water the plant three times.")
            diff = temperature - 85
            print("Decrease temperature by", diff, "degrees to reach the ideal range.")
            return temperature


def main():
    temperature_readings = []
    watering_count = []
    counter = 0

    while True:
        temperature = get_temperature_reading()
        if temperature is None:
            break

        counter += 1
        watering_count.append(counter)
        print("Watering count:", counter)

        input_str = ""
        while input_str.lower() not in ("y", "n"):
            input_str = input("Did you water the plant? (y/n): ")
        if input_str.lower() == "y":
            counter = 0

        temperature_readings.append(temperature)

    print("Temperature readings:", temperature_readings)
    print("Watering count:", watering_count)


if __name__ == "__main__":
    main()

