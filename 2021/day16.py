import fileinput
from dataclasses import dataclass, field
from enum import Enum
from math import prod
from typing import Optional, Tuple


class PacketType(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


@dataclass
class Packet:
    version: int
    type: PacketType
    value: int = field(default=0, init=False, repr=False)
    subpackets: list = field(default_factory=list, init=False, repr=False)


@dataclass
class LiteralPacket(Packet):
    value: int


@dataclass
class OperatorPacket(Packet):
    length_type_flag: bool = field(repr=False)
    subpackets: list[Packet] = field(default_factory=list, init=False)

    @property
    def value(self):
        values = [subpacket.value for subpacket in self.subpackets]

        if self.type == PacketType.SUM:
            return sum(values)
        elif self.type == PacketType.PRODUCT:
            return prod(values)
        elif self.type == PacketType.MINIMUM:
            return min(values)
        elif self.type == PacketType.MAXIMUM:
            return max(values)
        elif self.type == PacketType.GREATER_THAN:
            return 1 if values[0] > values[1] else 0
        elif self.type == PacketType.LESS_THAN:
            return 1 if values[0] < values[1] else 0
        elif self.type == PacketType.EQUAL_TO:
            return 1 if values[0] == values[1] else 0
        else:
            raise ValueError(self.type)

    def append(self, subpacket: Packet) -> None:
        self.subpackets.append(subpacket)


hex = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(data: str) -> str:
    return "".join(hex[char] for char in data)


def shift(data: str, num_bits: int) -> Tuple[str, str]:
    return data[:num_bits], data[num_bits:]


def parse_packet(data: str) -> Tuple[Packet, str]:
    raw_version, rest = shift(data, 3)
    raw_packet_type, rest = shift(rest, 3)

    version = int(raw_version, 2)
    packet_type = PacketType(int(raw_packet_type, 2))

    if packet_type == PacketType.LITERAL:
        raw_bits = ""
        group_flag = "1"

        while group_flag == "1":
            group_flag, rest = shift(rest, 1)
            value, rest = shift(rest, 4)

            raw_bits += value

        padding = 4 - (len(raw_bits) % 4) if len(raw_bits) % 4 != 0 else 0
        bits = int(raw_bits, 2)

        zeros, rest = shift(rest, padding)

        assert all(char == "0" for char in zeros)

        return LiteralPacket(version, packet_type, bits), rest

    else:
        length_type_id, rest = shift(rest, 1)
        length_type_flag = length_type_id == "1"
        packet = OperatorPacket(version, packet_type, length_type_flag=length_type_flag)

        if length_type_id == "0":
            raw_length, rest = shift(rest, 15)
            length = int(raw_length, 2)

            subpacket_data, rest = rest[:length], rest[length:]

            while subpacket_data:
                subpacket, subpacket_data = parse_packet(subpacket_data)
                packet.append(subpacket)
        elif length_type_id == "1":
            raw_num_packets, rest = shift(rest, 11)
            num_packets = int(raw_num_packets, 2)

            for _ in range(num_packets):
                subpacket, rest = parse_packet(rest)
                packet.append(subpacket)
        else:
            raise ValueError("Invalid length_type_id", length_type_id)

        return packet, rest


def sum_versions(packet: Packet) -> int:
    return packet.version + sum(
        sum_versions(subpacket) for subpacket in packet.subpackets
    )


def evaluate_packets(packet: Packet) -> int:
    return packet.value


def part1(data):
    data = hex_to_bin(data)

    packet, _ = parse_packet(data)

    return sum_versions(packet)


def part2(data):
    data = hex_to_bin(data)

    packet, _ = parse_packet(data)

    return packet.value


def main():
    with fileinput.input() as input:
        data = [line for line in input][0].rstrip()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
