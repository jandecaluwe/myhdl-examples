gray_counter
============

This is the code from [this essay](http://www.jandecaluwe.com/hdldesign/thinking-software-rtl.html).

It illustrates how to design at the RTL level by starting from an algorithm. The design problem is a gray counter. The algorithm goes as follows:

Given an n-bit Gray code word G = { g[n-1] g[n-2] g[n-3] ... g[0] }, with g[k] representing the individual bits of the word:

* Construct a new word W = { 1 g[n-3] ... g[0] p }, with p being the even parity bit of G.
* Starting from the LSB at position 0, look for the first 1 in W
* Toggle the bit in G at the corresponding position.
