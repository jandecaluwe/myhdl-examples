from myhdl import *

ONES = 2**16-1

class StackObject(object):

    def __init__(self, depth=6):
        self.depth = depth
        self.ToSPiece = intbv(0)[6:]
        self.ToSMask = intbv(ONES)[16:]
        self.stack = []
        self.nritems = 0

    def reset(self):
        self.ToSPiece[:] = 0  
        self.ToSMask[:] = ONES 
        self.stack[:] = []
        self.nritems = 0

    def mask_reset(self, mask):
        self.ToSMask &= mask

    def push(self, PieceIn, MaskIn):
        if self.nritems == self.depth: 
            raise IndexError('Overflow')
        if self.nritems > 0:
            # push values on the stack as immutable ints
            self.stack.append((int(self.ToSPiece), int(self.ToSMask)))
        self.ToSPiece[:] = PieceIn
        self.ToSMask[:] = MaskIn
        self.nritems += 1

    def pop(self):
        if self.nritems == 0: 
            raise IndexError('Underflow')
        self.ToSPiece[:], self.ToSMask[:] = self.stack.pop() 
        self.nritems -= 1
         
