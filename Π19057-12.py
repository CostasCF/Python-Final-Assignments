#ΑΣΚΗΣΗ 12
#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ και εμφανίζει πόσες μέρες/ώρες/δευτερόλεπτα
#απέχει αυτή από σήμερα καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας.
import datetime
import calendar

DateInput = input("Εισαγεται ημερομονία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ: ")
day,month,year = DateInput.split('/')
a = datetime.datetime(int(year),int(month),int(day)) # εισαγουμε στο προγραμμα μια συγκεκριμένη ημορομονία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ
b = datetime.datetime.now() #η ώρα σήμερα

delta = b - a
days = (delta.days) #Ημερες
hours = (delta.days)*24 #ωρες
seconds = (delta.days)*86400 #δευτερολεπτα


#ποσες ημερες εχει ο μήνας εκείνης της ημερομηνίας 
print (calendar.monthrange(int(year), int(month))[1])

#εκτυπώνει σε ποσες μερες/ωρες/δευτερολεπτα απεχει η ταδε ημερομηνία απο την σημερινη
print (days,"μέρες /",hours,"ώρες /",seconds,"δευτερολεπτα")

