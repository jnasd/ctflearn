#!/bin/sh

#compile, link for adoni.asm

nasm -f elf64 -o adoni.o adoni.asm
ld -o adoni adoni.o
./adoni
