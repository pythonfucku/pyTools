#!/bin/env python

def main(s):
    output = ""
    N = "\n"
    T = "    "
    i = 0 
    j =0
    count = len(s)

    for i in range(count):
        if s[i] == '{' or s[i] == '[':
            j += 1
            output += s[i] + N + T*j
        elif s[i] =='}' or s[i] == ']':
            j -= 1
            if i+1<count and s[i+1] == ',' and i+2<count and s[i+2] == '[':
                output += N + T*j+s[i]
            elif i+1<count and s[i+1] == ',':
                output += N + T*j +s[i]
            else:
                output += N + T*j+s[i] + N 
        elif s[i] == ',':
            if s[i-1] == ']' and i+1<count and s[i+1] =='[':
                output += s[i] + N + T*j
            elif s[i-1] == '}' and i+1<count and s[i+1] =='{':
                output += s[i] + N + T*j
            else:
                output += s[i]  + N + T*j
        elif s[i] == '\\':
            continue
        else:
            output += s[i]
    return output

print main(s)
