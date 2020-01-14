#ΑΣΚΗΣΗ 1
#Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει τις πέντε μεγαλύτερες λέξεις ενός κειμένου
#το οποίο διαβάζει από αρχείο και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα.

#εισαγωγη αρχειου
text = open("RandomTextFile.txt").read().split()

#συναρτηση που βρισκει το μηκος καθε λεξης απο μια λιστα
def map_(A):
    return list(map(len, A))

words = map_(text) #λιστα που περιεχει των αριθμων των χαρακτηρων καθε λεξης
words,text = (zip(*sorted(zip(words, text)))) #ταξινόμηση στις λιστες με βαση το μεγεθος καθε λεξης

words =(list(reversed(words)))
text = (list(reversed(text)))


my_list=[]
for i in range(5):
    my_list.append(text[i])

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

reversed(my_list[::-1])

my_list = [w.replace(('a', 'e', 'i', 'o', 'u'), '') for w in words]


print (my_list)
