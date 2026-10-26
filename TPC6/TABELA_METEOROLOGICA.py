
# TPC6 - Aplicação de Meteorologia

# Tipos de dados:
# TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
    # Data = (Int,Int,Int)
    # TempMin = Float
    # TempMax = Float
    # Precipitacao = Float


def menu():
    print('\n Menu')
    print('1: Média das temperaturas')
    print('2: Guardar tabela meteorológica')
    print('3: Carregar tabela meteorológica')
    print('4: Temperatura mínima mais baixa')
    print('5: Amplitude máxima')
    print('6: Dia com maior precipitação')
    print('7: Dias com precipitação superior a um limite')
    print('8: Maior período de calor')
    print('9: Mostrar gráfico meteorológico')
    print('0: Sair')


# (1.a) 1: TEMPERATURA MÉDIA DE CADA DIA
def Media_temp(tabMeteo):
    res = []
    for dia in tabMeteo:
        tem_media = (dia[1] + dia[2])/2
        tem_dia = (dia[0], tem_media)
        res.append(tem_dia)
    return res
 

# (1.b) 2: GUARDAR METEOROLÓGICA NUM FICHEIRO
def Guardar_tabela(tabela, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in tabela:      # era "in t"
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}|\n")
    file.close()
    return


# (1.c) 3: CARREGAR METEOROLÓGICA DE UM FICHEIRO
def Carregar_tabela(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        data, tmin, tmax, prec, _ = line.split("|")
        ano, mes, dia = data.split("-")
        tempo = ((int(ano), int(mes), int(dia)), float(tmin), float(tmax), float(prec))
        res.append(tempo)
    file.close()
    return res
 

# (1.d) 4: CARREGAR A TEMPERATURA MINIMA MAIS BAIXA
def Min_temp(tabMeteo):
    i = 1
    minimo = tabMeteo[0][1]
    for dia in tabMeteo:
        if dia[1] < minimo:
            minimo = dia[1]
    return minimo


# (1.e) 5: CALCULAR A AMPLITUDE TERMICA
def Amplitude_temp(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        amplitude = tmax - tmin
        res.append((data,amplitude))
    return res 


# (1.f) 6: DIA COM PRECIPITAÇÃO SUPERIOR A UM LIMITE
def Max_chuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for data, tmax, tmin, prec in tabMeteo:
            if prec > max_prec:
                max_prec = prec
                max_data = data
    return (max_data, max_prec)


# (1.g) 7: DIA COM PRECIPITAÇÃO MAXIMA
def Dias_chuvosos(tabMeteo, p):
    prec_superior = []
    for data, tmax, tmin, prec in tabMeteo:
        if prec > p:
            prec_superior.append((data,prec))
    return prec_superior
 
 
# (1.h) 8: MAIOR PERIODO DE CALOR
def Max_calor(tabMeteo, p):
    consec_atuais = 0
    maximo_diasconsec = 0
    for data, tmax, tmin, prec in tabMeteo:
        if prec < p:
            consec_atuais = consec_atuais + 1
            if consec_atuais > maximo_diasconsec:
                maximo_diasconsec = consec_atuais
        else:
            consec_atuais = 0
    return maximo_diasconsec
 
 
# (1.i) 9: MOSTRAR GRÁFICO METEROLOGÓGICO gráfico meteorológico
from matplotlib import pyplot as plt

def Grafico(t):
    #y_min = [ elem[1] for elem in t]
    y_min = [tmin for data, tmin, tmax, prec in t ]
    y_max = [tmax for data, tmin, tmax, prec in t ]
    y_prec = [prec for data, tmin, tmax, prec in t ]
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]

    plt.plot(x,y_min, color="blue", marker="o", label="Tmin ºC")
    plt.plot(x,y_max, color="red", marker="o", label="Tmax ºC")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.grid(color="black")
    plt.show()

    plt.bar(x,y_prec, color="green", label="Precipitação (mm)")
    plt.title("Precipitação")
    plt.legend()
    plt.grid()
    plt.show()
    return


 
tab_meteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

opção = -1

while opção != 0:
    menu()
    opção = int(input('Selecione a opção desejada: '))

    if opção == 1:
        print(Media_temp(tab_meteo1))
    elif opção == 2:
        Guardar_tabela(tab_meteo1, 'meteorologia.txt')
        print('Tabela guardada.')
    elif opção == 3:
        tab_meteo1 = Carregar_tabela('meteorologia.txt')
        print(tab_meteo1)
    elif opção == 4:
        print(Min_temp(tab_meteo1))
    elif opção == 5:
        print(Amplitude_temp(tab_meteo1))
    elif opção == 6:
        print(Max_chuva(tab_meteo1))
    elif opção == 7:
        print(Dias_chuvosos(tab_meteo1, 0))
    elif opção == 8:
        print(Max_calor(tab_meteo1, 0.6))
    elif opção == 9:
        Grafico(tab_meteo1)

print('Até à próxima!')