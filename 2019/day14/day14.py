from collections import namedtuple
import math

Formula = namedtuple('Formula', 'product reactants')
Product = namedtuple('Product', 'quantity name')
Reactant = namedtuple('Reactant', 'quantity name')


def debug(f):
    def wrapper(*args, **kwargs):
        # print(f'args: {args[1:]} kwargs: {kwargs}')
        return f(*args, **kwargs)
    return wrapper


@debug
def find_reactants(formulas, extra_produced={}, requested_quantity=1, product='FUEL'):
    if product == 'ORE':
        return requested_quantity, extra_produced
    formula = formulas[product]

    needed_quantity = requested_quantity - extra_produced.get(product, 0)
    multiplier = math.ceil(needed_quantity / formula.product.quantity)
    # print(f'multi {product}: {multiplier} = ceiling(({requested_quantity} - {extra_produced.get(product, 0)}) / {formula.product.quantity})')  # noqa: E501

    extra = (formula.product.quantity * multiplier) - needed_quantity
    # print(f'extra {product}: {extra} = (({multiplier} * {formula.product.quantity}) - {needed_quantity})')
    if extra:
        extra_produced[product] = extra
    elif product in extra_produced:
        del extra_produced[product]

    results = []
    # print(f'searching children of {product}: {", ".join(reactant.name for reactant in formula.reactants)}')
    for reactant in formula.reactants:
        reactant_requested_quantity = multiplier * reactant.quantity
        result, extra_produced = find_reactants(formulas, extra_produced.copy(), reactant_requested_quantity, reactant.name)  # noqa: E501
        results.append(result)

    # print(f'results {product}: {sum(results)} = {" + ".join(str(r) for r in results)}')

    return sum(results), extra_produced


def main(filename="puzzle1.in"):
    with open(filename) as file:
        lines = file.read().splitlines()

    reactions = [line.split(' => ') for line in lines]
    reactions = [(reaction[1].split(' '), [reactant.split(' ') for reactant in reaction[0].split(', ')]) for reaction in reactions]  # noqa: E501

    formulas = {reaction[0][1]: Formula(product=Product(quantity=int(reaction[0][0]), name=reaction[0][1]), reactants=[Reactant(quantity=int(reactant[0]), name=reactant[1]) for reactant in reaction[1]]) for reaction in reactions}  # noqa: E501

    produced, _extra = find_reactants(formulas)

    return produced


def main2(filename="puzzle1.in"):
    with open(filename) as file:
        lines = file.read().splitlines()

    reactions = [line.split(' => ') for line in lines]
    reactions = [(reaction[1].split(' '), [reactant.split(' ') for reactant in reaction[0].split(', ')]) for reaction in reactions]  # noqa: E501

    formulas = {reaction[0][1]: Formula(product=Product(quantity=int(reaction[0][0]), name=reaction[0][1]), reactants=[Reactant(quantity=int(reactant[0]), name=reactant[1]) for reactant in reaction[1]]) for reaction in reactions}  # noqa: E501

    request = 1
    produced = 0
    offset = 0
    last = 0
    while True:
        produced = find_reactants(formulas, requested_quantity=(offset+request))[0]
        # print(f'{produced:13} {(request + offset):12} {last:12}')

        if produced > 1e12:
            if last + 1 == offset + request:
                break
            request = 1
            offset = last
        else:
            last = request + offset
            request *= 2

    return last


if __name__ == "__main__":
    print(main())
    print(main2())
    # print(main('example1.in'))
