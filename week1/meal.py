def convert(time):
     hour, minute = time.split(":")
     hour = float(hour)
     minute = float(minute)
     return hour + minute / 60

def main():
        time = input("What time is it? ").strip()

        if convert(time) >= 7 and convert(time) <= 8:
            print("breakfast time")
        elif convert(time) >= 12 and convert(time) <= 13:
            print("lunch time")
        elif convert(time) >= 18 and convert(time) <= 19:
            print("dinner time")
        else:
            print("")

if __name__ == "__main__":
    main()
