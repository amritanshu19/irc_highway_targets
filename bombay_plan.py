#Bombay Plan, Reference State:Sikkim

#A: Developed and agricultural areas in sq.km, A is estimated by using total agricultral land in sikkim (ref: https://sikkim.gov.in/departments/food-security-and-agriculture-development-department) + total urban land in sikkim
A = float(424.4+38.25)

#B: semi develped area in sq.km, B = total rural land area in sikkim which is total area of sikkim (7096 sq.km - A - C)
B = float(7096-(424.4+38.25+0.473*7096))

#C: un-developed area in sq.km, C = total forest cover + protected areas in sikkim which 43% of total area 
C = float(0.473*7096)

#K: no of towns with pop. over 1 lakh, only capital have population above 1 lakh as sikkim is a small state ref:
K = float(1)

#M: no of towns with pop. in range 1L-50K, as per census 2011
M = float(0)

#N: no of towns with pop. in range 50K-20K, as per census 2011
N = float(2)

#P: no of towns with pop. in range 20K-10K, as per census 2011
P = float(2)

#Q: no of towns with pop. in range 10K-5K, as per census 2011
Q = float(3)

#R: no of towns with pop. in range 5K-2K, as per census 2011
R = float(10)

#S: no of towns with pop. in range 2K-1K, as per census 2011
S = float(15)

#T: no of towns with pop. in range 1K-500, as per census 2011
T = float(20)

#V: no of towns with population less than 500, as per census 2011
V = float(150)

#D: development allowance of 5%, value of D has been adjusted in the formula for the ease of code as formulas has been multiplied by 1.05 i.e (100% + 5%)

#N1: NH
N1 = 1.05 * (A/64+B/80+C/96+32*K+8*M)

#N2: NH + SH
N2 = 1.05 * (A/20+B/24+C/32+48*K+24*M+11.2*N+1.6*P)

#N3: NH + SH + MDR
N3 = 1.05 * (A/8+B/16+C/24+48*K+24*M+11.2*N+9.6*P+6.4*Q+2.4*R)

#N4: NH + SH + MDR + (ODR+VR)
N4 = 1.05 * (A/4+B/8+C/12+48*K+24*M+11.2*N+9.6*P+12.8*Q+5.9*R+1.6*S+0.64*T+0.2*V)

#national highway length
NH = N1

#state highway length
SH = N2-N1

#major district roads
MDR = N3-N2

#other district roads + village roads (included)
ODR = N4 - N3

print(" length of NH:", NH, "\n","length of SH:", SH,"\n","length of MDR:", MDR, "\n", "length of ODR+VR:", ODR)
