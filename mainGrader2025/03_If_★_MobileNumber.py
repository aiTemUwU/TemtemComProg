tel = input().strip()

if len(tel) == 10:
    if tel[0:2] in ["06", "08", "09"]:
        print("Mobile number")
    else:
        print("Not a mobile number")
else: print("Not a mobile number")