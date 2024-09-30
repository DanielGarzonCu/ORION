import random
from Equipos.Barcelona import *
from Equipos.Real_madri import *
from Equipos.Barcelona import *
from Equipos.Real_madri import *
from Equipos.Ac_milan import *
from Equipos.Bayern_munich import *
from Equipos.Inter_milan import *
from Equipos.Liverpool import *
from Equipos.Man_city import *
from Equipos.Psg import *
from Equipos.Aston_villa import *
from Equipos.Estadios import *
from Equipos.Balon import balon
from Equipos.palabras import *

def elegir_equipo(jugador: str) -> dict:
    """
    Función para elegir el equipo de fútbol.
    
    Args:
    jugador (str): El nombre del jugador que elige el equipo.
    
    Returns:
    dict: Un diccionario con la información del equipo elegido.
    """
    if jugador == "Jugador 1":
        jugador_word = jugador_1_word
    if jugador == "Jugador 2":
        jugador_word = jugador_2_word

    while True:
        try:
            for a in range(len(barca_word)):
                print(barca_word[a])
            for b in range(len(real_madrid_word)):
                print(real_madrid_word[b])
            for c in range(len(bayern_munich_word)):
                print(bayern_munich_word[c])
            for d in range(len(inter_milan_word)):
                print(inter_milan_word[d])
            for e in range(len(psg_word)):
                print(psg_word[e])
            for f in range(len(liverpool_word)):
                print(liverpool_word[f])
            for g in range(len(ac_milan_word)):
                print(ac_milan_word[g])
            for h in range(len(manchester_city_word)):
                print(manchester_city_word[h])
            for i in range(len(aston_villa_word)):
                print(aston_villa_word[i])
            for z in range(len(jugador_word)):
                print(jugador_word[z])
            for x in range(len(cual_equipo_desea_escoger)):
                print(cual_equipo_desea_escoger[x])
            seleccion = int(input(f"{jugador}, ¿Cuál equipo desea escoger?: "))
            if 1 <= seleccion <= 9:
                break
            else:
                for ee in range(len(error_escoja_nuevo)):
                    print(error_escoja_nuevo[ee]) 
                print("ERROR, escoja nuevamente.")
        except ValueError:
            for ei in range(len(entrada_invalida_ingresa_valores_dentro_del_rango)):
                print(entrada_invalida_ingresa_valores_dentro_del_rango[ei])
            print("Entrada no válida. Por favor, ingrese un número.")
    
    equipo_seleccionado = teams.get(seleccion)
    if equipo_seleccionado:
        print("Escudo del equipo:")
        for es in range(len(escudo_equipo_word)):
            print(escudo_equipo_word[es])
        for linea in equipo_seleccionado["escudo"]:
            print(linea)
    
    jugadores = equipo_seleccionado["jugadores"]
    ataque = equipo_seleccionado["ataque"]
    defensa = equipo_seleccionado["defensa"]
    costo = equipo_seleccionado["costo"]
    nombre = equipo_seleccionado["nombre"]
    arco = equipo_seleccionado["arco"]
    estadio = equipo_seleccionado["estadio"]

    return jugadores, ataque, defensa, costo, nombre, arco, estadio

def elegir_modo_juego() -> int:
    """
    Función para elegir el modo de juego.
    
    Returns:
    int: El número de rondas del juego.
    """
    
    while True:
        try:
            for mm in range(len(escoger_modo_de_juego_word)):
                print(escoger_modo_de_juego_word[mm])
            for rr in range(len(rondas_words)):
                print(rondas_words[rr])
            modo = int(input("Escoja un modo de juego (1, 2, 3): "))
            if 1 <= modo <= 3:
                rondas = {1: 9, 2: 12, 3: 15}[modo]
                return rondas
            else:
                for ee in range(len(error_escoja_nuevo)):
                    print(error_escoja_nuevo[ee]) 
                print("ERROR, escoja nuevamente.")
        except ValueError:
            for ei in range(len(entrada_invalida_ingresa_valores_dentro_del_rango)):
                print(entrada_invalida_ingresa_valores_dentro_del_rango[ei])
            print("Entrada no válida. Por favor, ingrese un número.")

def escoger_estadio(): 
    print("el estadio se escoge de manera aleatoria")
    for ee in range(len(estadio_se_escoge_de_manera_aleatoria)):
        print(estadio_se_escoge_de_manera_aleatoria[ee])
    estadio_escogido = random.choice(list(estadios))
    print(estadio_escogido)
    for i in range(len(estadios[estadio_escogido])):
        print(estadios[estadio_escogido][i])

    return estadio_escogido
    
def penal(jugador: str):
    global goles_primer_jugador, goles_segundo_jugador  # Para actualizar los goles globales

    if jugador == "jugador 1":
        gol_jugador = gol_jugador_1word
        jugador_word = jugador_1_word
        otro_jugador_word = jugador_2_word
        arco_p = arco_p2
        goles_penal = goles_primer_jugador
    elif jugador == "jugador 2":
        gol_jugador = gol_jugador_2word
        jugador_word = jugador_2_word
        otro_jugador_word = jugador_1_word
        arco_p = arco_p1
        goles_penal = goles_segundo_jugador

    matriz_penal = [[" " * 100 for _ in range(4)] for _ in range(90)]
    for i in range(len(arco_p)):
        matriz_penal[i][1] = arco_p[i]
    for i in range(len(balon)):
        matriz_penal[45 + i][1] = balon[i] 

    for i in matriz_penal:
        print("".join(i))

    while True:
        try:
            for jj in range(len(jugador_word)):
                print(jugador_word[jj])
            for tt in range(len(donde_desea_tirar)):
                print(donde_desea_tirar[tt])
            tiro = input(f"{jugador}: ¿a dónde deseas tirar (<-), (-), (->)?: ")
            if tiro in ["<-", "-", "->"]:
                break
            else:
                for ee in range(len(error_escoja_nuevo)):
                    print(error_escoja_nuevo[ee]) 
                print("ERROR, escoja nuevamente.")
        except ValueError:
            for ev in range(len(entrada_invalida_word)):
                print(entrada_invalida_word[ev])
            print("Entrada no válida.")

    while True:
        try:
            for pp in range(len(otro_jugador_word)):
                print(otro_jugador_word[pp])
            for oj in range(len(donde_desea_atajar)):
                print(donde_desea_atajar[oj])
            atajada = input(f"Otro jugador: ¿a dónde deseas atajar (<-), (-), (->)?: ")
            if atajada in ["<-", "-", "->"]:
                break
            else:
                for ee in range(len(error_escoja_nuevo)):
                    print(error_escoja_nuevo[ee]) 
                print("ERROR, escoja nuevamente.")
        except ValueError:
            for ev in range(len(entrada_invalida_word)):
                print(entrada_invalida_word[ev])
            print("Entrada no válida.")

    if jugador == "jugador 1":
        goles_primer_jugador = goles_penal
    else:
        goles_segundo_jugador = goles_penal

    if tiro == "<-" and atajada == "<-":
        for i in range(len(arco_p)):
            matriz_penal[i][0] = arco_p[i]
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100
        for i in range(len(arco_p)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro == "<-" and atajada == "-":
        for i in range(len(balon)):
            matriz_penal[i][0] = balon[i] 
        for i in range(len(arco_p)):
            matriz_penal[i * arco_p][1] = " " * 100
        for i in range(len(balon)):
            matriz_penal[45 + i][0] = " " * 100

    if tiro == "<-" and atajada == "->":
        for i in range(len(arco_p)):
            matriz_penal[i][2] = arco_p
        for i in range(len(balon)):
            matriz_penal[i][0] = balon[i] 
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro == "-" and atajada == "<-":
        for i in range(len(arco_p)):
            matriz_penal[i][0] = arco_p
        for i in range(len(balon)):
            matriz_penal[i][1] = balon[i] 
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro == "-" and atajada == "-":
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro == "-" and atajada == "->":
        for i in range(len(balon)):
            matriz_penal[i][1] = balon[i] 
        for i in range(len(arco_p)):
            matriz_penal[i][2] = arco_p
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro == "->" and atajada == "<-":
        for i in range(len(arco_p)):
            matriz_penal[i * arco_p][0] = arco_p
        for i in range(len(balon)):
            matriz_penal[i][2] = balon[i] 
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100

    if tiro == "->" and atajada == "-":
        for i in range(len(balon)):
            matriz_penal[i][2] = balon[i] 
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro == "->" and atajada == "->":
        for i in range(len(arco_p)):
            matriz_penal[i][2] = arco_p
        for i in range(len(arco_p)):
            matriz_penal[i][1] = " " * 100
        for i in range(len(balon)):
            matriz_penal[45 + i][1] = " " * 100

    if tiro != atajada:
        goles_penal += 1
        print(f"¡Gol de {jugador}!")
        for gg in range(len(gol_jugador)):
            print(gol_jugador[gg])

    return goles_penal

def desempate():
    global ronda_penales, goles_primer_jugador, goles_segundo_jugador
    ronda_penales = 1
    goles_primer_jugador = 0
    goles_segundo_jugador = 0

    while ronda_penales <= 5:
        # Tiro del primer jugador
        penal("jugador 1")
        # Tiro del segundo jugador
        penal("jugador 2")

        # Verificar condiciones de victoria después del tiro del segundo jugador
        if ronda_penales == 3 and goles_primer_jugador == 3 and goles_segundo_jugador == 0:
            print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
            break
        elif ronda_penales == 4 and goles_primer_jugador == 4 and goles_segundo_jugador <= 1:
            print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
            break
        elif ronda_penales == 5 and goles_primer_jugador == 5 and goles_segundo_jugador <= 2:
            print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
            break

        # Verificar si el segundo jugador puede ganar o empatar
        if ronda_penales == 3 and goles_segundo_jugador == 3 and goles_primer_jugador == 0:
            print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
            break
        elif ronda_penales == 4 and goles_segundo_jugador == 4 and goles_primer_jugador <= 1:
            print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
            break
        elif ronda_penales == 5 and goles_segundo_jugador == 5 and goles_primer_jugador <= 2:
            print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
            break

        ronda_penales += 1

    # Si no hay un ganador después de 5 rondas
    if ronda_penales > 5 and goles_segundo_jugador == goles_primer_jugador:
        print("Empate. Rondas adicionales:")
        while True:
            penal("jugador 1")
            penal("jugador 2")

            if goles_primer_jugador > goles_segundo_jugador:
                print(f"El primer jugador gana con un marcador de {goles_primer_jugador}-{goles_segundo_jugador}")
                break
            elif goles_segundo_jugador > goles_primer_jugador:
                print(f"El segundo jugador gana con un marcador de {goles_segundo_jugador}-{goles_primer_jugador}")
                break

def carta_especial (jugador : str):

    global ataque_jugadores_p1, ataque_jugadores_p2, defensa_jugadores_p1, defensa_jugadores_p2, goles_primer_jugador, goles_segundo_jugador, jugadores_partido_p1, jugadores_partido_p2, jugadores_muertos_p1, jugadores_muertos_p2, talentos_jugador_1, talentos_jugador_2, cols
    
    if jugador == "jugador 1":
        talentos = talentos_jugador_1
        talentos_rivales = talentos_jugador_2
        jugadores_sin_vida = jugadores_muertos_p1
        jugadores_sin_vida_rival = jugadores_muertos_p2
        jugadores_cancha = jugadores_partido_p1
        jugadores_cancha_rival = jugadores_partido_p2
        jugadores_propios = jugadores_p1
        jugadores_rivales = jugadores_p2
        ataque_jugadores = ataque_jugadores_p1
        defensa_jugadores = defensa_jugadores_p1
        jugador_rival = "jugador 2"
        ataque_rival = ataque_jugadores_p2
        defensa_rival = defensa_jugadores_p2
        goles = goles_primer_jugador
        suerte : float = 0.05
        suerte_rival : float = 0.05
        if estadio_p1 == escoger_estadio:
            suerte += 0.1
            suerte_rival -= 0.1

    if jugador == "jugador 2":
        talentos = talentos_jugador_2
        talentos_rivales = talentos_jugador_1
        jugadores_sin_vida = jugadores_muertos_p2
        jugadores_sin_vida_rival = jugadores_muertos_p1
        jugadores_cancha = jugadores_partido_p2
        jugadores_cancha_rival = jugadores_partido_p1
        jugadores_propios = jugadores_p1
        jugadores_rivales = jugadores_p2
        ataque_jugadores = ataque_jugadores_p2
        defensa_jugadores = defensa_jugadores_p2
        jugador_rival = "jugador 1"
        ataque_rival = ataque_jugadores_p1
        defensa_rival = defensa_jugadores_p1
        goles = goles_segundo_jugador
        suerte : float = 0.05
        suerte_rival : float = 0.05
        if estadio_p2 == escoger_estadio:
            suerte += 0.1
            suerte_rival -= 0.1
    
    def actualizar_matriz_cartas_especiales(dorsal : int):
        if defensa_jugadores[dorsal] <= 0:
            jugadores_sin_vida.append(dorsal)
            jugadores_cancha.remove(dorsal)
            for col in cols:
            # Iterar solo sobre los primeros dos elementos de 'col'
                for fila in col[:2]:  
                    if dorsal == fila:  # Verificar si 'dorsal' está en los primeros dos elementos
                        index_fila = col.index(dorsal)
                        col[index_fila] = 0  # Reemplazar dorsal con 0
                        jugador = jugadores_propios[dorsal]
                        for i in range(len(jugador)):
                            matriz_visual[(index_fila * 44) + i][cols.index(col)] = " " * 100

            for r in matriz_visual:
                        print("".join(r)) 
    
    def actualizar_matriz_cartas_especiales_rival(dorsal : int):
        if defensa_rival[dorsal] <= 0:
            jugadores_sin_vida_rival.append(dorsal)
            jugadores_cancha_rival.remove(dorsal)
            for col in cols:
            # Iterar solo sobre los primeros dos elementos de 'col'
                for fila in col[2:-1]:  
                    if dorsal == fila:  # Verificar si 'dorsal' está en los ultimos elementos
                        index_fila = col.index(dorsal)
                        col[index_fila] = 0  # Reemplazar dorsal con 0
                        jugador = jugadores_rivales[dorsal]
                        for i in range(len(jugador)):
                            matriz_visual[(index_fila * 44) + i][cols.index(col)] = " " * 100

            for r in matriz_visual:
                        print("".join(r)) 

    for llave, valor in cartas_especiales.items():
        print(f"CARTA : {llave}")
        print(f"FUNCIÓN : {valor}")
        print(f"VALOR : {creditos_cartas_especiales[llave]}")
        print("-" * 100) 

    while True:
        try:
            for ss in range(len(desea_usar_una_carta)):
                print(desea_usar_una_carta[ss])
            seleccion_carta_especial = str(input("ingrese la carta que desea jugar: "))
            if seleccion_carta_especial in cartas_especiales.keys() and talentos > creditos_cartas_especiales[seleccion_carta_especial]:
                break
            elif seleccion_carta_especial not in cartas_especiales.keys():
                for cc in range(len(carta_invalida)):
                    print(carta_invalida[cc])
                print("carta inválida")
            elif talentos < creditos_cartas_especiales[seleccion_carta_especial]:
                for nn in range(len(no_tienes_suficientes_creditos)):
                    print(no_tienes_suficientes_creditos[nn])
                print("no tienes suficientes creéditos")
        except ValueError:
            for ee in range(len(entrada_invalida_word)):
                print(entrada_invalida_word[ee])
            print("ERROR, entrada invalida.")

    match seleccion_carta_especial:
        case "tikitaka ":
            if len(jugadores_cancha) > 0:
                talentos -= creditos_cartas_especiales["tikitaka "]
                for jugador in jugadores_cancha:
                    if jugador in defensa_jugadores:
                        defensa_jugadores[jugador] += 2
                    if jugador in ataque_jugadores:
                        ataque_jugadores[jugador] += 2
            else:
                for nh in range(len(no_hay_jugadores_cancha)):
                    print(no_hay_jugadores_cancha[nh])
                print("no hay jugadores en cancha")

        case "tussi":
            while True:
                try:
                    for dt in range(len(jugador_que_soplar)):
                        print(jugador_que_soplar[dt])
                    dorsal_tussi = int(input("ingrese el dorsal del jugador que va a soplar: "))
                    if dorsal_tussi in jugadores_cancha:
                        if random.random() < 0.5 + suerte:
                            ataque_jugadores[dorsal_tussi] += 3
                        else:
                            defensa_jugadores[dorsal_tussi] -= 1
                            if defensa_jugadores[dorsal_tussi] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_tussi)
                        talentos -= creditos_cartas_especiales["tussi"]
                        break
                    else:
                        print("ese jugador no esta jugando")
                except ValueError:
                    print("dorsal invalido")

        case "roja":
            while True:
                try:
                    for dr in range(len(dorsal_jugador_roja)):
                        print(dorsal_jugador_roja[dr])
                    dorsal_roja = int(input("ingrese el dorsal del jugador al que le va a sacar roja: "))
                    if dorsal_roja in jugadores_cancha_rival:
                        defensa_rival[dorsal_roja] -= 10
                        if defensa_rival[dorsal_roja] <= 0:
                            actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_roja)
                        talentos -= creditos_cartas_especiales["roja"]
                        break
                    else:
                        for jn in range(len(ese_jugador_no_esta_jugando)):
                            print(ese_jugador_no_esta_jugando[jn])
                        print("ese jugador no esta jugando")
                except ValueError:
                    for di in range(len(dorsal_invalido)):
                        print(dorsal_invalido[di])
                    print("dorsal invalido")

        case "amarilla":
            while True:
                try:
                    for da in range(len(dorsal_jugador_amarilla)):
                        print(dorsal_jugador_amarilla[da])
                    dorsal_amarilla = int(input("ingrese el dorsal del jugador al que le va a sacar amarilla: "))
                    if dorsal_amarilla in jugadores_cancha_rival:    
                        defensa_rival[dorsal_amarilla] -= 3
                        if defensa_rival[dorsal_amarilla] <= 0:
                            actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_amarilla)
                        talentos -= creditos_cartas_especiales["amarilla"]
                        break
                    else:
                        for pp in range(len(ese_jugador_no_esta_jugando)):
                            ese_jugador_no_esta_jugando[pp]
                        print("ese jugador no esta jugando")
                except ValueError:
                    for dd in range(len(dorsal_invalido)):
                        print(dorsal_invalido[dd])
                    print("dorsal invalido")

        case "barrabrava":
                if len(jugadores_cancha_rival) > 0:
                    talentos -= creditos_cartas_especiales["barrabrava"]
                    for jugador in jugadores_cancha_rival:
                        if jugador in ataque_rival[jugador]:
                            ataque_rival[jugador] -= 1
                else:
                    for nj in range(len(no_hay_jugadores_cancha)):
                        print(no_hay_jugadores_cancha[nj])
                    print("no hay jugadores en cancha")
                    

        case "mistica":
            if ronda > 8:
                goles += 1
                talentos -= creditos_cartas_especiales["mistica"]
            else:
                for an in range(len(aun_no_es_el_momento)):
                    print(aun_no_es_el_momento[an])
                print("aun no es el momento...")

        case "gatorade":
            while True:
                try:
                    for dg in range(len(jugador_desea_hidratar)):
                        print(jugador_desea_hidratar[dg])
                    dorsal_gatorade = int(input("ingrese el dorsal del jugador que desea hidratar: "))
                    if dorsal_gatorade in jugadores_cancha:
                        defensa_jugadores[dorsal_gatorade] += 1
                        ataque_jugadores[dorsal_gatorade] += 1
                        talentos -= creditos_cartas_especiales["gatorade"]
                        break
                    else:
                        for es in range(len(ese_jugador_no_esta_jugando)):
                            print(ese_jugador_no_esta_jugando[es])
                        print("ese jugador no esta jugando")
                except ValueError:
                    for ddi in range(len(dorsal_invalido)):
                        print(dorsal_invalido[ddi])
                    print("dorsal invalido")

        case "chilena":
            while True:
                try:
                    for dc in range(len(jugador_a_realizar_chilena)):
                        print(jugador_a_realizar_chilena[dc])
                    dorsal_chilena = int(input("ingrese el jugador que va a hacer la chilena: "))
                    if dorsal_chilena in jugadores_cancha:
                        if random.random() > 0.3:
                            goles += 3
                        else:
                            defensa_jugadores[dorsal_chilena] -= 3
                            if defensa_jugadores[dorsal_chilena] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_chilena)
                        talentos -= creditos_cartas_especiales["chilena"]
                        break
                    else:
                        for ess in range(len(ese_jugador_no_esta_jugando)):
                            print(ese_jugador_no_esta_jugando[ess])
                        print("ese jugador no esta jugando")
                except ValueError:
                    for dx in range(len(dorsal_invalido)):
                        print(dorsal_invalido[dx])
                    print("dorsal invalido")

        case "balon de oro":
            while True:
                try:
                    for dbo in range(len(jugador_ganador_balon_de_oro)):
                        print(jugador_ganador_balon_de_oro[dbo])
                    dorsal_balon_oro = int(input("ingrese el dorsal del jugador que se supero a si mismo: "))
                    if dorsal_balon_oro in ataque_jugadores:
                        ataque_jugadores[dorsal_balon_oro] += 5
                        defensa_jugadores[dorsal_balon_oro] += 5
                        talentos -= creditos_cartas_especiales["balon de oro"]
                        break
                    else:
                        for eq in range(len(jugador_no_esta_tu_equipo)):
                            print(jugador_no_esta_tu_equipo[eq])
                        print("ese jugador no esta en tu equipo")
                except ValueError:
                    for dxx in range(len(dorsal_invalido)):
                        print(dorsal_invalido[dxx])
                    print("dorsal invalido")

        case "bota dorada":
            while True:
                try:
                    for dbd in range(len(jugador_bota_doradisima)):
                        print(jugador_bota_doradisima[dbd])
                    dorsal_bota_dorada = int(input("ingrese el dorsal del jugador que va a patear durisimo: "))
                    if dorsal_bota_dorada in ataque_jugadores:
                        ataque_jugadores[dorsal_bota_dorada] += 10
                        talentos -= creditos_cartas_especiales["bota dorada"]
                        break
                    else:
                        for eqq in range(len(jugador_no_esta_tu_equipo)):
                            print(jugador_no_esta_tu_equipo[eqq])
                        print("ese jugador no esta en tu equipo")
                except ValueError:
                    for dxd in range(len(dorsal_invalido)):
                        print(dorsal_invalido[dxd])
                    print("dorsal invalido")

        case "mano de dios":
            talentos -= creditos_cartas_especiales["mano de dios"]
            suerte += 0.1

        case "comprar arbitro":
            talentos -= creditos_cartas_especiales["comprar arbitro"]
            suerte_rival -= 0.1

        case "gol fantasma":
            talentos -= creditos_cartas_especiales["gol fantasma"]
            if random.random() < 0.1 + suerte:
                goles += 1

        case "encara messi":
            talentos -= creditos_cartas_especiales["encara messi"]
            for jugador in jugadores_cancha_rival:
                if jugador in defensa_rival[jugador]:
                    defensa_rival[jugador] -= 1
                    if defensa_rival[jugador] <= 0:
                        actualizar_matriz_cartas_especiales_rival(dorsal=jugador)

        case "mordidita":
            while True:
                try:
                    for dm in range(len(jugador_mostrador_dientes)):
                        print(jugador_mostrador_dientes[dm])
                    dorsal_mordedor = int(input("ingrese el dorsal del jugador que mostrara los dientes ;): "))
                    for dmm in range(len(jugador_lastimosamente_mordido)):
                        print(jugador_lastimosamente_mordido[dmm])
                    dorsal_mordido = int(input("ingrse el dorsal del jugador que desea morder: "))
                    if dorsal_mordedor in jugadores_cancha and dorsal_mordido in jugadores_cancha_rival:
                        if random.random() > 0.1 + suerte:
                            defensa_rival[dorsal_mordido] -= 8
                            if defensa_rival[dorsal_mordido] <= 0:
                                actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_mordido)
                        else:
                            defensa_jugadores[dorsal_mordedor] -= 10
                            if defensa_jugadores[dorsal_mordedor] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_mordedor)  
                                penal(jugador_rival)  
                        talentos -= creditos_cartas_especiales["mordidita"]
                        break
                    else:
                        for udj in range(len(uno_de_esos_jugadores_no_esta_jugando)):
                            print(uno_de_esos_jugadores_no_esta_jugando[udj])
                        print("uno de esos jugadores no esta jugando")      
                except ValueError:
                    for did in range(len(dorsal_invalido)):
                        print(dorsal_invalido[did])
                    print("dorsal invalido")    

        case "barrida":
            while True:
                try:
                    for db in range(len(jugador_cometera_accion)):
                        print(jugador_cometera_accion[db])
                    dorsal_barrer = int(input("ingrese el dorsal del jugador que cometera la accion: "))
                    for dbb in range(len(jugador_lastimosamente_barrido)):
                        print(jugador_lastimosamente_barrido[dbb])
                    dorsal_barrido = int(input("ingrese el dorsal del jugador que sera barrido: "))
                    if dorsal_barrer in jugadores_cancha and dorsal_barrido in jugadores_cancha_rival:
                        if random.random() > 0.3 + suerte:
                            defensa_rival[dorsal_barrido] -= 5
                            if defensa_rival[dorsal_barrido] <= 0:
                                actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_barrido)
                        else:
                            defensa_jugadores[dorsal_barrer] -= 10
                            if defensa_jugadores[dorsal_barrer] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_barrer)
                                penal(jugador_rival)    
                        talentos -= creditos_cartas_especiales["barrida"]
                        break
                    else:
                        for udjn in range(len(uno_de_esos_jugadores_no_esta_jugando)):
                            print(uno_de_esos_jugadores_no_esta_jugando[udjn])
                        print("uno de esos jugadores no esta jugando")
                except ValueError:
                    for dix in range(len(dorsal_invalido)):
                        print(dorsal_invalido[dix])
                    print("dorsal invalido")

        case "golpe":
            while True:
                try:
                    for dgg in range(len(jugador_que_lanza_golpe)):
                        print(jugador_que_lanza_golpe[dgg])
                    dorsal_golpear = int(input("ingrese el dorsal del jugador que lanza el golpe: "))
                    for drg in range(len(jugador_que_recibe_golpe)):
                        print(jugador_que_recibe_golpe[drg])
                    dorsal_golpeado = int(input("ingrese el dorsal del jugador que recibe el golpe: "))
                    if dorsal_golpeado in jugadores_cancha and dorsal_golpear in jugadores_cancha_rival:
                        if random.random() > 0.2 + suerte:
                            defensa_rival[dorsal_golpeado] -= 6
                            if defensa_rival[dorsal_golpeado] <= 0:
                                actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_golpeado)
                        else:
                            defensa_jugadores[dorsal_golpear] -= 10
                            if defensa_jugadores[dorsal_golpear] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_golpear)
                                penal(jugador_rival)    
                        talentos -= creditos_cartas_especiales["golpe"]
                        break
                    else:
                        for udjnn in range(len(uno_de_esos_jugadores_no_esta_jugando)):
                            print(uno_de_esos_jugadores_no_esta_jugando[udjnn])
                        print("uno de esos jugadores no esta jugando")
                except ValueError:
                    for dix1 in range(len(dorsal_invalido)):
                        print(dorsal_invalido[dix1])
                    print("dorsal invalido")

        case "cabebazo":
            while True:
                try:
                    for dlc in range(len(jugador_que_cabeceara)):
                        print(jugador_que_cabeceara[dlc])
                    dorsal_cabeceador = int(input("ingrese el dorsal del jugador que va a 'cabecear': "))
                    for drc in range(len(jugador_lastimosamente_cabeceado)):
                        print(jugador_lastimosamente_cabeceado[drc])
                    dorsal_cabeceado = int(input("ingrese el dorsal del jugador que sera 'agredido': "))
                    if dorsal_cabeceado in jugadores_cancha and dorsal_cabeceador in jugadores_cancha_rival:
                        if random.random() > 0.05 + suerte:
                            defensa_rival[dorsal_cabeceado] -= 10
                            if defensa_rival[dorsal_cabeceado] <= 0:
                                actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_cabeceado)
                        else:
                            defensa_jugadores[dorsal_cabeceador] -= 10
                            if defensa_jugadores[dorsal_cabeceador] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_cabeceador)
                                penal(jugador_rival)
                        talentos -= creditos_cartas_especiales["cabebazo"]
                        break
                    else:
                        for jugador_nono in range(len(uno_de_esos_jugadores_no_esta_jugando)):
                            print(uno_de_esos_jugadores_no_esta_jugando[jugador_nono])
                        print("uno de esos jugadores no esta jugando")
                except ValueError:
                    for line in range(len(dorsal_invalido)):
                        print(dorsal_invalido[line])
                    print("dorsal invalido")                

        case "provocacion":
            while True:
                try:
                    for dp in range(len(jugador_cometera_provocacion)):
                        print(jugador_cometera_provocacion[dp])
                    dorsal_provocador = int(input("ingrese el dorsal del jugador que cometera la provocacion: "))
                    for dpp in range(len(rival_lastimosamente_provocado)):
                        print(rival_lastimosamente_provocado[dpp])
                    dorsal_provocado = int(input("ingrese el dorsal del rival que desea provocar: "))
                    if dorsal_provocador in jugadores_cancha and dorsal_provocado in jugadores_cancha_rival:
                        if random.random() > 0.2 + suerte:
                            defensa_rival[dorsal_provocado] -= 3
                            if defensa_rival[dorsal_provocado] <= 0:
                                actualizar_matriz_cartas_especiales_rival(dorsal=dorsal_provocado)
                            defensa_jugadores[dorsal_provocador] -= 2
                            if defensa_jugadores[dorsal_provocador] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_provocador)
                                penal(jugador_rival)    
                        talentos -= creditos_cartas_especiales["provocacion"]
                        break
                    else:
                        for line_l in range(len(uno_de_esos_jugadores_no_esta_jugando)):
                            print(uno_de_esos_jugadores_no_esta_jugando[line_l])
                        print("uno de esos jugadores no esta jugando")
                except ValueError:
                    for line_x in range(len(dorsal_invalido)):
                        print(dorsal_invalido[line_x])
                    print("dorsal invalido")

        case "piscinazo":
            while True:
                try:
                    for dqp in range(len(dorsal_del_oscar_del_año)):
                        print(dorsal_del_oscar_del_año[dqp])
                    dorsal_piscinazo = int(input("Ingrese el dorsal del jugador que va a actuar: "))
                    if dorsal_piscinazo in jugadores_cancha:
                        if random.random() > 0.3 + suerte:
                            penal(jugador_rival)    
                        else:
                            defensa_jugadores[dorsal_piscinazo] -= 3
                            if defensa_jugadores[dorsal_piscinazo] <= 0:
                                actualizar_matriz_cartas_especiales(dorsal=dorsal_piscinazo)
                        talentos -= creditos_cartas_especiales["piscinazo"]
                        break
                    else:
                        for lineline in range(len(el_jugador_no_esta_en_cancha)):
                            print(el_jugador_no_esta_en_cancha[lineline])
                        print("el jugador no esta en cancha")
                except ValueError:
                    for line_xy in range(len(dorsal_invalido)):
                        print(dorsal_invalido[line_xy])
                    print("dorsal invalido")

# Bucle de juego por rondas
if __name__ == "__main__":
    
    teams = {
        1: barcelona,
        2: real_madrid,
        3: bayern,
        4: inter,
        5: psg,
        6: liverpool,
        7: milan,
        8: city,
        9: aston_villa 
    }

    cartas_especiales = {
        "tikitaka " : "+2 en el ataque y la defensa de tus jugadores",
        "barrabrava" : "-2 de ataque en todo el equipo rival",
        "encara messi" : "-1 de de defensa en todo el equipo rival",
        "tussi" : "20 porciento de probabilidad de +3 de daño sino -1 de vida",
        "gatorade" : "hidrata a uno de tus jugadores (+1 de vida +1 de daño)",
        "roja" : "-10 de vida (elimina) a cualquier jugador rival",
        "amarilla" : "-3 de vida a cualquier jugador rival",
        "mistica" : "+1 gol despues de la ronda ocho",
        "gol fantasma" : "(10%) probabilidad de hacer un gol",
        "chilena" : "30 porciento de probabilidad de hacer un golazo (vale x 3) sino te partes la espalda (-3 de vida )",
        "balon de oro" : "uno de tus jugadores saca su prime (+5 de ataque +5 de vida)",
        "bota dorada" : "uno de tus jugadores tiene un cañon en la pierna (+10 de ataque)",
        "mano de dios" : "el dieguito baja del cielo para ayudarte (+10%) de suerte",
        "comprar arbitro" : "haces un 'trato' con el arbitro ;) (-10%) de suerte a tu rival",
        "cabebazo" : "(5%) de probabilidad de -10 de vida a tu rival sino roja para tu jugador y penal para tu rival",
        "mordidita" : "(10%) de probabilidad de -8 de vida a tu rival sino roja para tu jugador y penal para tu rival",
        "golpe" : "(20%) de probabilidad de -6 de vida a tu rival sino roja para tu jugador y penal para tu rival",
        "barrida" : "(30%) de probabilidad de -5 de vida a tu rival sino roja para tu jugador y penal para tu rival",
        "provocacion" : "(30%) de probabilidad de penal amarilla a tu rival pero -2 de vida a tu jugador",
        "piscinazo" : "(30%) de probabilidad de penal para ti sino amarilla a tu jugador",
    }

    creditos_cartas_especiales = {
        "tikitaka " : 10,
        "barrabrava" : 8,
        "encara messi" : 7,
        "tussi" : 3,
        "gatorade" : 2,
        "roja" : 10,
        "amarilla" : 5,
        "mistica" : 4,
        "gol fantasma" : 2,
        "chilena" : 4,
        "balon de oro" : 9,
        "bota dorada" : 9,
        "mano de dios" : 7,
        "comprar arbitro" : 7,
        "cabebazo" : 1,
        "mordidita" : 1,
        "golpe" : 1,
        "barrida" : 2,
        "provocacion" : 3,
        "piscinazo" : 3
    }

    jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, costo_jugadores_p1, nombre_jugadores_p1, arco_p1, estadio_p1 = elegir_equipo("Jugador 1")
    jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2, costo_jugadores_p2, nombre_jugadores_p2, arco_p2, estadio_p2 = elegir_equipo("Jugador 2")
    rondas_totales = elegir_modo_juego()
    choose_estadium = escoger_estadio()
    
    jugadores_partido_p1 = []
    jugadores_partido_p2 = []
    jugadores_muertos_p1 = []
    jugadores_muertos_p2 = []
    costos_disponibles_p1 = {jugador: valor for jugador, valor in costo_jugadores_p1.items() if jugador not in jugadores_partido_p1}
    costo_minimo_p1 = min(costos_disponibles_p1.values())
    costos_disponibles_p2 = {jugador: valor for jugador, valor in costo_jugadores_p2.items() if jugador not in jugadores_partido_p2}
    costo_minimo_p2 = min(costos_disponibles_p2.values())
    costo_minimo_cartas = min(creditos_cartas_especiales.values())

    cols = [[0, 0, 0, 0, 0] for _ in range(4)]
    matriz_visual = [[" " * 100 for _ in range(5)] for _ in range(226)]

    actualizar_matriz : int = 45
    talentos_jugador_1 : int = 20
    talentos_jugador_2 : int = 20
    goles_primer_jugador: int = 0
    goles_segundo_jugador : int = 0
    ronda : int = 1
    while True:
        
        print(f"--- Ronda {ronda} ---")
        # Turno del jugador 1
        print("--- Turno del primer jugador ---")
        print(f"-- GOLES P1-- {goles_primer_jugador}")
        print(f"-- GOLES P2-- {goles_segundo_jugador}")
        print(f"-- CREDITOS -- {talentos_jugador_1}")
        for dorsal in jugadores_p1:
            nombre = nombre_jugadores_p1.get(dorsal)
            costo = costo_jugadores_p1.get(dorsal)
            # Imprimimos el costo y dorsal de cada jugador
            print(f"{nombre} -- DORSAL: {dorsal} -- COSTO: {costo}")

        while True:
            try:
                for linea in range(len(desea_poner_un_jugador)):
                    print(desea_poner_un_jugador[linea]) 
                poner_jugador_p1 = input("¿Desea poner a un jugador? (Responda si o no): ")
                if poner_jugador_p1.lower() in ["si", "no"]:
                    break
                else:
                    for linea1 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                        print(entrada_invalida_por_favor_responda_con_si_o_no[linea1])
                    print("Entrada inválida, por favor responda 'si' o 'no'.")
            except ValueError:
                for linea2 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                        print(entrada_invalida_por_favor_responda_con_si_o_no[linea2])
                print("Entrada inválida, por favor responda 'si' o 'no'.")

        if poner_jugador_p1.lower() == "si":
            while True:
                if talentos_jugador_1 < costo_minimo_p1:
                    for linea3 in range(len(no_tienes_suficientes_creditos)):
                        print(no_tienes_suficientes_creditos)
                    print("No tienes suficientes talentos.")
                    break
                            
                try:  
                    while True:
                        for line4 in range(len(jugador1_dorsal_jugador)):
                            print(jugador1_dorsal_jugador[line4])
                        numero_jugador_escogido = int(input("Jugador 1, ingresa el dorsal del jugador: "))
                        if numero_jugador_escogido not in jugadores_p1:
                            for line5 in range(len(dorsal_invalido)):
                                print(dorsal_invalido[line5])
                            print("Dorsal inválido, intenta de nuevo.")

                        elif numero_jugador_escogido in jugadores_partido_p1:
                            for line6 in range(len(jugador_en_cancha)):
                                print(jugador_en_cancha[line6])
                            print("Jugador en cancha, elige otro jugador.")

                        elif numero_jugador_escogido in jugadores_muertos_p1:
                            for linea7 in range(len(jugador_muerto)):
                                print(jugador_muerto[linea7])
                            print("Jugador muerto, elige otro jugador.")

                        elif talentos_jugador_1 < costo_jugadores_p1[numero_jugador_escogido]:
                            for linea8 in range(len(no_tienes_suficientes_creditos_para_este_jugador)):
                                print(no_tienes_suficientes_creditos_para_este_jugador[linea8])
                            print("No tienes suficientes creditos para contratar a este jugador.")

                        else:
                            try:
                                jugador_escogido = jugadores_p1[numero_jugador_escogido]
                                talentos_jugador_1 -= costo_jugadores_p1[numero_jugador_escogido]
                                jugadores_partido_p1.append(numero_jugador_escogido)

                                for linea9 in range(len(en_que_fila_12)):
                                    print(en_que_fila_12[linea9])
                                fila_p1 = int(input("En qué fila (1-2): "))
                                while fila_p1 not in [1, 2]:
                                    for linea10 in range(len(fila_valida_12)):
                                        print(fila_valida_12[linea10])
                                    fila_p1 = int(input("ERROR, ingrese una fila válida (1-2): "))

                                for linea11 in range(len(en_que_columna)):
                                    print(en_que_columna[linea11])
                                columna_p1 = int(input("En qué columna (1-4): "))
                                while columna_p1 not in [1, 2, 3, 4]:
                                    for linea12 in range(len(validar_columna_word)):
                                        print(validar_columna_word[linea12])
                                    columna_p1 = int(input("ERROR, ingrese una columna válida (1-4): "))

                                cols[columna_p1 - 1][fila_p1] = numero_jugador_escogido

                                filas_p1 = (fila_p1 - 1) * 44
                                for i in range(len(jugador_escogido)):
                                    matriz_visual[filas_p1 + i][columna_p1] = jugador_escogido[i]
                                
                                for r in matriz_visual:
                                    print("".join(r)) 
                                break
                                    
                            except ValueError:
                                for linea13 in range(len(entrada_invalida_ingresa_valores_dentro_del_rango)):
                                    print(entrada_invalida_ingresa_valores_dentro_del_rango[linea13])
                                print("Entrada inválida. ingresa valores dentro del rango")

                except ValueError:
                    for linea14 in range(len(dorsal_invalido)):
                        print(dorsal_invalido[linea14])
                    print("Dorsal inválido, intenta de nuevo.")
                    
                while True:
                    try:
                        for linea15 in range(len(desea_ingresar_otro_jugador)):
                            print(desea_ingresar_otro_jugador[linea15])
                        iterar_jugador = input("¿Desea ingresar otro jugador? (Responda si o no): ").lower()
                        if iterar_jugador in ["si", "no"]:
                            break
                        else:
                            for linea16 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                                print(entrada_invalida_por_favor_responda_con_si_o_no[linea16])
                            print("Entrada inválida, por favor responda 'si' o 'no'.")
                    except ValueError:
                        for linea17 in range(len(entrada_no_valida)):
                            print(entrada_no_valida[linea17])
                        print("Entrada inválida")
                    
                if iterar_jugador == "no":
                    break

        while True:
            try:
                for linea18 in range(len(desea_usar_una_carta)):
                    print(desea_usar_una_carta[linea18])
                ingresar_carta_p1 = input("¿Desea usar una carta?(responda con si o no):")
                if ingresar_carta_p1 in ["si", "no"]:
                    break
                else:
                    for linea19 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                        print(entrada_invalida_por_favor_responda_con_si_o_no[linea19])
                    print("Entrada inválida, por favor responda 'si' o 'no'.")
            except ValueError:
                for linea20 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                    print(entrada_invalida_por_favor_responda_con_si_o_no[linea20])
                print("Entrada inválida, por favor responda 'si' o 'no'.")

        if ingresar_carta_p1.lower() == "si":   
            while True:
                if talentos_jugador_1 < costo_minimo_cartas:
                    for linea21 in range(len(no_tienes_suficientes_creditos)):
                        print(no_tienes_suficientes_creditos[linea21])
                    print("No tienes suficientes talentos.")
                    break
                else:
                    carta_especial("jugador 1")
                    for r in matriz_visual:
                        print("".join(r))    

                while True:
                    try:
                        for linea22 in range(len(desea_ingresar_otra_carta)):
                            print(desea_ingresar_otra_carta[linea22])
                        iterar_cartas = input("¿Desea ingresar otra carta? (Responda si o no): ").lower()
                        if iterar_cartas in ["si", "no"]:
                            break
                        else:
                            for linea23 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                                print(entrada_invalida_por_favor_responda_con_si_o_no[linea23])
                            print("Entrada inválida, por favor responda 'si' o 'no'.")
                    except ValueError:
                        for linea24 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                                print(entrada_invalida_por_favor_responda_con_si_o_no[linea24])
                        print("Entrada inválida")
                    
                if iterar_cartas == "no":
                    break

        # Turno del jugador 2
        print("--- Turno del segundo jugador ---")
        print(f"-- GOLES P1-- {goles_primer_jugador}")
        print(f"-- GOLES P2-- {goles_segundo_jugador}")
        print(f"-- CREDITOS -- {talentos_jugador_2}")
        for dorsal in jugadores_p2:
            nombre = nombre_jugadores_p2.get(dorsal)
            costo = costo_jugadores_p2.get(dorsal)
            # Imprimimos el costo y dorsal de cada jugador
            print(f"JUGADOR: {nombre} -- DORSAL: {dorsal} -- COSTO: {costo}")

        while True:
            try:
                for linea25 in range(len(desea_poner_un_jugador)):
                    print(desea_poner_un_jugador[linea25]) 
                poner_jugador_p2 = input("¿Desea poner a un jugador? (Responda si o no): ")
                if poner_jugador_p2.lower() in ["si", "no"]:
                    break
                else:
                    for linea26 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                        print(entrada_invalida_por_favor_responda_con_si_o_no[linea26])
                    print("Entrada inválida, por favor responda 'si' o 'no'.")
            except ValueError:
                for linea27 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                    print(entrada_invalida_por_favor_responda_con_si_o_no[linea27])
                print("Entrada inválida, por favor responda 'si' o 'no'.")

        if poner_jugador_p2.lower() == "si":
            while True:
                if talentos_jugador_2 < costo_minimo_p2:
                    for linea28 in range(len(no_tienes_suficientes_creditos)):
                        print(no_tienes_suficientes_creditos[linea28])
                    print("No tienes suficientes talentos.")
                    break
                            
                try:  
                    while True:
                        for linea29 in range(len(jugador2_dorsal_jugador)):
                            print(jugador2_dorsal_jugador[linea29])
                        numero_segundo_escogido = int(input("Jugador 2, ingresa el dorsal del jugador: "))
                        if numero_segundo_escogido not in jugadores_p2:
                            for linea30 in range(len(dorsal_invalido)):
                                print(dorsal_invalido[linea30])
                            print("Dorsal inválido, intenta de nuevo.")

                        elif numero_segundo_escogido in jugadores_partido_p2:
                            for linea31 in range(len(jugador_en_cancha)):
                                print(jugador_en_cancha[linea31])
                            print("Jugador en cancha, elige otro jugador.")

                        elif numero_segundo_escogido in jugadores_muertos_p2:
                            for linea32 in range(len(jugador_muerto)):
                                print(jugador_muerto[linea32])
                            print("Jugador muerto, elige otro jugador.")

                        elif talentos_jugador_2 < costo_jugadores_p2[numero_segundo_escogido]:
                            for linea33 in range(len(no_tienes_suficientes_creditos_para_este_jugador)):
                                print(no_tienes_suficientes_creditos_para_este_jugador[linea33])
                            print("No tienes suficientes creditos para contratar a este jugador.")

                        else:
                            try:
                                jugador_escogido_segundo = jugadores_p2[numero_segundo_escogido]
                                talentos_jugador_2 -= costo_jugadores_p2[numero_segundo_escogido]
                                jugadores_partido_p2.append(numero_segundo_escogido)

                                for linea34 in range(len(en_que_fila_45)):
                                    print(en_que_fila_45[linea34])
                                fila_p2 = int(input("En qué fila (4-5): "))
                                while fila_p2 not in [4, 5]:
                                    for linea35 in range(len(fila_valida_45)):
                                        print(fila_valida_45[linea35])
                                    fila_p2 = int(input("ERROR, ingrese una fila válida (4-5): "))

                                for linea36 in range(len(en_que_columna)):
                                    print(en_que_columna[linea36])
                                columna_p2 = int(input("En qué columna (1-4): "))
                                while columna_p2 not in [1, 2, 3, 4]:
                                    for linea37 in range(len(validar_columna_word)):
                                        print(validar_columna_word[linea37])
                                    columna_p2 = int(input("ERROR, ingrese una columna válida (1-4): "))

                                cols[columna_p2 - 1][fila_p2] = numero_segundo_escogido

                                filas_p2 = (fila_p2 - 1) * 44
                                for i in range(len(jugador_escogido_segundo)):
                                    matriz_visual[filas_p2 + i][columna_p2] = jugador_escogido_segundo[i]
                                for r in matriz_visual:
                                    print("".join(r)) 
                                break
                                    
                            except ValueError:
                                for linea38 in range(len(entrada_invalida_ingresa_valores_dentro_del_rango)):
                                    print(entrada_invalida_ingresa_valores_dentro_del_rango[linea38])
                                print("Entrada inválida. ingresa valores dentro del rango")

                except ValueError:
                    for linea39 in range(len(dorsal_invalido)):
                        print(dorsal_invalido[linea39])
                    print("Dorsal inválido, intenta de nuevo.")
                    
                while True:
                    try:
                        for linea40 in range(len(desea_ingresar_otro_jugador)):
                            print(desea_ingresar_otro_jugador[linea40])
                        iterar_jugador_p2 = input("¿Desea ingresar otro jugador? (Responda si o no): ").lower()
                        if iterar_jugador_p2 in ["si", "no"]:
                            break
                        else:
                            for linea41 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                                print(entrada_invalida_por_favor_responda_con_si_o_no[linea41])
                            print("Entrada inválida, por favor responda 'si' o 'no'.")
                    except ValueError:
                        for linea42 in range(len(entrada_no_valida)):
                            print(entrada_no_valida[linea42])                                                 
                        print("Entrada inválida")
                    
                if iterar_jugador_p2 == "no":
                    break

        while True:
            try:
                for linea43 in range(len(desea_ingresar_otra_carta)):
                    print(desea_ingresar_otra_carta[linea43])
                ingresar_carta_p2 = input("¿Desea usar una carta?(responda con si o no):")
                if ingresar_carta_p2 in ["si", "no"]:
                    break
                else:
                    for linea44 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                        print(entrada_invalida_por_favor_responda_con_si_o_no[linea44])
                    print("Entrada inválida, por favor responda 'si' o 'no'.")
            except ValueError:
                for linea45 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                        print(entrada_invalida_por_favor_responda_con_si_o_no[linea45])
                print("Entrada inválida, por favor responda 'si' o 'no'.")

        if ingresar_carta_p2.lower() == "si":   
            while True:
                if talentos_jugador_2 < costo_minimo_cartas:
                    for linea46 in range(len(no_tienes_suficientes_creditos)):
                        print(no_tienes_suficientes_creditos[linea46])
                    print("No tienes suficientes talentos.")
                    break
                else:
                    carta_especial("jugador 2")
                    for r in matriz_visual:
                        print("".join(r))    

                while True:
                    try:
                        for linea47 in range(len(desea_ingresar_otra_carta)):
                            print(desea_ingresar_otra_carta[linea47])
                        iterar_cartas_p2 = input("¿Desea ingresar otra carta? (Responda si o no): ").lower()
                        if iterar_cartas_p2 in ["si", "no"]:
                            break
                        else:
                            for linea48 in range(len(entrada_invalida_por_favor_responda_con_si_o_no)):
                                print(entrada_invalida_por_favor_responda_con_si_o_no[linea48])
                            print("Entrada inválida, por favor responda 'si' o 'no'.")
                    except ValueError:
                        for linea49 in range(len(entrada_no_valida)):
                            print(entrada_no_valida[linea49])
                        print("Entrada inválida")
                    
                if iterar_cartas_p2 == "no":
                    break

        # Calculamos los goles
        for col in cols:
            indices = []
            if sum(col) != 0:
                for dorsal in col:
                    if dorsal != 0:
                        indice = col.index(dorsal)
                        indices.append(indice)

                if len(indices) == 1:
                    if indices[0] < 2:
                        goles_primer_jugador += ataque_jugadores_p1[col[indices[0]]]
                    elif indices[0] > 2:
                        goles_segundo_jugador += ataque_jugadores_p2[col[indices[0]]] 

                elif len(indices) == 2:
                    if indices[0] < 2 and indices[1] < 2:
                        goles_primer_jugador += ataque_jugadores_p1[col[indices[0]]] + ataque_jugadores_p1[col[indices[1]]]
                    elif indices[0] > 2 and indices[1] > 2:
                        goles_segundo_jugador += ataque_jugadores_p2[col[indices[0]]] + ataque_jugadores_p2[col[indices[1]]]
                    elif indices[0] < 2 and indices[1] > 2:

                        defensa_jugadores_p1[col[indices[0]]] -= ataque_jugadores_p2[col[indices[1]]]
                        defensa_jugadores_p2[col[indices[1]]] -= ataque_jugadores_p1[col[indices[0]]]

                        if defensa_jugadores_p1[col[indices[0]]] <= 0:
                            jugadores_muertos_p1.append(col[indices[0]])
                            jugadores_partido_p1.remove(col[indices[0]])
                            col[indices[0]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * (indices[0])) + i][cols.index(col)] = " " * 100
                        elif defensa_jugadores_p2[col[indices[1]]] <= 0:
                            jugadores_muertos_p2.append(col[indices[1]])
                            jugadores_partido_p2.remove(col[indices[1]])
                            col[indices[1]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * (indices[0])) + i][cols.index(col)] = " " * 100

                elif len(indices) == 3:
                    if indices[0] < 2 and indices[1] < 2 and indices[2] > 2:                   
                     
                        defensa_jugadores_p1[col[indices[1]]] -= ataque_jugadores_p2[col[indices[2]]]
                        defensa_jugadores_p2[col[indices[2]]] -= ataque_jugadores_p1[col[indices[1]]]

                        if defensa_jugadores_p2[col[indices[2]]] <= 0:
                            jugadores_muertos_p2.append(col[indices[2]])
                            jugadores_partido_p2.remove(col[indices[2]])
                            col[indices[2]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * (indices[2])) + i][cols.index(col)] = " " * 100
                            goles_primer_jugador += ataque_jugadores_p1[col[indices[0]]]
                        else:
                            defensa_jugadores_p2[col[indices[2]]] -= ataque_jugadores_p1[col[indices[0]]]
                            if defensa_jugadores_p2[col[indices[2]]] <= 0:
                                jugadores_muertos_p2.append(col[indices[2]])
                                jugadores_partido_p2.remove(col[indices[2]])
                                col[indices[2]] = 0
                                for i in range(actualizar_matriz):
                                    matriz_visual[(actualizar_matriz * (indices[2])) + i][cols.index(col)] = " " * 100

                        if defensa_jugadores_p1[col[indices[1]]] <= 0:
                            jugadores_muertos_p1.append(col[indices[1]])
                            jugadores_partido_p1.remove(col[indices[1]])
                            col[indices[1]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[1]) + i][cols.index(col)] = " " * 100
                        
                    elif indices[0] < 2 and indices[1] > 2 and indices[2] > 2:
                    
                        defensa_jugadores_p1[col[indices[0]]] -= ataque_jugadores_p2[col[indices[2]]]
                        defensa_jugadores_p2[col[indices[2]]] -= ataque_jugadores_p1[col[indices[0]]]

                        if defensa_jugadores_p1[col[indices[0]]] <= 0:
                            jugadores_muertos_p1.append(col[indices[0]])
                            jugadores_partido_p1.remove(col[indices[0]])
                            col[indices[0]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[0]) + i][cols.index(col)] = " " * 100
                            goles_segundo_jugador += ataque_jugadores_p2[col[indices[1]]]
                        else:
                            defensa_jugadores_p1[col[indices[0]]] -= defensa_jugadores_p2[col[indices[1]]]
                            if defensa_jugadores_p1[col[indices[0]]] <= 0:
                                jugadores_muertos_p1.append(col[indices[0]])
                                jugadores_partido_p1.remove(col[indices[0]])
                                col[indices[0]] = 0
                                for i in range(actualizar_matriz):
                                    matriz_visual[(actualizar_matriz * indices[0]) + i][cols.index(col)] = " " * 100

                        if defensa_jugadores_p2[col[indices[2]]] <= 0:
                            jugadores_muertos_p2.append(col[indices[2]])
                            jugadores_partido_p2.remove(col[indices[2]])
                            col[indices[2]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[2]) + i][cols.index(col)] = " " * 100

                elif len(indices) == 4:
                
                    defensa_jugadores_p1[col[indices[1]]] -= ataque_jugadores_p2[col[indices[2]]]
                    defensa_jugadores_p2[col[indices[2]]] -= ataque_jugadores_p1[col[indices[1]]]

                    if defensa_jugadores_p1[col[indices[1]]] <= 0:
                        jugadores_muertos_p1.append(col[indices[1]])
                        jugadores_partido_p1.remove(col[indices[1]])
                        col[indices[1]] = 0
                        for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[1]) + i][cols.index(col)] = " " * 100
                        defensa_jugadores_p1[col[indices[0]]] -= ataque_jugadores_p2[col[indices[3]]]
                        if defensa_jugadores_p1[col[indices[0]]] <= 0:
                            jugadores_muertos_p1.append(col[indices[0]])
                            jugadores_partido_p1.remove(col[indices[0]])
                            col[indices[0]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[0]) + i][cols.index(col)] = " " * 100
                    else:
                        defensa_jugadores_p1[col[indices[1]]] -= ataque_jugadores_p2[col[indices[3]]]
                        if defensa_jugadores_p1[col[indices[1]]] <= 0:
                            jugadores_muertos_p1.append(col[indices[1]])
                            jugadores_partido_p1.remove(col[indices[1]])
                            col[indices[1]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[1]) + i][cols.index(col)] = " " * 100
                    
                    if defensa_jugadores_p2[col[indices[2]]] <= 0:
                        jugadores_muertos_p2.append(col[indices[2]])
                        jugadores_partido_p2.remove(col[indices[2]])
                        col[indices[2]] = 0
                        for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[2]) + i][cols.index(col)] = " " * 100
                        defensa_jugadores_p2[col[indices[3]]] -= ataque_jugadores_p1[col[indices[0]]]
                        if defensa_jugadores_p2[col[indices[3]]] <= 0:
                            jugadores_muertos_p2.append(col[indices[3]])
                            jugadores_partido_p2.remove(col[indices[3]])
                            col[indices[3]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[3]) + i][cols.index(col)] = " " * 100

                    else:
                        defensa_jugadores_p2[col[indices[2]]] -= ataque_jugadores_p1[col[indices[0]]]
                        if defensa_jugadores_p2[col[indices[2]]] <= 0:
                            jugadores_muertos_p2.append(col[indices[2]])
                            jugadores_partido_p2.remove(col[indices[2]])
                            col[indices[2]] = 0
                            for i in range(actualizar_matriz):
                                matriz_visual[(actualizar_matriz * indices[2]) + i][cols.index(col)] = " " * 100
        
        for r in matriz_visual:
            print("".join(r))

        if ronda == rondas_totales:
            break

        ronda += 1
        talentos_jugador_1 += ronda * 2
        talentos_jugador_2 += ronda * 2

    if goles_primer_jugador == goles_segundo_jugador:
        desempate
    elif goles_primer_jugador > goles_segundo_jugador:
        print("PRIMER JUGADOR GANA")
    else:
        print("SEGUNDO JUGADOR GANA")
