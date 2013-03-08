import os, glob, shutil

from myhdl import *

from UK101AddressDecode import UK101AddressDecode

AL = Signal(intbv(0)[16:])
MonitorRom = Signal(bool(0))
ACIA = Signal(bool(0))
KeyBoardPort = Signal(bool(0))
VideoMem = Signal(bool(0))
BasicRom = Signal(bool(0))
Ram = Signal(bool(0))

for conv in (toVHDL, toVerilog):
    conv(UK101AddressDecode, 
         AL, 
         MonitorRom, 
         ACIA, 
         KeyBoardPort,
         VideoMem,
         BasicRom, 
         Ram)

for fn in glob.glob('*.vhd'):
    shutil.copy2(fn, 'vhdl')
    os.remove(fn)
    
for fn in glob.glob('*.v'):
    if fn[:3] == 'tb_':
        os.remove(fn)
        continue
    shutil.copy2(fn, 'verilog')
    os.remove(fn)
