# Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε 
# κάθε χαρακτήρα σε δυαδικό μήκους 7. Υπολογίστε ποια είναι η μεγαλύτερη 
# ακολουθία από συνεχόμενα 0 και από συνεχόμενα 1.

# Epilegoyme to arxeio poy theloyme na 'trabhksoyme' thn plhroforia 
file = '/Users/mpardanhs/Desktop/papei/Python/eksetastikhPython/askhsh9/two_cities_ascii.txt'

# Anoigoyme to arxeio kai diabazoyme kathe grammh toy apothikebontas th se mia lista 'seires'
with open(file) as f:
    seires = f.readlines()

f.close() #kleinoyme to arxeio afoy apothikeysame to periexomeno toy

# Ennwnoyme th lista twn seirwn se ena string me olo to periexomeno 
keimeno = ' '.join([str(elem) for elem in seires])

results = '' # Arxikopoioyme thn metablhth poy ua apothikeysoyme tis dyadikes times twn ascii xarakthrwn

# Gia kathe xarakthra vriskoyme th seira toy kai th metatrepoyme se dyadiko arithmo 
for xarakthras in keimeno:
    dyadikh_apeikonish = str(bin(ord(xarakthras)))[2:] # Kratame thn dyadikh anaparastash toy xarakthra mas ksekinwntas apo to trito psifio wste na mhn apothikeytei kai o typos ths anaparastashs ('0b')

    # Elegxoyme ean o arithmos einai 7 psifiwn diaforetika prosthetoyme ta aparaithta mhdenika sthn arxh toy wste na ginei 7psifios (sigoyra ua exoyme to poly 7 psifia kathws oi basikoi ascii xarakthres einai 127)
    if len(dyadikh_apeikonish) == 7:
        results += dyadikh_apeikonish
    else:
        results += (7-len(dyadikh_apeikonish))*'0' + dyadikh_apeikonish

# Arxika 'spame' to string twn apotelesmatwn simfwna me ta 1 (results.split('1'))kati poy exei ws apotelesma mia lista
# me stoixeia ths kenoys xarakthres kai tis akoloythies twn sinexomenwn 0. Sth synexeia taksinomoyme thn lista ayth 
# symfwna me to megethos ton akoloythiwn kai antistrefoyme th seira twn stoixeiwn ths wste na exoyme ws prwto stoixeio
# ths thn megalyterh akoloythia mhdenikwn (sorted(sorted(results.split('1'), key=len, reverse=True))). Apo ayth th lista
# epilegoyme to prwto stoixeio ([0]) to opoio periexei kai thn megalyterh akoloytheia kai me th synarthsh len vriskoyme
# to megethos ths akoloythias ayths. Analoga ergazomaste kai gia thn eyresh thn megalyterhs akoloytheias aswn.
mhkos_megalyterhs_akoloythias0 = len(sorted(results.split('1'), key=len, reverse=True)[0])
mhkos_megalyterhs_akoloythias1 = len(sorted(results.split('0'), key=len, reverse=True)[0])

# Emfanizoyme ta telika apotelesmata 
print(f'To mhkos ths megalyterhs akoloythias apo 0 einai: {mhkos_megalyterhs_akoloythias0} kai to mhkos ths megalyterhs akoloythias apo 1 einai: {mhkos_megalyterhs_akoloythias1}.')