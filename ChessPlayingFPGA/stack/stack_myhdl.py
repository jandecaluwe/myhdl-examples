from myhdl import *

def Stack(
    ToSPieceOut, 
    ToSMaskOut, 
    PieceIn, 
    MaskIn, 
    MaskReset, 
    Enable, 
    PushPop, 
    Reset,
    Clk,
    DEPTH = 6
):
    """Stack module in MyHDL

    This the MyHDL RTL code for the Stack module. It
    can be converted to Verilog/VHDL and synthesized.
    """

    ONES = 2**16-1

    ToSPiece = Signal(intbv(0)[6:])
    ToSMask = Signal(intbv(ONES)[16:])
    Stack = [Signal(intbv(0)[22:]) for i in range(DEPTH-1)]
    StackWriteData = Signal(intbv(0)[22:])
    StackReadData = Signal(intbv(0)[22:])
    StackWrite = Signal(bool(0))
    Pointer = Signal(intbv(0, min=0, max=DEPTH-1))
    WritePointer = Signal(intbv(0, min=0, max=DEPTH-1))
    NrItems = Signal(intbv(0, min=0, max=DEPTH+1))
  
    @always_seq(Clk.posedge, reset=Reset)
    def control():
        StackWrite.next = False
        if MaskReset != 0:
            ToSMask.next = ToSMask & ~MaskReset
        elif PushPop and Enable: # push
            ToSPiece.next = PieceIn
            ToSMask.next = MaskIn  
            NrItems.next = NrItems + 1
            if NrItems > 0:
                StackWriteData.next = concat(ToSPiece, ToSMask)
                StackWrite.next = True
                Pointer.next = WritePointer
                if WritePointer < DEPTH-2:
                    WritePointer.next = WritePointer + 1 
        elif not PushPop and Enable: # pop
            ToSPiece.next = StackReadData[22:16]
            ToSMask.next = StackReadData[16:]
            NrItems.next = NrItems - 1
            WritePointer.next = Pointer
            if Pointer > 0:
                Pointer.next = Pointer - 1 
                    
    @always_seq(Clk.posedge, reset=None)
    def write_stack():
        if StackWrite:
            Stack[Pointer].next = StackWriteData
 
    @always_comb
    def read_stack():
        StackReadData.next = Stack[Pointer]

    @always_comb
    def output():
         ToSPieceOut.next = ToSPiece
         ToSMaskOut.next = ToSMask 
               
    return control, write_stack, read_stack, output
