import time

class Timer():
    def __init__(self, timer_minutes):
        self.timer_minutes = timer_minutes
    
    def countdown(self):
        time_seconds = self.timer_minutes * 60

        while time_seconds > 0:
            minutes = time_seconds // 60
            seconds = time_seconds % 60

            timer_display = f"{minutes:02d}:{seconds:02d}"

            print(timer_display, end='\r')
            
            time.sleep(1)
            time_seconds -= 1
            
        print("Time's up!")

