import os

from src.text import *
from src.tiles import *

def load_rom():
    file = open("rom/goemon.gbc", "rb")
    rom = bytearray(file.read())
    file.close()
    return rom

def write_rom(rom_buffer):
    file = open("out/goemon_patched.gbc", "wb")
    file.write(rom_buffer)
    file.close()

def extract_font():
    FONT_WIDTH_TILES = 16
    FONT_HEIGHT_TILES = 21
    FONT_START_ADDRESS = 0x4C4D8
    FONT_NUM_TILES = 336
    rom = load_rom()
    tiles = extract_tiles(rom, FONT_START_ADDRESS, FONT_NUM_TILES)
    bmp = tiles_to_bmp(tiles, FONT_WIDTH_TILES, FONT_HEIGHT_TILES)
    os.makedirs("out/image", exist_ok=True)
    write_bmp("out/image/font.bmp", bmp, FONT_WIDTH_TILES, FONT_HEIGHT_TILES)
    return

def inject_font():
    FONT_START_ADDRESS = 0x4C4D8
    rom = load_rom()
    new_font = load_bmp("data/edited_font.bmp")
    inject_tiles(rom, new_font, FONT_START_ADDRESS)
    write_rom(rom)

def inject_text_test():
    rom = load_rom()
    table = load_table("data/original.tbl")
    inject_text(rom, 0x99F3E, table, "SUP RHDN!")
    write_rom(rom)
