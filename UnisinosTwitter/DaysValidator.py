from datetime import datetime

class DaysValidator:
    def __init__(self, dayInfo):
        self.dayInfo = dayInfo
        self.isValid = self.validate()
    
    def validate(self):
        if (self.dayInfo.is_exactly):
            self.isValid = self.calculateDaysDifference() <= 5
        
        else:
            self.isValid = self.dayInfo.days_ahead <= 5
    
    def calculateDaysDifference(self):
        today = datetime.today().weekday()
        nextDay = self.dayInfo.days_ahead
        
        if (nextDay > today):
            return nextDay - today
        
        else:
            return nextDay + 7 - today