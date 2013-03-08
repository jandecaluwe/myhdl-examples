----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    15:12:28 02/01/2013 
-- Design Name: 
-- Module Name:    UK101AddressDecode - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity UK101AddressDecode is
    Port ( AL : in  STD_LOGIC_VECTOR (15 downto 0);-- Address bus to decode
           MonitorRom : out  STD_LOGIC;-- decoded output 
           ACIA : out  STD_LOGIC;-- decoded output
           KeyBoardPort : out  STD_LOGIC;--decoded output
           VideoMem : out  STD_LOGIC;--decoded output
           BasicRom : out  STD_LOGIC;--decoded output
           RAM : out  STD_LOGIC);--decoded output
end UK101AddressDecode;

architecture Behavioral of UK101AddressDecode is

begin
Process (AL )
Begin					--FFFF                          FF80
		If ((AL <= "1111111111111111") and (AL >= "1111111110000000") ) Then-- chech for the valid address range
			MonitorRom <= '1'; -- set the output state
		Else 
			MonitorRom <= '0';
		End If;		--F7FF                           F000
		If ((AL <= "1111011111111111") and (AL >= "1111000000000000") ) Then-- chech for the valid address range
			ACIA <= '1';-- set the output state
		Else 
			ACIA <= '0';
		End If;		--DFFF                          DC00
		If ((AL <= "1101111111111111") and (AL >= "1101110000000000") ) Then-- chech for the valid address range
			KeyBoardPort <= '1';-- set the output state
		Else 
			KeyBoardPort <= '0';
		End If;		--D3FF                           D000
		If ((AL <= "1101001111111111") and (AL >= "1101000000000000") ) Then-- chech for the valid address range
			VideoMem <= '1';-- set the output state
		Else 
			VideoMem <= '0';
		End If;		--BFFF                           A000
		If ((AL <= "1011111111111111") and (AL >= "1010000000000000") ) Then-- chech for the valid address range
			BasicRom <= '1';-- set the output state
		Else 
			BasicRom <= '0';
		End If;		--2FFF                           0000
		If ((AL <= "0010111111111111") and (AL >= "0000000000000000") ) Then-- chech for the valid address range
			Ram <= '1';-- set the output state
		Else 
			Ram <= '0';
		End If;
End Process;

end Behavioral;

