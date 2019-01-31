import re

pattern = re.compile(r"(\d+)\[([a-z]+)\]")

def solve(compressed_string):
    if '[' in compressed_string:
        return decompress(compressed_string)
    return compressed_string

def decompress(string):
    number, piece = pattern.search(string).groups()
    string = re.sub(pattern, int(number) * piece, string, 1)
    return solve(string)
    

