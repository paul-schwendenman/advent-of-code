from day15 import calc_score, Ingredient

def test_calc_score():
	ingredients = [
		Ingredient(name='Butterscotch', capacity=-1, durability=-2, flavor=6, texture=3, calories=8),
		Ingredient(name='Cinnamon', capacity=2, durability=3, flavor=-2, texture=-1, calories=3)
	]

	assert 62842880 == calc_score(ingredients, [44, 56])

