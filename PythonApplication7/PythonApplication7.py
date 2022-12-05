from math import*
print("*** Mangud numbridega ***")
print()

while 1:
    try:
        a=(abs(int(input("Sisestage=> ")))) #Panen juurde 2 umarsulgusid
        break
    except ValueError:
        print("See ei ole taisarv")

if a==0:
    print("Pole mote tootada selle nulliga")
else:
    print("Kui palju numbris paaritu ja paaris arved")
    print()
    c=b=a #Eemaldasin 2 vordusmarkisid
    paaris=0 #Eemaldasin  vordusmargi
    paaritu=0 #Eemaldasin  vordusmargi
    while b > 0: #Panen kooloni punkti ja koma asemel
        if b % 2==0: #Panen vordusmargi sisse
            paaris+=1 #Vahetasin margi vahele
        else:
            paaritu+=1 #Vahetasin margi vahele
        b //= 10 #Liigutasin pariteet vasakule 
    print("Paaris arved:",paaris)
    print("Paaritu arved:",paaritu)
    print()
    print("Keerame umber sisestatud arv")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #Vahetasin margi vahele
    print("umberkeeratud arv", b)
    print()
    print("Kontrollime hupotees") #Eemaldasin uks umarsulu vasakult poolt
    print()
    if c % 2 == 0: #Panin vordusmargi juurde
      print("c - paaris arv. Jagame 2-ks.")
    else:
      print("c - paaritu arv. Korrutame 3-ks, paneme juurde 1 ja jagame 2-ks.")
    while c != 1: #Panen kooloni punkti ja koma asemel
        if c % 2 == 0:
            c = c / 2
        else:
            c = (3*c + 1) / 2
        print(int(c), end=" ")
    print()
    print("Hupotees on oige")

    #for j in range(9):
#    for i in range(9):
#        if j==i:
#            print(j+1, end=" ")
#        else:
#            print(0,end=" ")
#    print()

#for r in range(1,11):
#    for c in range(1,11):
#        print(str(r*c).center(4), end="")
#    print()

#r=0
#c=0
#while r<11:
#    r+=1
#    while c<11:
#        c+=1
#        print(str(r*c).center(4), end="")
#    c=0
#    print()
