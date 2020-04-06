import sys
print(sys.path)

# """this is a dictionary in python"""
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# """def instead of function in python"""
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    # """colon and then indent the code, no {}"""
    if size <0:
        raise ValueError('number must be non-negative')

    # """ternary condition in python"""
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=False))
    print(approximate_size(-16384))
        # """equivalent of console.log"""