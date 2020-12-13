from day13 import part1, part2, find_schedule_timestamp


def test_part1_sample(sample_data):
    assert part1(sample_data) == 295


def test_part2_sample(sample_data):
    assert part2(sample_data) == 1068781


def test_part1_input(input_data):
    assert part1(input_data) == 1895


# def test_part2_input(input_data):
#     assert part2(input_data) == -1


def test_find_schedule_1():
    assert find_schedule_timestamp('7,13,x,x,59,x,31,19') == 1068781


def test_find_schedule_2():
    assert find_schedule_timestamp('17,x,13,19') == 3417


def test_find_schedule_3():
    assert find_schedule_timestamp('67,7,59,61') == 754018


def test_find_schedule_4():
    assert find_schedule_timestamp('67,x,7,59,61') == 779210


def test_find_schedule_5():
    assert find_schedule_timestamp('67,7,x,59,61') == 1261476


def test_find_schedule_6():
    assert find_schedule_timestamp('1789,37,47,1889') == 1202161486
