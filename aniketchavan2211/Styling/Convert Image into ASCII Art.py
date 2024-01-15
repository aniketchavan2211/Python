#!/usr/bin/env python

#import pywhatkit as kit
#kit.image_to_ascii_art("file_path", 'filename.txt')

import ascii_magic

output = ascii_magic.from_image_file("file_path", columns = 300, char = '#')

ascii_magic.to_terminal(output)
