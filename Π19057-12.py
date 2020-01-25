#ΑΣΚΗΣΗ 12
#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ και εμφανίζει πόσες μέρες/ώρες/δευτερόλεπτα
#απέχει αυτή από σήμερα καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας.
import datetime

DateInput = input("Εισαγετε ημερομονία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ: ")
day,month,year = DateInput.split('/')
a = datetime.datetime(int(year),int(month),int(day)) # εισαγουμε στο προγραμμα μια συγκεκριμένη ημορομονία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ
b = datetime.datetime.now() #η ώρα σήμερα

difference = b - a
days = (difference.days) #Ημερες
hours = (difference.days)*24 #ωρες
seconds = (difference.days)*86400 #δευτερολεπτα

#εκτυπώνει σε ποσες μερες/ωρες/δευτερολεπτα απεχει η ταδε ημερομηνία απο την σημερινη και το αντιστροφο

if b>a:
    print ("H ημερομηνία αυτη ανήκει στο παρελθον για ",days,"μέρες /",hours,"ώρες /",seconds,"δευτερολεπτα")
else:
    print ("Η ημερομηνία αυτη θα έρθει σε ",abs(days),"μέρες /",abs(hours),"ώρες /",abs(seconds),"δευτερολεπτα"," απο σήμερα")

#συναρτηση που βρισκει την τελευταια μερα μιας συγκεκριμενης ημερομονιας αφαιρόντας
#την ακριβως επομενη μερα του επομενου μήνα
def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

print ("Ημέρες του",int(month),"μήνα του",int(year),':',last_day_of_month(a).day)
