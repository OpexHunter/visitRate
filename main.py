import datetime

# ReadTime func
def rt(t):
    return datetime.datetime.strptime(t.replace('\n', ''), '%H:%M:%S')

# Read Rasp
f = open('Rasp.txt', 'r')
rasp = []
for i in f:
    rasp.append(list(map(str, i.split(' '))))
f.close()

# Read in/out Event
f = open('Posh.txt', 'r')
k = 0
Visit = []
for i in f:
    k += 1
    Visit.append(list(map(str, i.split(' '))))
f.close()

# Rasp in datetime
for i in range(14):
    try:
        if rasp[i] == '\n':
            rasp[i] = None
    except:
        pass
    try:
        rasp[i][0] = rt(rasp[i][0])
    except:
        pass
    try:
        rasp[i][1] = rt(rasp[i][1])
    except:
        pass

for i in range(k):
    Visit[i][0] = datetime.datetime.strptime(Visit[i][0], '%d.%m.%Y')
    try:
        Visit[i][3] = rt(Visit[i][3])
        Visit[i][2] = rt(Visit[i][2])
    except:
        Visit[i].append(Visit[i][2])
        Visit[i][2] = datetime.datetime(1900, 1, 1, 9, 0)
        Visit[i][3] = Visit[i][3] = rt(Visit[i][3])

def progul(Visit, yshol, nadapr, otpystili):
    paraSr = datetime.timedelta(hours=1, minutes=50)
    opozd = datetime.timedelta(minutes=30)
    poranshe = datetime.timedelta(minutes=20)
    atata1 = 0
    atata2 = 0
    while Visit > nadapr + opozd + paraSr * atata1:
        atata1 += 1
        if atata1 == 10:
            atata1 = 0
            break
    while yshol + paraSr * atata2 < otpystili - poranshe:
        atata2 += 1
        if atata2 == 10:
            atata2 = 0
            break
    return atata1 + atata2

def pup(k, Visit):
    D = datetime.timedelta(1)
    startdata = Visit[k-1][0]
    """Start in 01.09"""
    startdata2 = datetime.datetime.strptime('29.08.2022', '%d.%m.%Y')
    stopdata = Visit[0][0]
    Nedela = 0
    ParVsego = 0
    pk = 0
    probil = 0
    while True:
        for i in (0, 1, 2, 3, 7, 8, 9, 10, 11):
            data = i*D + startdata2 + 14*D*Nedela
            if data < startdata:
                continue
            if data > stopdata:
                return ParVsego - probil, probil, ParVsego, Nedela, i
            ParVsego += int(rasp[i][2].replace('\n', ''))
            for i1 in range(k):
                if data == Visit[i1][0]:
                    probil += int(rasp[i][2].replace('\n', '')) - progul(Visit[k - 1 - pk][2], Visit[k - 1 - pk][3], rasp[i][0], rasp[i][1])
                    if progul(Visit[k - 1 - pk][2], Visit[k - 1 - pk][3], rasp[i][0], rasp[i][1]) > 0:
                        print(progul(Visit[k - 1 - pk][2], Visit[k - 1 - pk][3], rasp[i][0], rasp[i][1]))
        Nedela += 1
v1, v2, v3, v4, v5 = pup(k, Visit)

# Results
print('Skipped: ' + str(v1) + '\n' + 'All: ' + str(v3) + '\n' +
      'SkipRate: ' + str(round(v1/v3*100, 2)) +
      '% | VisitRate: ' + str(round(100 - v1/v3*100, 2)) + '%')
