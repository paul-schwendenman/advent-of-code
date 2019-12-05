import hashlib

def calc_hash(key, counter):
    data = (key + str(counter)).encode('utf-8')
    return hashlib.md5(data).hexdigest()


def check_hash(hash, leading_zeros=5):
    return hash[:leading_zeros] == "0" * leading_zeros


def main(key, leading_zeros=5):
    for counter in range(100000000):
        hash = calc_hash(key, counter)
        if check_hash(hash, leading_zeros):
            break

    return counter


if __name__ == "__main__":
    print(main('iwrupvqb', 6))
