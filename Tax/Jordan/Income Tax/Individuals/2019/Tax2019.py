#Income_Tax_Individuals_2019
def ITI_2019 ():
    #Input the amount to be taxed 
    A = float(input("Enter the amount to be taxed  (p_q): " ))
    #0- Tax bracket( <= 0)
    if A <= 0 :
        print('------------------------------------------')
        print('(^_^) Not subject to')
        IT = 0
    #1- Tax bracket(First 5000)/0.05
    elif A <= 5000 and A > 0 :
        IT = A * 0.05
        print('------------------------------------------')
        print( A,'X 5%  = ',IT)
        if IT < 1 :
            IT = 1
    #2- Tax bracket( > 5000 <= 10000)/0.1
    elif A > 5000 and A <= 10000:
        IT = 250 + ((A - 5000)* 0.10)
        print('------------------------------------------')
        print('5000    X 5%  = 250')
        print(A-5000,'X 10% = ',IT-250)
    #3- Tax bracket( > 10000 <= 15000 )/0.15
    elif A > 10000 and A <= 15000:
        IT = (750) + ((A - 10000) * 0.15)
        print('------------------------------------------')
        print('5000   X  5%  = 250')
        print('5000   X  10% = 500')
        print((A-10000),' X  15% =',IT-750)
    #4- Tax bracket( > 15000 <= 20000 )/0.2 
    elif A > 15000 and A <= 20000:
        IT = (1500) + ((A - 15000) * 0.20)
        print('------------------------------------------')
        print('5000   X  5%  = 250')
        print('5000   X  10% = 500')
        print('5000   X  15% = 750')
        print((A-15000),'X  20% =',IT-1500)
    #5-Tax bracket ( > 20000 <= 1000000 )/0.25
    elif A > 20000 and A <= 1000000 :
        IT = (2500) + ((A - 20000) * 0.25)
        print('------------------------------------------')
        print('5000   X 5%  =  250')
        print('5000   X 10% =  500')
        print('5000   X 15% =  750')
        print('5000   X 20% =  1000')
        print((A-(20000)),'  X 25% =',IT-2500)
    #6-Tax bracket ( > 1000000 )/0.3
    else:
        IT = (247500) + ((A - 1000000) * 0.30)
        print('------------------------------------------')
        print('5000   X 5%  =  250')
        print('5000   X 10% =  500')
        print('5000   X 15% =  750')
        print('5000   X 20% =  1000')
        print('980000 X 25% = 245000')
        print(A-1000000,'  X 30% = ',IT-247500)
    print('------------------------------------------')
    print('Income Tax = ',int(IT),'JD(@__@) ')
    print('Monethly Income Tax = ',int(IT/12),'JD(*__@)')
ITI_2019()
