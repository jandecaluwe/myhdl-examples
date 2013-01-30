from myhdl import *

def gray_counter(gray_count, enable, clock, reset):

    n = len(gray_count)
    gray = Signal(intbv(0)[n:])
    even = Signal(bool(1))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        word = concat('1', gray[n-2:], even)
        if enable:
            toggled = False
            for i in range(n):
                if word[i] == 1 and not toggled:
                    gray.next[i] = not gray[i]
                    toggled = True
            even.next = not even

    @always_comb
    def alias():
        gray_count.next = gray
               
    return seq, alias
