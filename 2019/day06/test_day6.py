from day6 import calc_orbits, calc_hops, main, main2


def test_calc_orbits():
    assert calc_orbits(["COM)B", "B)C"]) == 3


def test_calc_orbits2():
    assert calc_orbits(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']) == 42


def test_calc_hops():
    assert calc_hops(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']) == 4  # noqa: E501


def test_main():
    assert main() == 154386


def test_main2():
    assert main2() == 346
