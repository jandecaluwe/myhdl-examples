import glob
import shutil
import os

from myhdl import *

from gray_counter import gray_counter

def convert(gray_counter, N, target=toVHDL):
    
    enable = Signal(bool(0))
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, async=True)
    gray_count = Signal(intbv(0)[N:])

    name = gray_counter.__name__ + '_' + str(N)
    target.name = name
    target(gray_counter, gray_count, enable, clock, reset)

cwd = os.getcwd()

os.chdir(cwd)
os.chdir('vhdl')
for i in (4, 8, 12, 16, 20, 24, 28, 32):
    convert(gray_counter, i, toVHDL)

os.chdir(cwd)
os.chdir('verilog')
for i in (4, 8, 12, 16, 20, 24, 28, 32):
    convert(gray_counter, i, toVerilog)

