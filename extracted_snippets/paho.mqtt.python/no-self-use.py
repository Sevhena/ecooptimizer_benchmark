# no-self-use snippets for paho.mqtt.python

# File: /root/ecooptimizer/paho.mqtt.python/src/paho/mqtt/client.py
# Line: 3345

def _pack_remaining_length(
    self, packet: bytearray, remaining_length: int

# ==================================================
# Line: 3362

def _pack_str16(self, packet: bytearray, data: bytes | str) -> None:
    data = _force_bytes(data)
    packet.extend(struct.pack("!H", len(data)))
    packet.extend(data)


# ==================================================
# Line: 4819

def _create_frame(
    self, opcode: int, data: bytearray, do_masking: int = 1

# ==================================================
