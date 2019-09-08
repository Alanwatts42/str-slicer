import re

syslog = '/var/log/syslog'  # log to be searched
sys_errors = []
line_num = 0
pattern = re.compile("error", re.IGNORECASE)  # re search term: "error"
with open(syslog, 'rt') as logfile:
    for entry in logfile:
        line_num += 1
        if pattern.search(entry) is not None:
            sys_errors.append((line_num, entry.rstrip('\n')))
for error in sys_errors:
    print("Line " + str(error[0]) + ": " + error[1])
