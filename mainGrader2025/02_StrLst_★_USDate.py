monthsList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

date = input().split("/")
month = monthsList[int(date[1])-1]

print(f"{month} {date[0]}, {date[2]}")
