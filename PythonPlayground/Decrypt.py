#!/usr/bin/python
import math

#  int to text 
def int_array_to_text(arr):
    txt = ''
    for i in range(0,len(arr)):
        txt += (chr(arr[i] + 97))
    return txt

# String to array implementation
def string_to_int_array(text):
    tmp = []
    for i in text:
        charcode = ord(i)
        part_a = math.floor(charcode/26)
        part_b = charcode % 26
        tmp.append(part_a)
        tmp.append(part_b)
    return tmp


# array_to_string
def array_to_string(arr):
    txt = ''
    length = int(len(arr))
    for i in range(0,length,2):
        txt += (chr(arr[i]*26+arr[i+1]))
    return txt


# text to array
def text_to_array(txt):
    tmp = []
    for i in txt:
        tmp.append(ord(i) - 97)
    return(tmp)

print(array_to_string(text_to_array(array_to_string(text_to_array('dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu')))))
