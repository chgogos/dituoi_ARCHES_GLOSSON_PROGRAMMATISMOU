from math import sqrt


def distance_percentage(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    d = sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)
    p = d / sqrt((255) ** 2 + (255) ** 2 + (255) ** 2)
    return p
