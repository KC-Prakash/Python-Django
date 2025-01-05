from datetime import datetime, timedelta
import time
import os
from plyer import notification



# new_year = datetime(datetime.now().year + 1, 1, 1)
new_year = datetime.now() + timedelta(seconds=5)

while datetime.now() < new_year:
    remaining_time = new_year - datetime.now()

    print(f"New year in {remaining_time.days} days | {remaining_time.seconds//60} minutes | {remaining_time.seconds%60} seconds")

    time.sleep(1)
    os.system("cls")


#notification window
# Create a notification
notification_title = "Happy New Year !!!"
notification_message = "May this year be filled with love, happiness, and success for you and your loved ones."

notification.notify(
    title=notification_title,
    message=notification_message,
    app_name='New Year',
    timeout=10  # Duration in seconds for which the notification will be visible
)