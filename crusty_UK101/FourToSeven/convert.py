import os, glob, shutil

from myhdl import *

from FourToSeven import FourToSeven

ByteIn = Signal(intbv(0)[4:])
Enable = Signal(bool(0))
Polarity = Signal(bool(0))
SegOut = Signal(intbv(0)[7:])

for conv in (toVHDL, toVerilog):
    conv(FourToSeven,
         ByteIn,
         Enable,
         Polarity,
         SegOut)

for fn in glob.glob('*.vhd'):
    shutil.copy2(fn, 'vhdl')
    os.remove(fn)
    
for fn in glob.glob('*.v'):
    if fn[:3] == 'tb_':
        os.remove(fn)
        continue
    shutil.copy2(fn, 'verilog')
    os.remove(fn)
