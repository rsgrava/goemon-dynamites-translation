DEFAULT_PALETTE = [ b'\x00\x00\x00', b'\x52\x52\x52', b'\xA5\xA5\xA5', b'\xFF\xFF\xFF']

def extract_tiles(rom_buffer, start_address, num_tiles):
    tiles = rom_buffer[start_address:start_address + 16 * num_tiles]
    return tiles

def tiles_to_bmp(tile_buffer, width_tiles, height_tiles, palette=DEFAULT_PALETTE):
    bitmap_buffer = bytearray(0)
    for i in range(height_tiles - 1, -1, -1):
        for j in range(7, -1, -1):
            for k in range(0, width_tiles):
                line = tile_buffer[(width_tiles * i + k) * 16 + 2 * j:(width_tiles * i + k) * 16 + 2 * (j + 1)]
                byte1 = line[0]
                byte2 = line[1]
                for l in range (7, 0, -1):
                    pixel = ((byte2 >> (l - 1)) & 0x02) | ((byte1 >> l) & 0x01)
                    bitmap_buffer += palette[pixel]
                pixel = ((byte2 << 1) & 0x02) | (byte1 & 0x01)
                bitmap_buffer += palette[pixel]
    return bitmap_buffer

def write_bmp(file_name, bitmap_buffer, width_tiles, height_tiles):
    file = open(file_name, "wb")
    width = 8 * width_tiles
    height = 8 * height_tiles
    raw_size = width * height * 3
    file_size = raw_size + 54

    #BITMAPFILEHEADER
    file.write(b'\x42\x4D')                                     #magic numbers
    file.write(file_size.to_bytes(4, "little"))                 #file size
    file.write(b'\x00\x00\x00\x00')                             #reserved
    file.write(b'\x36\x00\x00\x00')                             #starting address

    #BITMAPINFOHEADER
    file.write(b'\x28\x00\x00\x00')                             #size of BITMAPINFOHEADER
    file.write(width.to_bytes(4, "little"))                     #width
    file.write(height.to_bytes(4, "little"))                    #height
    file.write(b'\x01\x00')                                     #number of color planes (must be 1)
    file.write(b'\x18\x00')                                     #number of bits per pixel
    file.write(b'\x00\x00\x00\x00')                             #compression method
    file.write(raw_size.to_bytes(4, "little"))                  #raw bitmap data size
    file.write(b'\x12\x0B\x00\x00')                             #horizontal resolution
    file.write(b'\x12\x0B\x00\x00')                             #vertical resolution
    file.write(b'\x00\x00\x00\x00')                             #number of colors in palette
    file.write(b'\x00\x00\x00\x00')                             #number of important colors used

    file.write(bitmap_buffer)
    return

