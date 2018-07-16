import psutil

print(psutil.cpu_count(logical=False))

print(psutil.cpu_times())