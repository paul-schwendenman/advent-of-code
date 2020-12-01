from day8 import main, main2


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out[-5:] == "1548\n"


def test_main2(capsys):
    main2()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == " ##  #### #  # #  #  ##  \n#  # #    # #  #  # #  # \n#    ###  ##   #  # #  # \n#    #    # #  #  # #### \n#  # #    # #  #  # #  # \n ##  #### #  #  ##  #  # \n"  # noqa: E501
