# Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε δακτυλίους. Έχετε στην κατοχή σας
# 27 δακτυλίους, 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο). Μια τριάδα που τερματίζει
# το παιχίνδι γίνεται οριζόντια, κάθετα ή διαγώνια. Η τριάδα αποτελείται από δακτυλίους 
# είτε του ίδιου μεγέθους είτε από το μικρό προς το μεγαλύτερο. Επειδή έχετε δακτύλιους, 
# ένας δακτύλιος μπορεί να μπει σε οποιοδήποτε τετράγωνο, αρκεί να μην έχει ήδη δακτύλιο 
# του ίδιου μεγέθους. Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 100 φορές 
# και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.

import random

# Arxikopoioyme to athroisma twn bhmatwn (tha to xrhsimopoihsoyme gia to meso oro)
sinolika_bhmata = 0

# Paizoyme to paixnidi 100 fores 
for k in range(100):
    #Arxikopoioyme to 'tablo' me 3 seires kai 3 styles
    tablo = [['' for i in range(3)] for i in range(3)]

    #Ftiaxnoyme mia lista me 27 diskoys 9 mikroys(S), 9 mesaioys(M) kai 9 megaloys(L)
    diskoi = ['S' for i in range(9)] + ['M' for i in range(9)] + ['L' for i in range(9)]
    random.shuffle(diskoi)

    win = False #thn xrhsimopoioyme gia na 'katalaboyme' to telos toy paixnidioy
    for diskos in diskoi:
        # Xrhsimopoioyme mia while wste na dokimazoyme na baloyme to tyxaio disko se mia tyxaia thesi
        # kai ean ayto den einai ethikto ksanadokimazoyme se allh thesi 
        while True:
            # Epilegoyme mia tyxaia thesi sto tamblo
            tyxaia_seira = random.randint(0,2)
            tyxaia_stylh = random.randint(0,2)

            # Elegxoyme ean h tyxaia thesi einai adeia h ean den periexei disko toy idioy megethoys 
            # wste na topothetisoyme to tyxaio disko mas
            if diskos not in tablo[tyxaia_seira][tyxaia_stylh]:
                tablo[tyxaia_seira][tyxaia_stylh] += diskos
                sinolika_bhmata += 1
                break #efoson topothetithike bgainoyme apo thn epanalhptikh diadikasia


        # Elegxoyme ean yparxei nikhfora triada 
        # Prwta elegxoyme tis diagwnioys
        if((((tablo[0][0] + tablo[1][1] + tablo[2][2]).count('S') == 3 or (tablo[0][0] + tablo[1][1] + tablo[2][2]).count('M') == 3 or (tablo[0][0] + tablo[1][1] + tablo[2][2]).count('L') == 3 ) or ('M' in tablo[1][1] and (('S' in tablo[2][2] and 'L' in tablo[0][0]) or ('L' in tablo[2][2] and 'S' in tablo[0][0])))) or 
            (((tablo[0][2] + tablo[1][1] + tablo[2][0]).count('S') == 3 or (tablo[0][2] + tablo[1][1] + tablo[2][0]).count('M') == 3 or (tablo[0][2] + tablo[1][1] + tablo[2][0]).count('L') == 3 ) or ('M' in tablo[1][1] and (('S' in tablo[2][0] and 'L' in tablo[0][2]) or ('L' in tablo[2][0] and 'S' in tablo[0][2]))))):
            win = True
            break 

        else:
            # Kai meta tis seires kai tis styles 
            for i in range(2):
                if ((((tablo[i][0] + tablo[i][1] + tablo[i][2]).count('S') == 3 or (tablo[i][0] + tablo[i][1] + tablo[i][2]).count('M') == 3 or (tablo[i][0] + tablo[i][1] + tablo[i][2]).count('L') == 3 ) or ('M' in tablo[i][1] and (('S' in tablo[i][2] and 'L' in tablo[i][0]) or ('L' in tablo[i][2] and 'S' in tablo[i][0])))) or
                    (((tablo[0][i] + tablo[1][i] + tablo[2][i]).count('S') == 3 or (tablo[0][i] + tablo[1][i] + tablo[2][i]).count('M') == 3 or (tablo[0][i] + tablo[1][i] + tablo[2][i]).count('L') == 3 ) or ('M' in tablo[1][i] and (('S' in tablo[2][i] and 'L' in tablo[0][i]) or ('L' in tablo[2][i] and 'S' in tablo[0][i]))))):
                        win = True
                        break 

        if win:
            break # Efoson yparxei stamatame thn epanalhpsh
            

# Briskoyme kai emfanizoyme ton teliko meso oro 
mesos_oros = sinolika_bhmata / 100
print('Sta 100 paixnidia eginan kata meso oro ' + str(mesos_oros) + ' bhmata.')
