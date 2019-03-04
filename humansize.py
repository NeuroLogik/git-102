SUFFIXES = ['KB','MB','GB','TB','PB','EB','ZB','YB']

def approximate_size(size):
    multiple = 1024
    for suffix in SUFFIXES:
        size / multiple
        if size < multiple:
            return f'{size} {suffix}'
#controllo se il numero è troppo grande
    raise ValueError('number too large')