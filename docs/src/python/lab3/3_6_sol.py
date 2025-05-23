import re

phones = """
Allison Neu 555-8396
Bob Newhall 555-4344
C. Montgomery Burns 555-0001
C. Montgomery Burns 555-0113
Canine College 555-7201
Canine Therapy Institute 555-2849
Cathy Neu 555-2362
City of New York Parking Violation Bureau 555-BOOT
Dr. Julius Hibbert 555-3642
Dr. Nick Riviera 555-NICK
Earn Cash For Your Teeth 555-6312
Family Therapy Center 555-HUGS
Homer Jay Simpson (Plow King episode) 555-3223
Homer Jay Simpson (work) 555-7334
Jack Neu 555-7666
Jeb Neu 555-5543
Jennifer Neu 555-3652
Ken Neu 555-8752
Lionel Putz 555-5299
MAD Magazine 555-8628
Marital Street Hotline 555-1680
Marvin Monroe 555-3700
Marvin Monroe's radio therapy show 555-PAIN
Moe Szyslak (phone number spells SMITHERS) 7648-4377
Moe Szyslak 555-0000
Moe's Tavern 555-1239
Mr. Plow 555-3226
NY Metro 555-5680
Ned Flanders 555-8904
New York Parking Violation Bureau 555-2668
ORB 	Dr Nick's "B"argain Medical Services 1-800-DOCT
Original Famous Ray's Pizza 555-PIZA
Otto's "How's my Driving" 555-8821
Plow King 555-4796
Pretzel Wagon 555-3226
Prof John Frink's Lab 555-5782
Radio Psychaiatrist 555-7246
Reverend Timothy Lovejoy 555-6542
Richard Nash 555-9996
Richard Newhall 555-9973
Ruff-form Dog School 555-0078
Santitarium for Dogs 555-9716
Sleep-Eazy Motel 555-1000
Sugar Truck 555-3872
Susan Newhall 555-2362
The Nuclear Powerplant 555-5246
The Simpsons' residence 555-8707
The Simpsons, 742 Evergreen Terrace 555-0113
Toby Muntz 555-9972
"""

print("Ερώτημα 1")
results = re.findall(
    r"(\bJ.*)(\d{3}-\d{4}|[a-z]{4})", phones, flags=re.IGNORECASE | re.MULTILINE
)
for result in results:
    print(f"{result[0]} -> {result[1]}")

print("Ερώτημα 2")
results = re.findall(
    r"(\b.*eu).*(\d{3}-\d{4}|[a-z]{4})", phones, flags=re.IGNORECASE | re.MULTILINE
)
for result in results:
    print(f"{result[0]} -> {result[1]}")

print("Ερώτημα 3")
results = re.findall(
    r"(.*)(\d{3}-[a-z]{4})", phones, flags=re.IGNORECASE | re.MULTILINE
)
for result in results:
    print(f"{result[0]} -> {result[1]}")

print("Ερώτημα 4")
results = re.findall(
    r"(.*)(\d{3}-(\d{4}|[a-z]{4}))$", phones, flags=re.IGNORECASE | re.MULTILINE
)

for result in sorted(results, key=lambda row: row[2]):
    print(f"{result[1]} -> {result[0]}")
