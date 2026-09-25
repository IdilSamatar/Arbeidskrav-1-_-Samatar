"""
Arbeidskrav 1 

Sammenlikne Årlige Kostander av Elbil med Bensinbil

Idil Husein Samatar (idsam0436@usn.no)

Oppdatert 2026.09.25
"""

F = 5000 
T = 8.38*365
D = 0.2*10000*2
B = 0.1*10000
Elbil_Kostnader = (F+T+D+B)
print (Elbil_Kostnader)


F_Bensin = 7500
T_Bensin = 8.38*365
D_Bensin = 10000*1
B_Bensin = 0.3*10000
Bensin_Kostnader = (F_Bensin+T_Bensin+D_Bensin+B_Bensin )
print (Bensin_Kostnader)

Kostnadsdifferansen = (Bensin_Kostnader - Elbil_Kostnader)
print (Kostnadsdifferansen)
