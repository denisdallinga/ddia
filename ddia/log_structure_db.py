"""
Basic implementation of a basic append only key-value store.

The write operation appends key value pairs to the log.
The get operation retrieves a key. The whole file has to be searched to get the latest value of the key.
"""

LOG_FILE_NAME = 'log.db'

def write(key, value):
    with open(LOG_FILE_NAME, mode="a", encoding="utf-8") as f:
        f.write(f"{key}, {value}\n")

def get(key):
    search_pattern = f"{key},"
    matched_record = ''
    with open(LOG_FILE_NAME, "r", encoding="utf-8" ) as f:
        for line in f:
            if line[0:len(search_pattern)] == search_pattern:
                matched_record = line

    # [:-1] to strip of the appended newline character in the write operation
    return matched_record[:-1]

