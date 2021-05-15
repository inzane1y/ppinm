# proc_part.py

P_DFLT = 'dflt'
P_REAL = 'real'
P_IMAG = 'imag'

def part(func, part, *args, **kwargs):
    switch = {
        P_DFLT: func(*args, **kwargs),
        P_REAL: func(*args, **kwargs).real,
        P_IMAG: func(*args, **kwargs).imag,
    }

    return switch.get(part, 'Unknown part: ' + str(part))
