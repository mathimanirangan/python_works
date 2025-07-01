import re


pattern=re.compile(r"[a-zA-Z0-9$#%@]{8,}[0-9]$")

while True:
    pwd = input('enter an password:')
    if pattern.fullmatch(pwd):
         print("Password accepted, thank you")
         break
    else:
        print("Password must be 8 length and can have only these special characters %, #, @, $")
