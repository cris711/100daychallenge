import platform
import sys

print("""Python version: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
    sys.version.split('\n'),
    platform.system(),
    platform.machine(),
    platform.platform(),
    platform.uname(),
    platform.version(),
    platform.mac_ver(),
))
