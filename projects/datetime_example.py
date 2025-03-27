from datetime import datetime

# διάβασε μια ημερομηνία της μορφής ΕΕΕΕ.ΜΜ.ΗΗ 
# και εμφάνισε την ημερομηνία σε άλλες μορφές, 
# δείτε το https://strftime.org/
date1 =datetime.strptime("2024.4.10", "%Y.%m.%d")
print(date1.strftime("%d/%m/%Y"))
print(date1.strftime("%-d|%-m|%y"))
print(date1.strftime("%d-%B-%y"))
print(date1.strftime("%a %-d %b %Y"))
