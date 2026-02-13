user_input = input("Παρακαλώ εισάγετε ένα κείμενο: ")
text_no_spaces = user_input.replace(" ", "")
reversed_text = text_no_spaces[::-1]
print("Το ανεστραμμένο κείμενο χωρίς κενά είναι:", reversed_text)
