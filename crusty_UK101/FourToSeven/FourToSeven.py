from myhdl import *

a, b, c, d, e, f, g = [2**i for i in range(7)]
ssd = [0] * 16

ssd[0x0] = a+b+c+d+e+f
ssd[0x1] = b+c          
ssd[0x2] = a+b+d+e+g    
ssd[0x3] = a+b+c+d+g     
ssd[0x4] = b+c+f+g      
ssd[0x5] = a+c+d+f+g    
ssd[0x6] = a+c+d+e+f+g
ssd[0x7] = a+b+c        
ssd[0x8] = a+b+c+d+e+f+g 
ssd[0x9] = a+b+c+d+f+g   
ssd[0xA] = a+b+c+e+f+g  
ssd[0xb] = c+d+e+f+g 
ssd[0xC] = a+d+e+f     
ssd[0xd] = b+c+d+e+g
ssd[0xE] = a+d+e+f+g   
ssd[0xF] = a+e+f+g

ssd = tuple(ssd) # make the table read-only

def FourToSeven(ByteIn, Enable, Polarity, SegOut):

    @always_comb
    def comb():
        SegBuf = intbv(0)[7:]
        if Enable == 1:
            SegBuf[:] = ssd[ByteIn]
        if Polarity == 0:
            SegBuf = ~SegBuf
        SegOut.next = SegBuf

    return comb


            

