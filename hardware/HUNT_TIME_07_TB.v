timescale 1as / 1as

module HUNT_TIME_07_TB;

    reg clk_quantum;
    reg rst_n;
    reg [15:0] target_phase_shift;
    reg [15:0] active_spin_delay;

    wire [31:0] transition_speed;
    wire timing_coherence;
    wire violation_alert;

    // Instancia del analizador temporal bajo prueba
    HUNT_TIME_07_ATTO uut (
        .clk_quantum(clk_quantum),
        .rst_n(rst_n),
        .target_phase_shift(target_phase_shift),
        .active_spin_delay(active_spin_delay),
        .transition_speed(transition_speed),
        .timing_coherence(timing_coherence),
        .violation_alert(violation_alert)
    );

    // Generación del reloj cuántico de alta frecuencia
    always #5 clk_quantum = ~clk_quantum;

    initial begin
        clk_quantum = 0;
        rst_n = 0;
        target_phase_shift = 0;
        active_spin_delay = 0;

        #20 rst_n = 1;

        // Caso de Prueba 1: Transición ideal bajo el Teorema de Hunt (Fase perfecta)
        #20;
        target_phase_shift = 16'd2;
        active_spin_delay  = 16'd150; // 150 attosegundos de retardo natural

        // Caso de Prueba 2: Simulación de intrusión resistiva clásica (Falla en el Silicio)
        #20;
        target_phase_shift = 16'd5;
        active_spin_delay  = 16'd200; // Provoca un retraso fuera de los límites del PEUO

        #40 $finish;
    end

endmodule
