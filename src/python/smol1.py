button_list = []

for i in range(10):
    button = lambda: print(i)
    button_list.append(button)
    
for button in button_list:
    button()