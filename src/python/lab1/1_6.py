import hashlib

text = "ΠΑΝΕΠΙΣΤΗΜΙΟ ΙΩΑΝΝΙΝΩΝ"
hash1 = hashlib.sha256(
    text.encode()
).hexdigest()  # Καθορίζουμε την αρχική hash τιμή του κειμένου
print(hash1)  # 05f4cd1984d18f7200e31891c2b66ba6752568a691ce077da8824c9e0ef05fe3

text = "ΠΑΝΕΠΙΣΤΗΜΙΟ ΙΩΑΝΝΙΝΩΝ28706162"
hash2 = hashlib.sha256(
    text.encode()
).hexdigest()  # Hash τιμή του κειμένου με την προσθήκη του αριθμού 28706162
print(hash2) # 5c4b9aaed7f48d66a643fc05665f868454c1517e9f5f108b0478305c00000000
