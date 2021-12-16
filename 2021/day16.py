import fileinput
from dataclasses import dataclass, field

@dataclass
class Packet:
    version: int
    type: int
    data: str = None
    packets: list[any] = field(default_factory=list)

    def literal(self):
        if self.type == 4:
            return int(self.data, 2)


hex = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def hex_to_bin(data):
    return "".join(hex[char] for char in data)


def parse_packet(data):
    version, packet_type, rest = data[:3], data[3:6], data[6:]
    version = int(version, 2)
    packet_type = int(packet_type, 2)

    if packet_type == 4:
        bits = []

        while True:
            current, rest = rest[:5], rest[5:]

            if current[0] == '1':
                bits.append(current[1:])
            else:
                bits.append(current[1:])
                break

        bits = "".join(bits)
        padding = 4 - (len(bits) % 4) if len(bits) % 4 != 0 else 0

        print(f'{padding} {rest}')

        zeros, rest = rest[:padding], rest[padding:]

        assert all(char == '0' for char in zeros)

        return Packet(version, packet_type, bits), rest

    else:
        length_type_id, rest = rest[0], rest[1:]

        print(f'length_type_id: {length_type_id}')
        subpackets = []

        if length_type_id == '0':
            length, rest = rest[:15], rest[15:]
            length = int(length, 2)

            subpacket_data, rest = rest[:length], rest[length:]

            while subpacket_data:
                subpacket, subpacket_data = parse_packet(subpacket_data)
                print(f'subpacket: {subpacket} {subpacket.literal()}')

                subpackets.append(subpacket)
        elif length_type_id == '1':
            num_packets, rest = rest[:11], rest[11:]
            print(num_packets)
            num_packets = int(num_packets, 2)

            for _ in range(num_packets):
                subpacket, rest = parse_packet(rest)
                print(f'subpacket: {subpacket} {subpacket.literal()}')

                subpackets.append(subpacket)
        else:
            raise ValueError('Invalid length_type_id', length_type_id)


        return Packet(version, packet_type, packets=subpackets), rest

def sum_version(packet: Packet):
    return packet.version + sum(sum_version(subpacket) for subpacket in packet.packets)


def part1(data):
    data = hex_to_bin(data)

    packet, rest = parse_packet(data)

    return sum_version(packet)



def main():
    with fileinput.input() as input:
        data = [line for line in input][0].rstrip()

    print(part1(data))

if __name__ == '__main__':
    main()
