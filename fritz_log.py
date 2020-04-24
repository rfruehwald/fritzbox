from fritzconnection import FritzConnection
import sys
import mariadb
from datetime import datetime


HOST = '192.168.2.1'
PW = 'Fr@010265'


CONFIG_DB = {
    'host': '192.168.2.222',
    'user': 'ralf',
    'password': 'Fr@010265',
    'port': 3307
}
DB_NAME = 'morannon'

#
# connect to db
#
fc = FritzConnection(address=HOST, password=PW)
logDict = fc.call_action('DeviceInfo1', 'GetInfo')
log_l = logDict['NewDeviceLog']
log = log_l.splitlines()


# for line in log:
#     log_datetime = datetime.strptime(line[0:17], '%d.%m.%y %H:%M:%S')
#     log_desc = line[18:]
#     # print(datetime.strftime(log_datetime, '%Y-%m-%d %H:%M:%S')
#     my_sql = "INSERT INTO events (date_time, event) VALUES (%d, %s)"
#     my_val = (log_datetime, log_desc)
#     my_cursor.execute(my_sql, my_val)

# my_db.commit()
# my_db.close()
