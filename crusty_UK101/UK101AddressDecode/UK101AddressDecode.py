from myhdl import *

def UK101AddressDecode(
    AL,
    MonitorRom,
    ACIA,
    KeyBoardPort,
    VideoMem,
    BasicRom,
    Ram
):
    """ UK101 address map decoder.
    
    Source: http://www.gifford.co.uk/~coredump/ukarch.htm
    """

    @always_comb
    def decode():
        MonitorRom.next   = 0xF800 <= AL and AL <= 0xFFFF
        ACIA.next         = 0XF000 <= AL and AL <= 0xF7FF
        KeyBoardPort.next = 0xDC00 <= AL and AL <= 0xDFFF
        VideoMem.next     = 0xD000 <= AL and AL <= 0xD3FF
        BasicRom.next     = 0xA000 <= AL and AL <= 0xBFFF
        Ram.next          = 0x0000 <= AL and AL <= 0x1FFF

    return decode
