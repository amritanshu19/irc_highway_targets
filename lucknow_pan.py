#Lucknow plan, refrence state: sikkim

#Area in sq.km
Area = float(7096)

#N: no of towns with popn above 5000
N = float(8)

#n2: no of villages and town
n2 = float(460)

#total road length
T = 4.74 * n2

#national highway length
NH = Area/50

#state highway length
SH = max(Area/25, 62.5*N-NH)

#major district roads
MDR = max(Area/12.5, 90*N)

#other district roads + village roads (included)
ODR = T - NH - SH - MDR
print(" length of NH:", NH, "\n","length of SH:", SH,"\n","length of MDR:", MDR, "\n", "length of ODR+VR:", ODR)
