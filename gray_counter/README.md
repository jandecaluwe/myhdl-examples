gray_counter
============

This is the code from [this blog post](http://www.programmableplanet.com/author.asp?section_id=2438&doc_id=258486).

Given an n-bit Gray code word G = { g[n-1] g[n-2] g[n-3] ... g[0] }, with g[k] representing the individual bits of the word:

* Construct a new word W = { 1 g[n-3] ... g[0] p }, with 'p' being the even parity bit of G.
* Starting from the LSB at position 0, look for the first 1 in W
* Toggle the bit in G at the corresponding position.
