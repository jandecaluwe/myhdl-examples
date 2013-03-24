from myhdl import *

from FourToSeven import FourToSeven

def bench():

    ByteIn = Signal(intbv(0)[4:])
    Enable = Signal(bool(0))
    Polarity = Signal(bool(0))
    SegOut = Signal(intbv(0)[7:])

    dut = FourToSeven(
         ByteIn,
         Enable,
         Polarity,
         SegOut)

    @instance
    def stimulus():
        Enable.next = 0
        Polarity.next = 1
        yield delay(10)
        assert SegOut == 0
        Enable.next = 1
        for i in range(16):
            ByteIn.next = i
            yield delay(10)
            segmap = "_||_||_"
            a, b, c, d, e, f, g = [segmap[i] if SegOut[i] else ' ' for i in range(7)]
            print "%s%s%s" % (' ', a, ' ')
            print "%s%s%s" % ( f,  g,  b )
            print "%s%s%s" % ( e,  d,  c )
        raise StopSimulation()
        
    return dut, stimulus

sim = Simulation(bench())
sim.run()



