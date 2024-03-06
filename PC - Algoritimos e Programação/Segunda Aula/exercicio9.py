cigaros_dia = int(input("Quantos cigarros fumados por dia: "))
anos_fumando = int(input("Quantos anos fumando: "))

dias_fumando = anos_fumando * 365
cigaros_consumidos = cigaros_dia * dias_fumando
minutos_vida_perdido = cigaros_consumidos * 10

minutos_dias = 60 * 24

dias_perdidos_vida = minutos_vida_perdido / minutos_dias

print("Perdeu {} dias de vida".format(dias_perdidos_vida))