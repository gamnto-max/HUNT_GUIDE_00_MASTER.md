`timescale 1ns / 1ps
// Banco de pruebas para el núcleo spintrónico
module HUNT_TB_02_VAL;
    reg clk;
    reg rst_n;
    reg [15:0] phase_up;
    reg [15:0] phase_down;
    wire [31:0] coherence;
    wire peuo_ok;

    HUNT_CORE_01_SPIN uut (
        .clk(clk), .rst_n(rst_n),
        .phase_vector_up(phase_up), .phase_vector_down(phase_down),
        .quantum_coherence(coherence), .peuo_active(peuo_ok)
    );

    always #5 clk = ~clk;

    initial begin
        clk = 0; rst_n = 0; phase_up = 0; phase_down = 0;
        #10 rst_n = 1;
        // Inyección de fases acopladas (Superposición perfecta)
        #10 phase_up = 16'h0100; phase_down = 16'h0100;
        #20 $finish;
    end
endmodule
