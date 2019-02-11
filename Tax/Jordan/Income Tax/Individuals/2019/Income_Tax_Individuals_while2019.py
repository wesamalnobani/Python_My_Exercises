#Income_Tax_Individuals_2019
A = float(input("Enter the amount to be taxed  (p_q): " ))
TB1 = 5000
TB2 = 1000000
TR = 0.05
while A > TB2 :
    IT = (TB1 * TR)+(TB1 * (TR*2))+(TB1 * (TR*3))+(TB1 * (TR*4))+((TB2-(TB1 *4)) *(TR *5))+((A - TB2)*(TR*6))
    print(IT)
    break
while A <= TB2 and A > (TB1*4):
    IT = ((A-(TB1 *4)) *(TR *5))+(TB1 * TR)+(TB1 * (TR*2))+(TB1 * (TR*3))+(TB1 * (TR*4))
    print(IT)
    break
while A <= (TB1*4) and A > (TB1*3):
    IT =(TB1 * TR)+(TB1 * (TR*2))+(TB1 * (TR*3))+((A-(TB1*3)) * (TR*4))
    print(IT)
    break
while A <= (TB1*3) and A > (TB1*2):
    IT =(TB1 * TR)+(TB1 * (TR*2))+((A-(TB1*2)) * (TR*3))
    print(IT)
    break
while A <= (TB1*2) and A > TB1:
    IT =(TB1 * TR)+((A-TB1) * (TR*2))
    print(IT)
    break
while A <= TB1 and A > 0:
    IT = A * TR
    print(IT)
    break

'''
Wesam Al-Nobani
'''
