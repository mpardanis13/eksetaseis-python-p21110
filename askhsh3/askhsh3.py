# Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
# Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο
# με μόνο γράμματα και τον κενό χαρακτήρα (space). Χωρείστε αυτό το
# κείμενο σε λέξεις σύμφωνα με το κενό και ξεκινείστε να αφαιρείτε 
# ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20. Βγάλτε
# τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις του
# ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ.

# Epilegoyme to arxeio poy theloyme na 'trabhksoyme' thn plhroforia 
file = '/Users/mpardanhs/Desktop/papei/Python/eksetastikhPython/askhsh3/two_cities_ascii.txt'

# Anoigoyme to arxeio kai diabazoyme kathe grammh toy apothikebontas th se mia lista 'seires'
with open(file) as f:
    seires = f.readlines()

# Ennwnoyme th lista twn seirwn se ena string me olo to periexomeno 
seires = ' '.join([str(elem) for elem in seires])

# 'Filtraroyme' thn lista wste na parameinoyn se ayth mono grammata kai kena 
filteredSeires = ''
for char in seires:
    if((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90) or ord(char) == 32):
        filteredSeires += char

# 'Spame to keimeno se mia lista (simfwna me to whitespace) me stoixeia ths kathe leksh toy keimenoy'
lekseis = filteredSeires.split()

telikesLekseis = [] # Arxikopoioyme mia lista sthn opoia ua apothikseysoyme tis telikes lekseis

panwApo20 = [leksh for leksh in lekseis if len(leksh) > 20] # Afairoyme apo tis lekseis aytes poy exoyn panw apo 20 grammata kathws den apaloifontai me kapoia allh leksh

# Sth lista telikesLekseis apothikeyoyme oles tis lekseis mas omadopoihmenes analoga me to plithos twn grammatws toys 
for i in range(21):
    telikesLekseis.append([leksh for leksh in lekseis if len(leksh) == i])

# Oi lekseis me 10 grammata ua prepei na meinoyn mises kathws apaloifontai metaksy toys 
del telikesLekseis[10][:int(len(telikesLekseis[10])/2)]

# Gia kathe omada grammatwn (1-19, 2-18, 3-17 ktl) elegxoyme poia omada periexei perissotera
# grammata kai analoga eksaloifoyme thn katwterh omada enw afairoyme to plithos tis apo thn megalyterh omada
for i in range(1,10):
    if len(telikesLekseis[i-1]) > len(telikesLekseis[20-i]):
        del telikesLekseis[i-1][:len(telikesLekseis[20-i])]
        telikesLekseis.pop(20-i)
    else:
        del telikesLekseis[20-i][:len(telikesLekseis[i-1])]
        telikesLekseis.pop(i-1)

# Emfanizoyme ta statistika 
for omadaGrammatwn in telikesLekseis:
    print (str(len(omadaGrammatwn)) + ' lekseis toy enos grammatos' if(len(omadaGrammatwn[0]) == 1) else ( str(len(omadaGrammatwn)) + ' lekseis twn ' + str(len(omadaGrammatwn[0])) + ' grammatwn.'))

print(str(len(panwApo20)) + ' lekseis me perissotera apo 20 grammata.')