from datetime import datetime, timedelta

now =datetime.now()
print(now)

# formatting
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

future= now+timedelta(days=5)
past=now-timedelta(days=10)
print("5 days later:",future.strftime("%Y-%M-%d"))
print("10 days ago:",past.strftime("%Y-%M-%d"))