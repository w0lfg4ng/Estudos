timer:      mov     timer,#(16-7)    ;conta 7us
            setb    liga             ;liga timer

novo_tempo: jnb    TF,$              ;espera overflow
            clr    TF                ;limpa o flag para reinicializar
            mov    timer,#(16-7)     ;incrementa valor para recarregar

            jmp    novo_tempo
