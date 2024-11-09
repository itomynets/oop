from datetime import datetime

name = "Ігор"
location = "Париж"
activity = "Відпочиває"

print(f"{name} зараз {activity}  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. {location} красиве місто!")
