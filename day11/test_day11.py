from day11 import main


def test_main_part1():
    assert main(filename='day11/input') == 2319


def test_main_part2(capsys):
    main(1, filename='day11/input')
    captured = capsys.readouterr()
    assert captured.out == ' #  # #### ###  ###  ###  ####  ##    ##   \n #  # #    #  # #  # #  # #    #  #    #   \n #  # ###  #  # #  # #  # ###  #       #   \n #  # #    ###  ###  ###  #    # ##    #   \n #  # #    # #  #    # #  #    #  # #  #   \n  ##  #### #  # #    #  # #     ###  ##    \n'  # noqa: E501
