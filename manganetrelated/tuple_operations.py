import time

seconds = int(input("Enter countdown seconds: "))

while seconds > 0:
    print("Time remaining:", seconds)
    time.sleep(1)
    seconds -= 1

print("🎉 Time's up!")