# cached-repeated-calls snippets for paho.mqtt.python

# File: /root/ecooptimizer/paho.mqtt.python/src/paho/mqtt/client.py
# Line: 442

listensock = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

# ==================================================
# Line: 449

sock1 = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

# ==================================================
# Occurrences: Lines 813-814 (2 instances)

self._last_msg_in = time_func()

# ==================================================
# Occurrences: Lines 844-850 (7 instances)

self._in_callback_mutex = threading.Lock()

# ==================================================
# Occurrences: Lines 1580-1581 (2 instances)

self._last_msg_in = time_func()

# ==================================================
# Line: 3070

command = self._sock_recv(1)

# ==================================================
# Line: 3092

byte = self._sock_recv(1)

# ==================================================
# Line: 3137

self._last_msg_in = time_func()

# ==================================================
# Line: 3157

self._last_msg_in = time_func()

# ==================================================
# Line: 3224

self._last_msg_out = time_func()

# ==================================================
# Line: 3245

self._last_msg_out = time_func()

# ==================================================
# Line: 3960

rc = self._send_publish(
    m.mid,
    m.topic.encode('utf-8'),
    m.payload,
    m.qos,
    m.retain,
    m.dup,
    properties=m.properties
)

# ==================================================
# Line: 3976

rc = self._send_publish(
    m.mid,
    m.topic.encode('utf-8'),
    m.payload,
    m.qos,
    m.retain,
    m.dup,
    properties=m.properties
)

# ==================================================
# Line: 3992

rc = self._send_publish(
    m.mid,
    m.topic.encode('utf-8'),
    m.payload,
    m.qos,
    m.retain,
    m.dup,
    properties=m.properties
)

# ==================================================
# Line: 4101

(topic, packet) = struct.unpack(pack_format, packet)

# ==================================================
# Line: 4119

(message.mid, packet) = struct.unpack(pack_format, packet)

# ==================================================
# Line: 4529

now = time_func()

# ==================================================
# Line: 4547

remaining = target_time - time_func()

# ==================================================
# Occurrences: Lines 4706-4707 (2 instances)

self._sendbuffer = bytearray()

# ==================================================
# Occurrences: Lines 4716-4717 (2 instances)

self._sendbuffer = bytearray()

# ==================================================
# Line: 4807

self._readbuffer = bytearray()

# ==================================================
# Line: 4816

self._readbuffer = bytearray()

# ==================================================
# Occurrences: Lines 4883-4884 (2 instances)

header1 = self._buffered_read(1)

# ==================================================
# Occurrences: Lines 4924-4928 (2 instances)

payload = bytearray()

# ==================================================
# File: /root/ecooptimizer/paho.mqtt.python/src/paho/mqtt/properties.py
# Occurrences: Lines 383-385 (2 instances)

value, valuelen = readUTF(buffer, propslen)

# ==================================================
# Occurrences: Lines 402-407 (2 instances)

propslen, VBIlen = VariableByteIntegers.decode(buffer)

# ==================================================
