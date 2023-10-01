import os

from src.tiles import *

def load_rom():
    file = open("rom/goemon.gbc", "rb")
    rom = bytearray(file.read())
    file.close()
    return rom

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
