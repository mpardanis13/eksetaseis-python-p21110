# H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
# Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε
# ποιος είναι ο τελευταίος γύρος και στην συνέχεια πάρτε τις τελευταίες 100 τιμές (πεδίο randomness)
# μέσα από το https://drand.cloudflare.com/public/{round}. Μετατρέψτε αυτές τις τιμές
# σε δυαδικό και εμφανίστε το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά 
# και το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες.

import requests
# Briskoyme ton arithmo toy teleytaioy gyroy 
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
round = data['round']

results = '' # Arxikopoioyme thn metablhth poy ua apothikeysoyme tis teleytaies 100 times

# Briskoyme tis teleytaies 100 times kai tis apothikeyoyme thn mia dipla sthn allh
# se ena megalo string afoy tis metatrepsoyme se dyadikes times
for i in range(round - 100, round + 1):
    r = requests.get(f'https://drand.cloudflare.com/public/{i}', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = r.json()
    binary = bin(int(data['randomness'],16)) # Metatrepoyme thn kathe timh prwta se dekadikh kai ystera se dyadikh
    results += binary[2:] # Apothikeyoyme kathe timh sta apotelesmata mas ksekinwntas apo to trito psifio wste na mhn apothikeytei kai h anaparastash ths ('0b')

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