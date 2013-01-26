// File: gray_counter_4.v
// Generated by MyHDL 0.8dev
// Date: Sat Jan 26 17:51:19 2013


`timescale 1ns/10ps

module gray_counter_4 (
    gray_count,
    enable,
    clock,
    reset
);


output [3:0] gray_count;
wire [3:0] gray_count;
input enable;
input clock;
input reset;

reg even;
reg [3:0] gray;





always @(posedge clock, posedge reset) begin: GRAY_COUNTER_4_SEQ
    integer i;
    reg [4-1:0] word;
    reg toggled;
    if (reset == 1) begin
        even <= 1;
        gray <= 0;
    end
    else begin
        word = 4'h0;
        word = {1'b1, gray[(4 - 2)-1:0], even};
        if (enable) begin
            toggled = 1'b0;
            for (i=0; i<4; i=i+1) begin
                if (((word[i] == 1) && (!toggled))) begin
                    gray[i] <= (!gray[i]);
                    toggled = 1'b1;
                end
            end
            even <= (!even);
        end
    end
end



assign gray_count = gray;

endmodule
