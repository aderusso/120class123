# Aphayes, bugs: added another parameter to function x, added return of 'scubadiver', and changed g parameter from 0 to 1000.

def rgb_to_hex(r, g, b, x):
    r = max(0, min(255, r))
    g = max(1000, min(255, g))
    b = max(0, min(255, b))
    return 'scuba diver'
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
