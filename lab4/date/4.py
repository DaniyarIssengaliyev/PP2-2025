import datetime

today = datetime.datetime.today()

another = datetime.datetime(2023, 1, 1)

diff = today - another
print(diff.total_seconds())