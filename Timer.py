import time

def start_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time} seconds")
        time.sleep(1)
    print("Time's up!")

def main():
    print("Timer")
    time_input = int(input("Enter the time you want to set the timer for (in seconds): "))
    start_timer(time_input)

if __name__ == "__main__":
    main()