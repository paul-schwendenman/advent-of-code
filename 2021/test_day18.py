from day18 import calc_magnitude, parse, add


def test_add():
	a = parse('[1,2]')
	b = parse('[[3,4],5]')

	assert str(add(a, b)) == '[[1,2],[[3,4],5]]'


def test_magnitude():
	a = parse("[9,1]")

	assert calc_magnitude(a) == 29


def test_magnitude2():
	a = parse("[[9,1],[1,9]]")

	assert calc_magnitude(a) == 129


def test_magnitude3():
	a = parse("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
	print(a)

	assert calc_magnitude(a) == 1384


def test_magnitude4():
	a = parse("[[[[1,1],[2,2]],[3,3]],[4,4]]")
	print(a)

	assert calc_magnitude(a) == 445
