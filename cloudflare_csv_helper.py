#!/usr/bin/env python3
import re
import subprocess
import datetime
import sys

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
CLOUDFLARE_CLI_PATH = "/usr/local/bin/speed-cloudflare-cli"
SEPERATOR = "\t"

start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
test = subprocess.check_output(CLOUDFLARE_CLI_PATH)
stop = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

full_result = ANSI_ESCAPE.sub('', test.decode())
result_tuples = full_result.split("\n")

if len(sys.argv) > 1 and sys.argv[1] == "header":
    split = 0
else:
    split = 1

out = [x.split(":")[split].strip() for x in result_tuples if x]

if split == 0:
    out.insert(0, "stop")
    out.insert(0, "start")
else:
    out.insert(0, stop)
    out.insert(0, start)

print(SEPERATOR.join(out))
