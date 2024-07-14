"""
basic:

def main():
    time = input("What time is it? ").strip()
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute) / 60

if __name__ == "__main__":
    main()

"""
# challenge:
def main():
    time = input("What time is it? ").strip()
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.replace("a.m.", "").replace("p.m.", "").split(":")
    hour = int(hour)
    minute = int(minute)
    if "p.m." in time and hour != 12:
        hour += 12
    if "a.m." in time and hour == 12:
        hour = 0
    return hour + minute / 60

if __name__ == "__main__":
    main()
