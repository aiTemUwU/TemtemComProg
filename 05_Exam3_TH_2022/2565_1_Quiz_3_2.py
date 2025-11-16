N, M, K = [int(e) for e in input().split()]
bachNameToFaculty = {}
guestToFacultySetDict = {}

for i in range(N):
    bachName, faculty = input().split()
    bachNameToFaculty.update({bachName:faculty})

for i in range(M):
    data = input().split()
    guestName = data[0]
    
    tempBachNameTuple = tuple([])
    for visitedBachName in data[1::]:
        tempBachNameTuple += tuple([bachNameToFaculty.get(visitedBachName)])
    
    guestToFacultySetDict.update({guestName:set(tempBachNameTuple)})

for i in range(K):
    guestName = input().split()
    
    guestVisitingFacultySet = set(guestToFacultySetDict.get(guestName[0]))
    for eachGuest in guestName[1::]:
        guestVisitingFacultySet = guestVisitingFacultySet.intersection(set(guestToFacultySetDict.get(eachGuest)))

    if len(guestVisitingFacultySet) != 0:
        guestVisitingFacultyList = list(guestVisitingFacultySet)
        guestVisitingFacultyList = sorted(guestVisitingFacultyList)
        print(("".join(f"{e} " for e in guestVisitingFacultyList)).strip())
    else: print("None")
    

"""
8 3 2
Luffy faculty_a
Nami faculty_a
Sanji faculty_b
Zoro faculty_c
Robin faculty_c
Chopper faculty_a
Brook faculty_c
Franky faculty_b
Eren Nami Chopper Brook
Anya Sanji Luffy
Yaiba Franky
Eren Anya
Anya Eren Yaiba

8 2 1
Luffy faculty_a
Nami faculty_a
Sanji faculty_b
Zoro fac_c
Robin fac_c
Chopper faculty_a
Brook fac_c
Franky faculty_b
Shinji Sanji Chopper
Amuro Zoro Sanji Nami
Amuro Shiji
"""