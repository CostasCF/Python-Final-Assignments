#ΑΣΚΗΣΗ 1
#Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει τις πέντε μεγαλύτερες λέξεις ενός κειμένου
#το οποίο διαβάζει από αρχείο και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα.
#----------------------------------------------------------------------------------------------------

#εισαγωγη αρχειου
text = open("RandomTextFile.txt").read().split()

#συναρτηση που βρισκει το μηκος καθε λεξης απο μια λιστα
def map_(A):
    return list(map(len, A))

#------------ ταξινόμηση-------------------------------------------------
words = map_(text) #λιστα που περιεχει των αριθμων των χαρακτηρων καθε λεξης
print(words)
words,text = (zip(*sorted(zip(words, text)))) #ταξινόμηση στις λιστες με βαση το μεγεθος καθε λεξης


#-----------γυρίζει ανάποδα τις λίστες --------

words =(list(reversed(words)))
text = (list(reversed(text)))
print (text)

#----------- δημιουργια λιστας που περιεχει τις πιο 5 πιο μεγαλες σε μηκος λεξεις---------
mylist=[]
for i in range(5):
    mylist.append(text[i])
print (mylist)

#-----------αφαίρει τα φωνήεντα απο τις 5 πιο μεγαλες σε μηκος λεξεις
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(mylist)):
    for v in vowels:
        mylist[i] = mylist[i].replace(v,"")
print(mylist)

