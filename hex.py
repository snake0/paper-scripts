#!/Users/snake0/PycharmProjects/analyzer/venv/bin/python3
import sys

print(str(hex(int(sys.argv[1])))[2:] +
      str(hex(int(sys.argv[2])))[2:] +
      str(hex(int(sys.argv[3])))[2:])

