"""
Basic implementation of a basic append only key-value store.

The write operation appends key value pairs to the log.
The get operation retrieves a key. The whole file has to be searched to get the latest value of the key.
"""

LOG_FILE_NAME = 'binlog.db'
DEFAULT_ENCODING = 'utf-8'

HASH_INDEX = {}

def write(key, value):
    with open(LOG_FILE_NAME, mode="ab") as f:
        start = f.tell()
        f.write(f"{key}, {value}".encode(DEFAULT_ENCODING))
        end = f.tell()
        HASH_INDEX[key] = f"{start},{end}"

    print(HASH_INDEX)

def get(key):
    if key in HASH_INDEX:
        with open(LOG_FILE_NAME, "rb") as f:
            start, end = HASH_INDEX[key].split(",")
            f.seek(int(start))
            return f.read(int(end) - int(start)).decode()

    return ""

