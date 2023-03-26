from sympy import *

def movimento_uniforme(res = "velocidade",velocidade = 1,espaco = 1,tempo=1,SI = "km/h"):
    if SI == "km/h":
        if res == "velocidade": #para a resposta ser velocidade
            ΔS,Δt,vm = symbols('ΔS,Δt,v_m')
            print('')
            display(Eq(vm,ΔS/Δt))
            print('')

            d = symbols(f'{espaco}km')
            t = symbols(f'{tempo}h')
            display(Eq(vm,d/t))
            print('')

            si = symbols('km/h')
            display(Eq(vm,(espaco/tempo)*si))
            print('')


        if res == "tempo": #para a resposta ser tempo
            ΔS,Δt,vm = symbols('ΔS,Δt,v_m')
            print('')
            display(Eq(Δt,ΔS/vm))


            d = symbols(f'{espaco}km')
            v = symbols(f'{velocidade}km/h')
            print('')
            display(Eq(Δt,d/v))

            si = symbols('h')
            print('')
            display(Eq(Δt,(espaco/velocidade)*si))

        if res == "distancia": #para a resposta ser distancia
            ΔS,Δt,vm = symbols('ΔS,Δt,v_m')
            print('')
            display(Eq(ΔS,Δt*vm))


            t = symbols(f'{tempo}h')
            v = symbols(f'{velocidade}km/h')
            print('')
            display(Eq(ΔS,v*t))

            si = symbols('km')
            print('')
            display(Eq(ΔS,velocidade*tempo*si))
    
    #mudando as grandezas para metros por segundos
    if SI == "m/s":
        if res == 'velocidade':
            ΔS,Δt,vm = symbols('ΔS,Δt,v_m')
            print('')
            display(Eq(vm,ΔS/Δt))

            d = symbols(f'{espaco}m')
            t = symbols(f'{tempo}s')
            print('')
            display(Eq(vm,d/t))

            si = symbols('m/s')
            print('')
            display(Eq(vm,(espaco/tempo)*si))
            
        if res == "tempo": #para a resposta ser tempo
            ΔS,Δt,vm = symbols('ΔS,Δt,v_m')
            print('')
            display(Eq(Δt,ΔS/vm))


            d = symbols(f'{espaco}m')
            v = symbols(f'{velocidade}m/s')
            print('')
            display(Eq(Δt,d/v))

            si = symbols('s')
            print('')
            display(Eq(Δt,(espaco/velocidade)*si))
            
       
        if res == "distancia": #para a resposta ser distancia
            ΔS,Δt,vm = symbols('ΔS,Δt,v_m')
            print('')
            display(Eq(ΔS,Δt*vm))


            t = symbols(f'{tempo}s')
            v = symbols(f'{velocidade}m/s')
            print('')
            display(Eq(ΔS,v*t))

            si = symbols('m')
            print('')
            display(Eq(ΔS,velocidade*tempo*si))
