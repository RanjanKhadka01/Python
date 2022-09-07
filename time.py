import time

# print(time.ctime(0))
# seconds = time.time()
# print("Seconds since epoch = ", seconds)

# time_object = time.localtime()  # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

result = time.localtime()
print("result:", result)
print("\nyear:",result.tm_year)
print("\ntm_hour:", result.tm_hour)

