# string-concat-loop snippets for paho.mqtt.python

# File: /root/ecooptimizer/paho.mqtt.python/src/paho/mqtt/properties.py
# Occurrences: Lines 299-300 (2 instances)

for name in self.names.keys():
    compressedName = name.replace(' ', '')
    if hasattr(self, compressedName):
        if not first:
            buffer += ", "
        buffer += f"{compressedName} : {getattr(self, compressedName)}"
        first = False

# ==================================================
