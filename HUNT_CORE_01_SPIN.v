`timescale 1ns / 1ps
// Módulo de procesamiento atómico de espín
module HUNT_CORE_01_SPIN (
    input  wire        clk,
    input  wire        rst_n,
    input  wire [15:0] phase_vector_up,
    input  wire [15:0] phase_vector_down,
    output reg  [31:0] quantum_coherence,
    output reg         peuo_active
);
    localparam [31:0] PEUO_TARGET = 32'h00010000; // Coherencia 1.0 (Q16.16)

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            quantum_coherence <= 32'b0;
            peuo_active       <= 1'b0;
        end else begin
            quantum_coherence <= (phase_vector_up * phase_vector_down);
            peuo_active       <= (quantum_coherence >= PEUO_TARGET) ? 1'b1 : 1'b0;
        end
    end
endmodule
