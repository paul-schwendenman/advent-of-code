import fileinput
from collections import deque

def count_increases(measurements):
    past = measurements[0]
    count = 0

    for measurement in measurements[1:]:
        if past < measurement:
            count += 1
        past = measurement

    return count

def count_window(measurements):
    window = deque(measurements[:3])
    count = 0

    for measurement in measurements[3:]:
        past_sum = sum(window)

        window.append(measurement)
        window.popleft()

        current_sum = sum(window)

        if past_sum < current_sum:
            count += 1

        past_sum = current_sum

    return count


def main():
    with fileinput.input() as input:
        measurements = [int(line) for line in input]

    print(count_increases(measurements))
    print(count_window(measurements))

if __name__ == '__main__':
    main()
