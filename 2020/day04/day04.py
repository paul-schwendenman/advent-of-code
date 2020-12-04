from contextlib import contextmanager
import fileinput
import re


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line for line in data]


def make_passport(passport):
    return dict([item.split(':') for item in passport.split()])


def validate_passport_field(passport, field):
    value = passport[field]
    if field == 'byr':
        year = int(value)
        return 1920 <= year <= 2002
    elif field == 'iyr':
        year = int(value)
        return 2010 <= year <= 2020
    elif field == 'eyr':
        year = int(value)
        return 2020 <= year <= 2030
    elif field == 'hgt':
        unit = value[-2:]
        if unit not in ('in', 'cm'):
            return False
        height = int(value[:-2])
        if unit == 'in':
            return 59 <= height <= 76
        elif unit == 'cm':
            return 150 <= height <= 193

    elif field == 'hcl':
        return bool(re.match(r'#[0-9a-f]{6}', value))
    elif field == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    elif field == 'pid':
        return bool(re.match(r'^[0-9]{9}$', value))
    elif field == 'cid':
        return value


def validate_passport_fields(passport):
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    return all(validate_passport_field(passport, field) for field in required_fields)


def validate_passport(passport):
    '''Ensure a passport has all the correct fields

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    '''
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    return all(field in passport for field in required_fields)


def part1(data):
    count = 0
    passports = ''.join(data).split('\n\n')

    for passport in passports:
        doc = make_passport(passport)
        if validate_passport(doc):
            count += 1

    return count



def part2(data):
    count = 0
    passports = ''.join(data).split('\n\n')

    for passport in passports:
        doc = make_passport(passport)
        if validate_passport(doc) and validate_passport_fields(doc):
            count += 1

    return count

def main():
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
