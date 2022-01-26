import random

# Arxikopoioyme to athroisma twn bhmatwn (tha to xrhsimopoihsoyme gia to meso oro)
sinolika_bhmata = 0

for k in range(100):
    #Arxikopoioyme to 'tablo' me 3 seires kai 3 styles
    tablo = [['' for i in range(3)] for i in range(3)]

    #Ftiaxnoyme mia lista me 27 kapakia 9 mikra(S), 9 mesaia(M) kai 9 megala(L)
    kapakia = ['S' for i in range(9)] + ['M' for i in range(9)] + ['L' for i in range(9)]
    random.shuffle(kapakia)

    win = False 
    for kapaki in kapakia:

    #     # Xrhsimopoioyme mia while wste na dokimazoyme na baloyme to tyxaio kapaki se mia tyxaia thesi
    #     # kai ean ayto den einai ethikto ksanadokimazoyme se allh thesi 
        while True:
        
            # Epilegoyme mia tyxaia thesi sto tamblo
            tyxaia_thesi = tablo[random.randint(0,2)][random.randint(0,2)]

            # Elegxoyme th periptwsh poy den yparxei kenh thesi alla 'trabiksame' to mikrotero kommati 
            # wste na trabiksoyme kapoio allo
            if((kapaki == 'S' and not any('' in seira for seira in tablo)) or (kapaki == 'M' and not any('S' in seira for seira in tablo))):
                kapaki = kapakia[random.randint(1, len(kapakia)-1)]

            # Elegxoyme ean h tyxaia thesi einai adeia h exei kapoio mikrotero kapaki wste na topothetisoyme
            # to tyxaio kapaki mas
            if tyxaia_thesi == '' or kapaki < tyxaia_thesi:
                tablo[random.randint(0,2)][random.randint(0,2)] = kapaki
                sinolika_bhmata += 1 # Auksanoyme ta bhmata afoy topothetisame ena kapaki
                break #efoson topothetithike bgainoyme apo thn epanalhptikh diadikasia

        # Elegxoyme ean yparxei nikhfora triada prosexontas kai gia ta kena pedia
        for i in range(2):
            if ((tablo[i][0] == tablo[i][1] == tablo[i][2] != '') or (((tablo[i][0] < tablo[i][1] < tablo[i][2]) or (tablo[i][0] > tablo[i][1] > tablo[i][2])) and '' not in (tablo[i][0], tablo[i][1], tablo[i][2])) or 
                (tablo[0][i] == tablo[1][i] == tablo[2][i] != '') or (((tablo[0][i] < tablo[1][i] < tablo[2][i]) or (tablo[0][i] > tablo[1][i] > tablo[2][i])) and '' not in (tablo[0][i], tablo[1][i], tablo[2][i])) or 
                (tablo[0][0] == tablo[1][1] == tablo[2][2] != '') or (((tablo[0][0] < tablo[1][1] < tablo[2][2]) or (tablo[0][0] > tablo[1][1] > tablo[2][2])) and '' not in (tablo[0][0], tablo[1][1], tablo[2][2])) or 
                (tablo[0][2] == tablo[1][1] == tablo[2][0] != '') or (((tablo[0][2] < tablo[1][1] < tablo[2][0]) or (tablo[0][2] > tablo[1][1] > tablo[2][0])) and '' not in (tablo[0][2], tablo[1][1], tablo[2][0]))):

                # Efoson yparxei stamatame thn epanalhpsh
                win = True
                break
        
        if win:
            break

# Briskoyme kai emfanizoyme ton teliko meso oro 
mesos_oros = sinolika_bhmata/100
print(mesos_oros)






            





