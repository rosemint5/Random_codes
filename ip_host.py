
x1 = "192.168.1.22"
x = x1.split(".")
y = "24"
dec = []


def stringToInt(m):         #zwraca ip bez zer na początku, bo zmienia na integer
    lt = []
    for i in m:
       z = int(i)
       lt.append(z)
    return lt

def decimalToBinary(n):
    b = []
    n = stringToInt(n)
    for i in n:
        x2 = bin(i).replace("0b","")
        str(x2)
        if len(x2)<8:
            for i in range(8-len(x2)):
                x2 = "0" + x2
            b.append(x2)
        else:
            b.append(x2)
    return b

def binaryToDecimal(d):
    if d == list:
        for i in d:
            dec = (int(i,2))
    else:
        d = str(d)
        dec = int(d,2)
    return dec

def maska(k):
    y1 = int(k)
    j = y1//8
    g = y1%8
    h = (32-y1)//8
    ltj = []
    st = ""
    for i in range(j):
        for i1 in range(8):
            st = st + "1"
        ltj.append(st)
        st = ""
    for i2 in range(g):
        st = st + "1"
    for i3 in range(8-g):
        st = st + "0"
    ltj.append(st)
    st = ""
    for i4 in range(h):
        for i5 in range(8):
            st = st + "0"
        ltj.append(st)
        st = ""

    return ltj


def NOT(a):
    ltj = maska(y)
    ltn = []
    p = ""
    for i in ltj:
        z = str(i)
        for j in z:
            if j== "1":
                p = p + "0"
            else:
                p = p + "1"
        ltn.append(p)
        p = ""
    return ltn

def ads():
    ltb = []
    lta = []
    st = ""
    b = decimalToBinary(x)
    m = maska(y)
    for i in range(4):
        b1 = b[i]
        m1 = m[i]
        for j in range(8):
            b2 = b1[j]
            m2 = m1[j]
            if b2 == "1" and m2 == "1":
                st = st + "1"
            else:
                st = st + "0"
        ltb.append(str(st))
        st = ""
    for i in ltb:
        e = binaryToDecimal(i)
        lta.append(e)
    
    return lta

def adroz():
    ltrn=[]
    ltrd=[]
    ltro=[]
    n = NOT(maska(y))
    ad = ads()
    for i in n:
        x = binaryToDecimal(str(i))
        ltrn.append(x)
    for j in ad:
        ltrd.append(j)
    for i in range(4):
        ltro.append(ltrn[i]+ltrd[i])
    return ltro

def host(h):
    h = int(h)
    ho = 2**(32-h)-2
    return ho


print("ip ", stringToInt(x))
print("bin2 ", decimalToBinary(x))
print("maska ", maska(y))

print("NOT ", NOT(maska(y)))
print("adres sieci: ", ads())
print("adres rozgłoszeniowy: ", adroz())
print("liczba hostów: ", host(y))