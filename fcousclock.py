import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = seconds - elapsed_time

        if remaining_time <= 0:
            print("Time's up!")
            break

        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(f"Time remaining : {timer}\r", end='', flush=True)
        time.sleep(1)

focus_timer(25) # 25分钟专注时钟
