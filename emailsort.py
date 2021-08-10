import re
import pyperclip

emailRegax = re.compile(r'''
([a-zA-Z0-9_.+-]+ #user-name
@[a-zA-Z0-9-]+ #domain-name
\.[a-zA-Z0-9-.]+  # dot-something
)
''',re.VERBOSE)

phoneNumRegex = re.compile(r'''
(\d{3}|\(\d{3}\))? #area code
(\s|-)? #seperator
(\d{3}) #middile number
(\s|-) #seperator
(\d{4}) #last number
''',re.VERBOSE)

mobileNumRegax = re.compile(r'''
(\d{2}|\(\d{2}\)|\+\d{2})*
(\s|-)*
(\d{10})
''',re.VERBOSE)


text = str(pyperclip.paste())
match = []
for item in phoneNumRegex.findall(text):
    phoneNum = '-'.join([item[0],item[2],item[4]])
    match.append(phoneNum)

for item in mobileNumRegax.findall(text):
    print(item)
    phoneNum = '-'.join([item[0],item[2]])
    match.append(phoneNum)

for item in emailRegax.findall(text):
    print(item)
    match.append(item)
print(match)


if len(match)>0:
    pyperclip.copy('\n'.join(match))
else:
    print("No Phone Number or Email Traced")
