import math
x = math.sqrt(2**101/(math.pi**53 + 11**7))

# εμφάνιση πλήρους αριθμητικού αποτελέσματος
print(x)

# εμφάνιση 10 πρώτων ψηφίων
s = str(x)
s = s.replace('.','')
print(s[:10])