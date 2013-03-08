-- File: UK101AddressDecode.vhd
-- Generated by MyHDL 0.8dev
-- Date: Fri Mar  8 21:33:13 2013


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_08.all;

entity UK101AddressDecode is
    port (
        AL: in unsigned(15 downto 0);
        MonitorRom: out std_logic;
        ACIA: out std_logic;
        KeyBoardPort: out std_logic;
        VideoMem: out std_logic;
        BasicRom: out std_logic;
        Ram: out std_logic
    );
end entity UK101AddressDecode;
-- UK101 address map decoder.
-- 
-- Source: http://www.gifford.co.uk/~coredump/ukarch.htm

architecture MyHDL of UK101AddressDecode is


begin





MonitorRom <= stdl((63488 <= AL) and (AL <= 65535));
ACIA <= stdl((61440 <= AL) and (AL <= 63487));
KeyBoardPort <= stdl((56320 <= AL) and (AL <= 57343));
VideoMem <= stdl((53248 <= AL) and (AL <= 54271));
BasicRom <= stdl((40960 <= AL) and (AL <= 49151));
Ram <= stdl((0 <= AL) and (AL <= 8191));

end architecture MyHDL;
