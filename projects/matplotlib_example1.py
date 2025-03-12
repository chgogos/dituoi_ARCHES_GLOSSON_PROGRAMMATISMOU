import matplotlib.pyplot as plt

days = ['Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή']
values = [10, 40, 50, 20, 35]
plt.bar(days, values, color='skyblue')
plt.ylabel('Περιστατικά')
plt.show()
