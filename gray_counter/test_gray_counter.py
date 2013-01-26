from myhdl import *

from gray_code import gray_code
from gray_counter import gray_counter

def bench(gray_counter, n):

    enable = Signal(bool(0))
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=0, async=True)
    gray_count = Signal(intbv(0)[n:])

    dut = gray_counter(gray_count, enable, clock, reset)

    @always(delay(10))
    def clkgen():
        clock.next = not clock

    @instance
    def stimulus():
        m = 2**n
        yield delay(1)
        reset.next = 1
        enable.next = 1
        actual = [None] * m
        for i in range(2):
            for j in range(m):
                actual[j] = int(gray_count)
                yield clock.posedge
                yield delay(1)
            expected = [int(e, 2) for e in gray_code(n)]
            # print actual, expected
            assert actual == expected
        raise StopSimulation()

    return clkgen, stimulus, dut

def check_gray_counter(gray_counter, n):
    sim = Simulation(bench(gray_counter, n))
    sim.run()

def test_gray_counter():
    for i in (4, 8, 12, 16, ):
        yield check_gray_counter, gray_counter, i


