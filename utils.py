def calculate_crc(payload):
    """
    Calculate the CRC-16-CCITT checksum of the given payload.
    :param payload: Payload to calculate checksum for
    :return: CRC-16-CCITT checksum
    """
    crc = 0xFFFF
    poly = 0x1021

    for byte in bytearray(payload.encode("utf-8")):
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFFFF  # Ensure CRC remains within 16 bits

    return f"{crc:04X}"