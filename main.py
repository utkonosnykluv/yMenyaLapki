print('v kakom mesyace vi rodilis')
mes = input()
a = ""
if int(mes) == 1:
    a = 'yanvar'
if int(mes) == 2:
    a = 'fevral'
if int(mes) == 3:
    a = 'mart'
if int(mes) == 4:
    a = 'aprel'
if int(mes) == 5:
    a = 'may'
if int(mes) == 6:
    a = 'iun'
if int(mes) == 7:
    a = 'iul'
if int(mes) == 8:
    a = 'avgust'
if int(mes) == 9:
    a = 'sentyabr'
if int(mes) == 10:
    a = 'oktabr'
if int(mes) == 11:
    a = 'noyabr'
if int(mes) == 12:
    a = 'dekabr'
print('vi rodiis v ' + a)
if int(mes) == 12 or int(mes) == 1 or int(mes) == 2:
    print('За окном падал белый снег')
elif int(mes) == 3 or int(mes) == 4 or int(mes) == 5:
    print('Птицы пели прекрасные песни')
elif int(mes) == 6 or int(mes) == 7 or int(mes) == 8:
    print('Солнце светило ярче чем когда-либо')
elif int(mes) == 9 or int(mes) == 10 or int(mes) == 11:
    print(' Урожай был невероятным.')
