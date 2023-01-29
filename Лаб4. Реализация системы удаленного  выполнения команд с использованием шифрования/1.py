from psutil import process_iter
from json import dumps

pids = {}
for proces in process_iter(['name', 'status', 'username']):
    pids[proces.pid] = proces.info

print(dumps(pids))
