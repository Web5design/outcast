import hashlib
import sys


def double_hash(plain):
    first = hashlib.sha1()
    first.update(plain)

    second = hashlib.sha1()
    second.update(first.digest())

    return second.hexdigest()

if len(sys.argv) != 3:
    print "mysql_double_sha1.py hash pass_file"
    sys.exit(1)

for line in open(sys.argv[2], 'r'):
    if line == '':
        pass
    if line.startswith('#'):
        pass
    line = line.strip()
    hash = sys.argv[1]

    if double_hash(line).upper() == hash.upper():
        print '{0}:{1}'.format(hash, line)
