import hashlib

def calc_hash(key, counter):
    data = (key + str(counter)).encode('utf-8')
    return hashlib.md5(data).hexdigest()


def check_hash(hash):
    return hash[:5] == "00000"


def main(key):
    for counter in range(100000000):
        hash = calc_hash(key, counter)
        if check_hash(hash):
            break

    return counter


if __name__ == "__main__":
    print(main('iwrupvqb'))
