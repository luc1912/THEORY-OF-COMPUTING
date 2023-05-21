import sys

def funkcija_epsilon(stanje,prijelazi):
   brojac=-1
   for i in range(len(prijelazi)):
          brojac=brojac+1
          lista=prijelazi[brojac]
          linija=lista[0]
          lista2=linija.split(",")
          stanje1=lista2[0].strip()  #procitano stanje iz prijelaza 
          znak1=lista2[1].strip()  #procitani znak iz prijelaza

          counter=-1
          for i in stanje:
              counter=counter+1
              if stanje[counter]==stanje1 and znak1=='$':
                  counter2=-1
                  for j in lista2:
                      counter2=counter2+1
                      if counter2!=0 and counter2!=1:
                          if lista2[counter2] not in stanje and lista2[counter2]!='#': 
                               stanje.append(lista2[counter2])
                               stanje=funkcija_epsilon(stanje,prijelazi)
   return stanje
                  

def funkcija(stanje,znak,prijelazi,izlaz):
     izlaz=izlaz+"|"
     brojac=-1
     trenutna_stanja=[]
     for i in range(len(prijelazi)):
          brojac=brojac+1
          lista=prijelazi[brojac]
          linija=lista[0]
          lista2=linija.split(",")
          stanje1=lista2[0].strip()  #procitano stanje iz prijelaza 
          znak1=lista2[1].strip()  #procitani znak iz prijelaza
         
          brojilo=-1
          for i in stanje:
            brojilo=brojilo+1
            if  stanje[brojilo]==stanje1 and (znak1==znak):
               
               #iteriraj kroz listu2, spremaj stanja od lista2[2] pa do kraja
               brojac2=-1
               for i in lista2:
                    zastavica=True
                    brojac2=brojac2+1
                    if brojac2!=0 and brojac2!=1:
                        if lista2[brojac2] in trenutna_stanja:
                            zastavica=False
                        if zastavica==True and lista2[brojac2]!='#':
                          trenutna_stanja.append(lista2[brojac2])
                          trenutna_stanja=funkcija_epsilon(trenutna_stanja,prijelazi)
     brojac3=-1
     y=len(trenutna_stanja)
     sorted(trenutna_stanja)
     trenutna_stanja.sort()
     for i in trenutna_stanja:
        brojac3=brojac3+1
        if brojac3 != y-1:
            izlaz=izlaz+trenutna_stanja[brojac3]+","
        else:
            izlaz=izlaz+trenutna_stanja[brojac3]
     if len(trenutna_stanja)==0:
          trenutna_stanja.append("#")
          izlaz=izlaz+"#"
     
     return trenutna_stanja,izlaz



#f = open("C:\\Users\\marij\\Downloads\\primjer33.txt", "r")
line=input()
ulazniniz=line.split("|")
ulazniniz[-1] = ulazniniz[-1].strip() #micem \n sa zadnjeg elementa

line=input()
stanja=line.split(",")
stanja[-1] = stanja[-1].strip()
line=input()
abeceda=line.split(",")
abeceda[-1] = abeceda[-1].strip()
line=input()
prihvatljiva_stanja=line.split(",")
prihvatljiva_stanja[-1]=prihvatljiva_stanja[-1].strip()
line=input()
pocetno_stanje=line
pocetno_stanje.strip()
#print("Ulazni niz: ",ulazniniz)
#print("Stanja: ",stanja)
#print("Abeceda:" ,abeceda)
#print("Prihvatljiva stanja: ",prihvatljiva_stanja)
#print("Pocetno stanje: ",pocetno_stanje)

prijelazi=[]
for line in sys.stdin:
     lista=[]
     line2=line.replace("->",",")
     lista.append(line2)
     lista[-1] = lista[-1].strip() 
     prijelazi.append(lista)



stanje=[]
stanje.append(pocetno_stanje)
stanje[-1] = stanje[-1].strip() 
brojilo=-1
for i in range(len(prijelazi)):
          brojilo=brojilo+1
          lista=prijelazi[brojilo]
          linija=lista[0]
          lista2=linija.split(",")
          stanje1=lista2[0].strip()  #procitano stanje iz prijelaza 
          znak1=lista2[1].strip()  #procitani znak iz prijelaza

       
          if stanje1==stanje[0] and znak1=='$':
              stanje=funkcija_epsilon(stanje,prijelazi)
        

brojilo2=-1     
izlaz=""
sorted(stanje)
stanje.sort()
for i in range(len(stanje)):
    brojilo2=brojilo2+1
    if brojilo2 != len(stanje)-1:
        izlaz=izlaz+stanje[brojilo2]+","
    else:
        izlaz=izlaz+stanje[brojilo2]

    

for i in range (len(ulazniniz)):   #svaki znak ulaznog niza ulazi u funkciju
     list=ulazniniz[i].split(',')
     for j in range(len(list)):
         stanje,izlaz=funkcija(stanje,list[j],prijelazi,izlaz)
     print(izlaz)
     izlaz=""
     stanje.clear()
     stanje.append(pocetno_stanje)
     stanje[-1] = stanje[-1].strip() 
     stanje=funkcija_epsilon(stanje,prijelazi)
     sorted(stanje)
     stanje.sort()
     for i in range(len(stanje)):
       if i != len(stanje)-1:
         izlaz=izlaz+stanje[brojilo2]+","
       else:
         izlaz=izlaz+stanje[brojilo2]





    
     


