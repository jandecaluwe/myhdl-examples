--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   13:38:15 02/02/2013
-- Design Name:   
-- Module Name:   C:/Documents and Settings/UK101FPGA/TestAddressDecode.vhd
-- Project Name:  UK101FPGA
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: UK101AddressDecode
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY TestAddressDecode IS
END TestAddressDecode;
 
ARCHITECTURE behavior OF TestAddressDecode IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT UK101AddressDecode
    PORT(
         AL : IN  std_logic_vector(15 downto 0);
         MonitorRom : OUT  std_logic;
         ACIA : OUT  std_logic;
         KeyBoardPort : OUT  std_logic;
         VideoMem : OUT  std_logic;
         BasicRom : OUT  std_logic;
         RAM : OUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal AL : std_logic_vector(15 downto 0) := (others => '0');

 	--Outputs
   signal MonitorRom : std_logic;
   signal ACIA : std_logic;
   signal KeyBoardPort : std_logic;
   signal VideoMem : std_logic;
   signal BasicRom : std_logic;
   signal RAM : std_logic;
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
   Signal Clk : Std_logic;
   constant clK_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: UK101AddressDecode PORT MAP (
          AL => AL,
          MonitorRom => MonitorRom,
          ACIA => ACIA,
          KeyBoardPort => KeyBoardPort,
          VideoMem => VideoMem,
          BasicRom => BasicRom,
          RAM => RAM
        );

   -- Clock process definitions
   clK_process :process
   begin
		Clk <= '0';
		wait for Clk_period/2;
		Clk <= '1';
		wait for Clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for Clk_period*10;

      -- insert stimulus here
			AL <= "0000000000000000";
			wait for Clk_period;
			AL <= "0010111111111110";
			wait for Clk_period;
			AL <= "0010111111111111";
			wait for Clk_period;
			wait for Clk_period;
			AL <= "1010000000000000";
			wait for Clk_period;
      wait;
   end process;

END;
