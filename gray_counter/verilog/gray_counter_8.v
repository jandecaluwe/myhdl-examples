// File: gray_counter_8.v
// Generated by MyHDL 0.8dev
// Date: Sun Feb  3 17:16:42 2013


`timescale 1ns/10ps

module gray_counter_8 (
    gray_count,
    enable,
    clock,
    reset
);


output [7:0] gray_count;
wire [7:0] gray_count;
input enable;
input clock;
input reset;

reg even;
reg [7:0] gray;





always @(posedge clock, posedge reset) begin: GRAY_COUNTER_8_SEQ
    integer i;
    reg found;
    reg [8-1:0] word;
    if (reset == 1) begin
        even <= 1;
        gray <= 0;
    end
    else begin
        word = {1'b1, gray[(8 - 2)-1:0], even};
        if (enable) begin
            found = 1'b0;
            for (i=0; i<8; i=i+1) begin
                if (((word[i] == 1) && (!found))) begin
                    gray[i] <= (!gray[i]);
                    found = 1'b1;
                end
            end
            even <= (!even);
        end
    end
end



assign gray_count = gray;

endmodule
