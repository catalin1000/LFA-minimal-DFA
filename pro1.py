# l1=['nuci','mere','pere','piersici','albine','a','struguri']
# def sortare0(l1):
#     return sorted(l1,key=lambda x:(len(x),x[0]))
# def sortare(l1):
#     return sorted(l1,key=len)
# def sortare2(l1):
#     a=1
#     j=0
#     l3=[]
#     for i in range (len(l1)):
#         if a!=len(l1[i]):
#             print(str(sorted(l1[j:i],key=str)),end=' ')
#             l3.extend(sorted(l1[j:i],key=str))
#             a=len(l1[i])
#             j=i
#     print(l1[j:len(l1)])
#     l3.extend(l1[j:len(l1)])
#     return l3
# print(sortare0(l1))
# l2=sortare(l1)
# print(l2)
# l4=(sortare2(l2))
# print(l4)
# tuplu=[('a',1),('b',10)]
# tuplu=dict(tuplu)
# print(tuplu)


def afisare(part):
    for parts in part:
        print(*list(parts.keys()))
        for stare in parts:
            for stari in parts[stare]:
                print(stari,'->',parts[stare][stari][0])

def partitionare(lista_multimi): # impart multimile in alte multimi separabile(multime_noua)
    multime_noua = []
    for multime in lista_multimi:
        for stare in multime:
            if len(multime_noua) == 0 or len(multime) == 1:
                multime_noua.append({stare:multime[stare]})
            else:
                for parts in multime_noua:
                    ok=1
                    for litera in A:
                        if multime[stare][litera][1]!=parts[(list(parts.keys()))[0]][litera][1]:
                            ok=0
                    if ok:
                        parts[stare] = multime[stare]
                        break
                else:
                    multime_noua.append({stare: multime[stare]})
    return multime_noua



def indexare():
    for multime in multimi:
        for stare in multime:
            for litera in multime[stare]:
                for alta_multime in multimi:
                    if multime[stare][litera][0] in alta_multime:
                        multime[stare][litera][1] = multimi.index(alta_multime)#luam un index sa vedem in ce multime este
                        # dintre cele doua A sau B
                        # , daca se duce in alt index decat cel curent asa se va putea separa de altele




dictionar = {}
i=1
with open('input','r') as f:
    for line in f:
        if i==1:
            A=line.strip().split()
        if i==2:
            F=line.strip().split()
        if i==3:
            Q=line.strip().split()
            for stari in Q:
                dictionar[stari]={}

        if i>3:
            tranzitie = line.strip().split()
            dictionar[tranzitie[0]][tranzitie[1]] = [tranzitie[2], -1]
            pass
        i+=1

multimi = []
S1 = {}
S2 = {}
for stare in dictionar:
    if stare in F:
        S2[stare] = dictionar[stare]
    else:
        S1[stare] = dictionar[stare]

#print(S1)
#print(S2)
multimi.append(S1)
multimi.append(S2)
indexare() # am pus index
#print(len(multimi))
#print(multimi)
aux = partitionare(multimi) # multimea cu un pas inainte
#print(len(aux))
indexare()

while aux != multimi: # pana cand nu sunt egale atunci algoritmul continua
    multimi = partitionare(multimi)

    indexare()

    aux = partitionare(aux)

    indexare()
print("Starile finale dupa algoritmul de minimizare")
afisare(multimi)

#print(dictionar)
#print(A,F,Q)


