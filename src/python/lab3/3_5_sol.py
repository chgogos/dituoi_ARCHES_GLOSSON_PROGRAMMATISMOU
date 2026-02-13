import os
import re
import unittest


def part1():
    with open(
        os.path.join(os.path.dirname(__file__), "aoc2020_d2_input.txt"), "r"
    ) as f:
        regex = re.compile(
            "(?P<low>\d+)-(?P<hi>\d+)(\s)(?P<key_char>\w)(:\s)(?P<pwd>\w+)"
        )
        c = 0
        for line in f.readlines():
            match = regex.match(line)
            pwd = match.group("pwd")
            x = pwd.count(match.group("key_char"))
            if int(match.group("low")) <= x <= int(match.group("hi")):
                c += 1
        return c


def part2():
    with open(
        os.path.join(os.path.dirname(__file__), "aoc2020_d2_input.txt"), "r"
    ) as f:
        regex = re.compile(
            "(?P<pos1>\d+)-(?P<pos2>\d+)(\s)(?P<key_char>\w)(:\s)(?P<pwd>\w+)"
        )
        c = 0
        for line in f.readlines():
            match = regex.match(line)
            pwd = match.group("pwd")
            key_char = match.group("key_char")
            pos1 = int(match.group("pos1")) - 1
            pos2 = int(match.group("pos2")) - 1
            if pwd[pos1] == pwd[pos2]:
                continue
            if pwd[pos1] == key_char or pwd[pos2] == key_char:
                c += 1
        return c


class TestAOC2020Day2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(), 660)

    def test_part2(self):
        self.assertEqual(part2(), 530)


unittest.main()
