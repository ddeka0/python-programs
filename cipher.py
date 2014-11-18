#!/usr/bin/python

plainText = raw_input("Enter a word lower case: ")
distance = input("value: ")
code = ""
for ch in plainText:
  ordValue = ord(ch)
  cipherValue = ordValue + distance
  if cipherValue > ord('z'):
    cipherValue = cipherValue - ord('z') + ord('a')-1
  code += chr(cipherValue)
print code

