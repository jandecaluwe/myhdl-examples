from myhdl import *

from UK101AddressDecode import UK101AddressDecode

def bench():

    AL = Signal(intbv(0)[16:])
    MonitorRom = Signal(bool(0))
    ACIA = Signal(bool(0))
    KeyBoardPort = Signal(bool(0))
    VideoMem = Signal(bool(0))
    BasicRom = Signal(bool(0))
    Ram = Signal(bool(0))

    dut = UK101AddressDecode( 
        AL, 
        MonitorRom, 
        ACIA, 
        KeyBoardPort,
        VideoMem,
        BasicRom, 
        Ram)

    @instance
    def stimulus():
        for i in range(0, 2**16):
            AL.next = i
            yield delay(10)
        raise StopSimulation()
        
    return dut, stimulus

sim = Simulation(traceSignals(bench))
sim.run()



