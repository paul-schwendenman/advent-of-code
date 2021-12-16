from day16 import parse_packet, evaluate_packets, sum_version, hex_to_bin, PacketType

def test_parse_literal_packet():
    data = hex_to_bin('D2FE28')

    packet, _ = parse_packet(data)

    assert packet.type == PacketType.LITERAL
    assert packet.version == 6
    assert packet.literal() == 2021


def test_parse_operator_packet():
    data = hex_to_bin('38006F45291200')

    packet, _ = parse_packet(data)

    assert packet.type == 6
    assert packet.version == 1
    assert packet.literal() == None
    assert len(packet.packets) == 2
    assert packet.packets[0].literal() == 10
    assert packet.packets[1].literal() == 20

def test_parse_operator_packet2():
    data = hex_to_bin('EE00D40C823060')

    packet, _ = parse_packet(data)

    assert packet.type == 3
    assert packet.version == 7
    assert packet.literal() == None
    assert len(packet.packets) == 3
    assert packet.packets[0].literal() == 1
    assert packet.packets[1].literal() == 2
    assert packet.packets[2].literal() == 3

def test_sum_versions():
    data = hex_to_bin('8A004A801A8002F478')

    packet, _ = parse_packet(data)

    assert sum_version(packet) == 16


def test_sum_versions2():
    data = hex_to_bin('620080001611562C8802118E34')

    packet, _ = parse_packet(data)

    assert sum_version(packet) == 12


def test_sum_versions3():
    data = hex_to_bin('C0015000016115A2E0802F182340')

    packet, _ = parse_packet(data)

    assert sum_version(packet) == 23


def test_sum_versions4():
    data = hex_to_bin('A0016C880162017C3686B18A3D4780')

    packet, _ = parse_packet(data)

    assert sum_version(packet) == 31


def test_evalute_packet_addition():
    data = hex_to_bin('C200B40A82')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 3


def test_evalute_packet_product():
    data = hex_to_bin('04005AC33890')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 54


def test_evalute_packet_min():
    data = hex_to_bin('880086C3E88112')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 7


def test_evalute_packet_max():
    data = hex_to_bin('CE00C43D881120')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 9


def test_evalute_packet_greater():
    data = hex_to_bin('F600BC2D8F')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 0


def test_evalute_packet_less():
    data = hex_to_bin('D8005AC2A8F0')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 1


def test_evalute_packet_equal():
    data = hex_to_bin('9C005AC2F8F0')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 0


def test_evalute_packet_complex():
    data = hex_to_bin('9C0141080250320F1802104A08')

    packet, _ = parse_packet(data)

    assert evaluate_packets(packet) == 1
