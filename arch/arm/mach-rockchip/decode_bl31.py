#!/usr/bin/env python3
#
# Copyright (C) 2020 Rockchip Electronics Co., Ltd
#
# SPDX-License-Identifier:     GPL-2.0+
#
"""
A script to decode bl31.elf to binary
"""

# pip install pyelftools
from elftools.elf.elffile import ELFFile

ELF_SEG_P_TYPE='p_type'
ELF_SEG_P_PADDR='p_paddr'

def generate_atf_binary():
    bl31 = ELFFile(open("./bl31.elf", "rb"))
    num = bl31.num_segments()
    for i in range(num):
        seg = bl31.get_segment(i)
        if ('PT_LOAD' == seg.__getitem__(ELF_SEG_P_TYPE)):
            paddr = seg.__getitem__(ELF_SEG_P_PADDR)
            file_name = 'bl31_0x%08x.bin' % paddr
            with open(file_name, "wb") as atf:
                atf.write(seg.data());

def main():
    generate_atf_binary();

if __name__ == "__main__":
    main()
