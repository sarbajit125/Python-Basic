import re


def Encoding(string1):
    list1 = []
    for i in string1:
        if i == " " or i == ',' or i == '.':
            list1.append(i)
        else:
            j = chr(ord(i) + 5)
            list1.append(j)
    for i in list1:
        print(i, end='')
    print()


def Decoding(string2):
    list2 = []
    for i in string2:
        if i == " " or i == ',' or i == '.':
            list2.append(i)
        else:
            j = chr(ord(i) - 5);
            list2.append(j)
    for i in list2:
        print(i, end='')


def has_num(string):
    return bool(re.search(r"\d|/|\^|\?|\*", string))


# Driver Code
string1 = input("Enter string 1\n");
string2 = input("Enter string 2\n");
if has_num(string1):
    print("INVALID INPUT")
elif has_num(string2):
    print("INVALID INPUT")
else:
    Encoding(string1)
    Decoding(string2)
