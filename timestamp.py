from datetime import datetime
import time
#temp = datetime.datetime.fromtimestamp(1500055157546).strftime('%Y-%m-%d %H:%M:%S')

print(
    datetime.fromtimestamp(1500056682.729).strftime('%Y-%m-%d %H:%M:%S.%f')
)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1500058260)))

ms=1500056682729
temp = datetime.fromtimestamp(ms/1000.0)

print(temp)