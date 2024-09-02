;CODE BY M0RCEG0 P0CILGA

;TEMPORIZADOR SEM INICIALIZADOR DE TIMER


timer:      mov     timer,#(16-7)    ;conta 7us
            setb    liga             ;liga timer

novo_tempo: jnb    TF,$              ;espera overflow
            clr    TF                ;limpa o flag para reinicializar
            mov    timer,#(16-7)     ;incrementa valor para recarregar

            jmp    novo_tempo

;TEMPORIZADOR SEM INICIALIZADOR DE TIMER

timer:            mov            TL0,#18H            ;inicializa timer low
                  mov            TH0,#63h            ;inicializa timer low
                  setb           TR0                 ;liga o timer
denovo:           jb             TF0,$               
                  clr            TF0
                  mov            TH0,#(256-156)

                  jmp            denovo            
