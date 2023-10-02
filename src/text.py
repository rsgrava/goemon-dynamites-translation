def load_table(file_name):
    table = {}
    file = open(file_name, 'r')
    text = file.read()
    for line in text.splitlines():
        line_split = line.split('=')
        table[int(line_split[0], 16)] = line_split[1]
    return table

def inject_text(rom, start_address, table, text):
    i = 0
    for character in list(text):
        code = list(table.keys())[list(table.values()).index(character)]
        if code > 255:
            code = code.to_bytes(2, "big")
            rom[start_address + i] = code[0]
            rom[start_address + i + 1] = code[1]
            i = i + 2
        else:
            code = code.to_bytes(1, "big")
            rom[start_address + i] = code[0]
            i = i + 1