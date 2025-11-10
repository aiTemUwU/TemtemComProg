courseDict, profDict = {}, {}
courseFile, profFile, dbFile = [input().strip() for i in range(0, 3)]
dbCourse, dbProf = [], []
output = []

courseFileText = open(courseFile, "r")
profFileText = open(profFile, "r")
dbFileText = open(dbFile, "r")

for line in courseFileText:
    key, val = line.strip().split(", ")
    courseDict.update({key:val})

for line in profFileText:
    key, val = line.strip().split(", ")
    profDict.update({key:val})

for line in dbFileText:
    course, prof = line.strip().split(", ")
    dbCourse.append(course)
    dbProf.append(prof)

courseFileText.close()
profFileText.close()
dbFileText.close()

for i in range(0, len(dbCourse)):
    courseCode = dbCourse[i]
    profCode = dbProf[i]

    if courseCode in courseDict.keys() and profCode in profDict.keys():
        output.append(f"{courseDict.get(courseCode)}, {profDict.get(profCode)}")
    else: output.append(f"record error")

for e in output: print(e)
