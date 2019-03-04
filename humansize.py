SUFFIXES = ['KB','MB','GB','TB','PB','EB','ZB','YB']

def approximate_size(size):
    """Convert a file size to human-readable from.
    Keyword arguments:
    size -- file size in bytes

    Returns : string
    """
    multiple = 1024
    for suffix in SUFFIXES:
        size / multiple
        if size < multiple:
            return f'{size} {suffix}'
#controllo se il numero è troppo grande
    raise ValueError('number too large')