from myhdl import *

from stack_ref import StackObject, ONES
from stack_myhdl import Stack

def bench():

    ref = StackObject()

    ToSPieceOut = Signal(intbv(0)[6:])
    ToSMaskOut = Signal(intbv(ONES)[16:]) 
    PieceIn = Signal(intbv(0)[6:])
    MaskIn = Signal(intbv(0)[16:])
    MaskReset = Signal(intbv(0)[16:])
    Enable = Signal(bool(0))
    PushPop = Signal(bool(0))
    Reset = ResetSignal(bool(0), active=1, async=False)
    Clk = Signal(bool(0))
    
    dut = Stack(
        ToSPieceOut, 
        ToSMaskOut, 
        PieceIn, 
        MaskIn, 
        MaskReset, 
        Enable, 
        PushPop, 
        Reset,
        Clk,
    )

    @always(delay(10))
    def clkgen():
        Clk.next = not Clk

    @instance
    def stimulus():
        Reset.next = 1
        ref.reset()
        yield Clk.negedge
        Reset.next = 0
        yield Clk.negedge
        ref.push(5, 0xabcd)
        PieceIn.next = 5
        MaskIn.next = 0xabcd 
        Enable.next = 1
        PushPop.next = 1
        yield Clk.negedge
        Enable.next = 0
        PushPop.next = 0
        ref.mask_reset(0x9999)
        MaskReset.next = 0x9999
        yield Clk.negedge
        MaskReset.next = 0x0
        yield Clk.negedge
        for i in range(5):
            yield Clk.negedge
            ref.push(i, 0xbeef-i)
            PieceIn.next = i
            MaskIn.next = 0xbeef-i
            Enable.next = 1
            PushPop.next = 1
        yield Clk.negedge
        Enable.next = 0
        yield Clk.negedge  
        for i in range(5):
            yield Clk.negedge
            ref.pop()
            Enable.next = 1
            PushPop.next = 0
        yield Clk.negedge
        Enable.next = 0
        yield Clk.negedge
        raise StopSimulation()

    @instance
    def check():
        while True:
            yield Clk.posedge
            yield delay(1)
	    print ref.ToSPiece, ToSPieceOut 
            print ref.ToSMask, ToSMaskOut
            assert ref.ToSPiece == ToSPieceOut
            assert ref.ToSMask == ToSMaskOut
 
    return dut, clkgen, stimulus, check


sim = Simulation(traceSignals(bench))
sim.run()

