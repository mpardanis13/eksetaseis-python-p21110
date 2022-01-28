# Έστω μία σκακίερα 8*8 στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις,
# έναν λευκό πύργο και ένα μαύρο αξιωματικό. Σε κάθε γύρο, ο κάθε παίκτης
# παίρνει ένα βαθμό αν το κομμάτι του τρώει κομμάτι του αντιπάλου. Μετά από
# 100 παιχνίδια, εμφανίστε τους βαθμούς των δύο παικτών. Επαναλλάβετε το πείραμα
# 100 φορές για σκακιέρες 7*7 και 7*8 και εμφανίστε τους αντίστοιχους βαθμούς των παικτών.

import random

# Sinthetoyme to programma mas me th xrhsh mias synarthshs 'skaki' wste na mporoyme
# na pragmatopoihsoyme thn idia diadikasia gia opoiondhpote arithmo seirwn kai stylwn 
def skaki(seires, styles):
    # Arxikopoioyme toys bathmoys twn dyo paixtwn 
    vathmos1 = 0
    vathmos2 = 0

    # Pragmatopoioyme 100 paixnidia 
    for i in range(100):
        
        # Kathorizetai tyxaia poios paixths ua exei ton pyrgo kai poios ton aksiwmatiko 
        paixths1 = 'pyrgos' if (random.randint(0,1)) else 'aksiwmatikos'

        # Topothetoyme tyxaia sth skakiera ton pyrgo kai ton aksiwmatiko prosexontas na mhn 'pesoyn' o enas panw ston allo 
        thesi_pyrgoy = [random.randint(0,seires), random.randint(0,styles)]
        thesi_aksiwmatikoy = thesi_pyrgoy

        while thesi_pyrgoy == thesi_aksiwmatikoy:
            thesi_aksiwmatikoy = [random.randint(0,seires), random.randint(0,styles)]

        # Arxizontas me ton pyrgo (kathws einai leykos) ginontai tyxaies kinhseis mexri kapoios na 'faei' ton allo 
        while True:
            # Metakinoyme ton pyrgo mono katakoryfa h orizontia elegxontas wste na mh parameinei sthn idia thesi
            kateythinsh_pyrgoy = random.randint(0,1)
            thesi_pyrgoy[kateythinsh_pyrgoy] = random.choice([i for i in range(0, seires if kateythinsh_pyrgoy == 0 else styles) if i != thesi_pyrgoy[kateythinsh_pyrgoy]]) 
            if thesi_pyrgoy == thesi_aksiwmatikoy: # An o pyrgos 'faei' ton aksiwmatiko dinoyme enan vathmo ston paixth poy kerdise
                if paixths1 == 'pyrgos':
                    vathmos1 += 1
                else:
                    vathmos2 += 1
                break
            
            # Metakinoyme ton aksiwmatiko elegxontas wste aytos na mh bgei ektos skakieras
            while True:
                pithani_thesi = [0,0]

                # Dialegoyme tyxaia to megethos ths kinhshs toy aksiwmatikoy
                bhmata = random.choice([i for i in range(-seires,seires) if i != thesi_aksiwmatikoy[0]])

                # Dialegoyme tyxaia mia apo tis 2 diagwnioys gia na metakinithei o aksiwmatikos
                if(random.randint(0,1)):
                    pithani_thesi[0] = thesi_aksiwmatikoy[0] + bhmata
                    pithani_thesi[1] = thesi_aksiwmatikoy[1] + bhmata
                else:
                    pithani_thesi[0] = thesi_aksiwmatikoy[0] + bhmata
                    pithani_thesi[1] = thesi_aksiwmatikoy[1] - bhmata

                if (pithani_thesi[0] >= 0 and pithani_thesi[0] < seires and pithani_thesi[1] >= 0 and pithani_thesi[1] < styles):
                    thesi_aksiwmatikoy[0] = pithani_thesi[0]
                    thesi_aksiwmatikoy[1] = pithani_thesi[1]
                    break


            if thesi_pyrgoy == thesi_aksiwmatikoy:
                if paixths1 == 'aksiwmatikos': # An o aksiwmatikos 'faei' ton pyrgo dinoyme enan vathmo ston paixth poy kerdise
                    vathmos1 += 1
                else:
                    vathmos2 += 1
                break
    # Emfanizoyme ta apotelesmata gia kathe skakiera 
    print(f"Gia thn skakiera {seires}*{styles} h bathmologia twn dyo paiktwn einai: Paixths1: {vathmos1}, Paixths2: {vathmos2}" )
    



# Kaloyme th sinarthsh skakiera gia kathe arithmo seirwn kai stylwn
skaki(8,8)
skaki(7,7)
skaki(7,8)