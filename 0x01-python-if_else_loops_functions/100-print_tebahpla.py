#!/usr/bin/python3
for i in range (122, 64, -1):
  if 123 > i > 96:
    if i % 2 != 0:
      print(chr(i-32), end="")
    elif i % 2 == 0:
      print(chr(i), end="")
