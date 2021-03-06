#ΑΣΚΗΣΗ 1
#Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει τις πέντε μεγαλύτερες λέξεις ενός κειμένου
#το οποίο διαβάζει από αρχείο και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα.
#----------------------------------------------------------------------------------------------------

#εισαγωγη αρχειου
text = open("RandomTextFile.txt").read().split()

#συναρτηση που βρισκει το μηκος καθε λεξης απο μια λιστα
def map_(A):
    return list(map(len, A))

#συναρτηση που αφαιρει τις ",." απο το κειμενο
def remover(A):
    points =[".",","]
    for i in range(len(A)):
        for p in points:
            A[i]=A[i].replace(p,"")
    return(A)


text = remover(text) #αφαιρουμε τις ",." απο το λιστα κειμενου για να μενουν μονο οι λέξεις
words = map_(text)   #λιστα που περιεχει τον αριθμο των χαρακτηρων καθε λεξης

#----ευρεση max λεξεων
def Nmaxelements(list1,list2, N,list3): 
    final_list = []
    
    for i in range(0, N):  
        max1 = -1
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]
                textMax = list2[j]
        list1.remove(max1)
        list2.remove(textMax)
        final_list.append(max1)
        list3.append(textMax)
    return(list3)

list3 = []
Nmaxelements(words,text,5,list3)

print ("\nΛίστα με τις 5 μεγαλυτερες λεξεις",list3)

#αφαίρουμε τα φωνήεντα απο την λιστα με τις 5 πιο μεγαλες σε μηκος λεξεις
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(list3)):
    for v in vowels:
        list3[i] = list3[i].replace(v,"")

print ("\nΛιστα χωρις τα φωνήεντα",list3)

#αντιστρέφουμε καθε item της λιστας 
reversedstring = []
for i in range(5):
    reversedstring.append(''.join(reversed(list3[i])))

#εκτύπωση του τελικού ζητουμένου της άσκησης
print ("\nΛίστα χωρις τα φωνήεντα με αντεστραμένες τις λέξεις",reversedstring)


