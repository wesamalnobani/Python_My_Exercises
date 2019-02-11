#Income_Tax_Individuals_2019
def ITI_2019 ():
    # Tax bracket
    TB = 5000
    # Tax rate
    TR = 0.05
    #Input the amount to be taxed 
    A = float(input("Enter the amount to be taxed  (p_q): " ))
    #0- Tax bracket( <= 0)
    if A <= 0 :
        print('------------------------------------------')
        print('(^_^) Not subject to')
        IT = 0
    #1- Tax bracket(First 5000)/0.05
    elif A <= TB and A > 0 :
        IT = A * TR
        print('------------------------------------------')
        print( A,'X 5%  = ',IT)
        if IT < 1 :
            IT = 1
    #2- Tax bracket( > 5000 <= 10000)/0.1
    elif A > TB and A <= (TB * 2):
        IT = (TB * TR )+((A - TB)* (TR * 2))
        print('------------------------------------------')
        print('5000    X 5%  = 250')
        print((A-TB),'X 10% = ',IT-250)
    #3- Tax bracket( > 10000 <= 15000 )/0.15
    elif A > (TB * 2) and A <= (TB * 3):
        IT = (TB * TR)+(TB * (TR * 2))+((A - (TB * 2)) * (TR * 3))
        print('------------------------------------------')
        print('5000   X  5%  = 250')
        print('5000   X  10% = 500')
        print((A-(TB*2)),' X  15% =',IT-750)
    #4- Tax bracket( > 15000 <= 20000 )/0.2 
    elif A > (TB * 3) and A <= (TB * 4):
        IT = (TB * TR)+(TB * (TR * 2))+ (TB * (TR * 3))+((A - (TB * 3)) * (TR * 4))
        print('------------------------------------------')
        print('5000   X  5%  = 250')
        print('5000   X  10% = 500')
        print('5000   X  15% = 750')
        print((A-(TB*3)),'X  20% =',IT-1500)
    #5-Tax bracket ( > 20000 <= 1000000 )/0.25
    elif A > (TB * 4) and A <= (TB * 200) :
        IT = (TB * TR) + (TB * (TR * 2)) + (TB * (TR * 3))+(TB * (TR * 4))+ ((A - (TB * 4)) * (TR * 5))
        print('------------------------------------------')
        print('5000   X 5%  =  250')
        print('5000   X 10% =  500')
        print('5000   X 15% =  750')
        print('5000   X 20% =  1000')
        print((A-(TB*4)),'  X 25% =',IT-2500)
    #6-Tax bracket ( > 1000000 )/0.3
    else:
        IT = (TB * TR) + (TB * (TR * 2)) + (TB * (TR * 3)) +(TB * (TR * 4))+(((TB * 200) - (TB*4)) * (TR * 5))+((A - (TB * 200)) * (TR * 6))
        print('------------------------------------------')
        print('5000   X 5%  =  250')
        print('5000   X 10% =  500')
        print('5000   X 15% =  750')
        print('5000   X 20% =  1000')
        print('980000 X 25% = 245000')
        print(A-(TB * 200),'  X 30% = ',IT-247500)
    print('------------------------------------------')
    print('Income Tax = ',int(IT),'JD(@_@) ')
    print('Monethly Income Tax = ',int(IT/12),'JD(0_0)')
ITI_2019()

'''
Wesam Al-Nobani
'''



