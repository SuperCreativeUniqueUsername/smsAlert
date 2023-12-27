import datetime

class hourObj:
    def __init__(self) -> None:
        self.hour = datetime.datetime.now().hour
    
    def reset_hour(self):
        self.hour = datetime.datetime.now().hour
    
    def increment(self):
        if self.hour >= 23:
            self.hour = 0
        else:
            self.hour += 1
        
    def __str__(self) -> str:
        if self.hour <= 12 and self.hour != 0:
            return str(self.hour) + " AM"
        elif self.hour == 0:
            return "12 PM"
        else:
            return str(self.hour- 12) + " PM"