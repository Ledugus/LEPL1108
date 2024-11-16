from devoir1 import devoir1


TRAJETS = [
    "BRU-PAR",
    "BRU-AMS",
    "BRU-LON",
    "BRU-COL",
    "PAR-BOR",
    "PAR-LYO",
    "PAR-FRA",
    "PAR-LON",
    "PAR-REN",
    "AMS-BER",
    "AMS-COL",
    "AMS-HAM",
    "COL-HAM",
    "COL-FRA",
    "COL-BER",
    "LYO-MAR",
    "LYO-ZUR",
    "FRA-HAM",
    "FRA-BER",
    "FRA-MUN",
    "FRA-ZUR",
    "BER-MUN",
    "BER-HAM",
    "BER-PRA",
    "MUN-ZUR",
    "MIL-LYO",
    "MIL-ZUR",
    "LYO-BAR",
    "BAR-MAR",
    "BOR-TLS",
    "TLS-BAR",
    "TLS-MAR",
    "LON-BIR",
    "LON-MAN",
    "MAN-BIR",
    "MAN-EDI",
    "EDI-GLW",
    "LYO-TLS",
    "HAM-COP",
    "PAR-TLS",
]

DUREES = [
    80,
    95,
    120,
    105,
    120,
    110,
    230,
    140,
    90,
    385,
    180,
    300,
    215,
    60,
    280,
    110,
    240,
    280,
    275,
    200,
    235,
    255,
    175,
    265,
    210,
    270,
    240,
    330,
    285,
    120,
    195,
    225,
    95,
    140,
    80,
    190,
    50,
    250,
    280,
    260,
]

VILLE_DEPART = "FRA"

AVION = [
    75,
    125,
    70,
    100,
    105,
    60,
    30,
    90,
    120,
    125,
    65,
    105,
    80,
    105,
    95,
    75,
    55,
    75,
    65,
    95,
    105,
    55,
]

SACRIFICE = 120


if __name__ == "__main__":

    ville, min_distances_train, min_distances_avion, count_train = devoir1(
        TRAJETS, DUREES, VILLE_DEPART, AVION, SACRIFICE
    )
    print("Villes", ville)
    print("min_distances train", min_distances_train)
    print("min_distances avion", min_distances_avion)
    print(count_train)
