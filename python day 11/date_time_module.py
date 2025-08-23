import datetime
today = datetime.date.today()
print(today.strftime("%d-%m-%y"))

now = datetime.datetime.now()
print(now.strftime("%H-%M-%S"))


birthdate = datetime.date(2005, 4, 15)   
days_old = (today - birthdate).days
print(f"You are {days_old} days old!")