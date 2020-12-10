from collections import defaultdict
from contextlib import contextmanager
from typing import cast, List, Mapping, Tuple
import fileinput
import re

Passport = Mapping[str, str]
REQUIRED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line for line in data]


def parse_passport(raw_passport: str) -> Passport:
    return dict(cast(
        List[Tuple[str, str]],
        [item.split(':') for item in raw_passport.split()]
    ))


def validate_passport_field(passport: Passport, field: str) -> bool:
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
        return bool(re.match(r'^#[0-9a-f]{6}$', value))
    elif field == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    elif field == 'pid':
        return bool(re.match(r'^[0-9]{9}$', value))
    elif field == 'cid':
        return True

    return False


def validate_passport_fields(passport: Passport,
                             invalid_fields: Mapping[str, set],
                             valid_fields: Mapping[str, set]) -> None:
    for field in REQUIRED_FIELDS:
        if validate_passport_field(passport, field):
            valid_fields[field].add(passport[field])
        else:
            invalid_fields[field].add(passport[field])


def validate_passport(passport: Passport) -> bool:
    return all(field in passport for field in REQUIRED_FIELDS)


def make_invalid_passport(field: str, value: str) -> Mapping[str, str]:
    base_passport = {
        'byr': '2000',
        'iyr': '2015',
        'eyr': '2025',
        'hgt': '70in',
        'hcl': '#333333',
        'ecl': 'amb',
        'pid': '012345678',
    }
    base_passport[field] = value
    return base_passport


def generate_input(data: List[str]) -> List[str]:
    passports = ''.join(data).split('\n\n')

    valid_fields: Mapping[str, set] = defaultdict(set)
    invalid_fields: Mapping[str, set] = defaultdict(set)

    for passport in passports:
        doc = parse_passport(passport)
        if validate_passport(doc):
            validate_passport_fields(doc, invalid_fields, valid_fields)

    new_passports = []

    for item in invalid_fields['byr']:
        new_passports.append(make_invalid_passport('byr', item))
    for item in invalid_fields['iyr']:
        new_passports.append(make_invalid_passport('iyr', item))
    for item in invalid_fields['eyr']:
        new_passports.append(make_invalid_passport('eyr', item))
    for item in invalid_fields['hgt']:
        new_passports.append(make_invalid_passport('hgt', item))
    for item in invalid_fields['hcl']:
        new_passports.append(make_invalid_passport('hcl', item))
    for item in invalid_fields['ecl']:
        new_passports.append(make_invalid_passport('ecl', item))
    for item in invalid_fields['pid']:
        new_passports.append(make_invalid_passport('pid', item))

    new_passports.append(make_invalid_passport('cid', '012345'))

    return [' '.join('%s:%s' % (field, passport[field]) for field in REQUIRED_FIELDS) for passport in new_passports]


def main() -> None:
    with readfile() as data:
        out = generate_input(data)

    print('\n\n'.join(out))


if __name__ == '__main__':
    main()
