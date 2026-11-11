def parse_port(s):
    p = int(s)
    if p < 1 or p > 65535:
        raise ValueError("port out of range")
    return p
