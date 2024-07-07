# Εναλλακτική, συντομότερη λύση για την άσκηση Ε3Α4
import os
import xml.etree.ElementTree as ET

fn = os.path.join(os.path.dirname(__file__), "ITC2021_Test8_SolGenMethodA.xml")
with open(fn) as xml_f:
    tree = ET.ElementTree(file=xml_f)

matches = {}
for elem in tree.getroot()[1]:
    matches[(int(elem.attrib["home"]), int(elem.attrib["away"]))] = int(
        elem.attrib["slot"]
    )

nr_of_teams = max([t[0] for t in matches.keys()]) + 1
for team1 in range(nr_of_teams):
    for team2 in range(team1 + 1, nr_of_teams):
        slot1 = matches[(team1, team2)]
        slot2 = matches[(team2, team1)]
        print(
            f"Η ομάδα {team1} παίζει εναντίον της ομάδας {team2} στις αγωνιστικές {slot1} & {slot2}, διαφορά {abs(slot1-slot2)}"
        )
