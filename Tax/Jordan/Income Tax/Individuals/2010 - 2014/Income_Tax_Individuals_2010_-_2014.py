#Income_Tax_Individuals_2010_-_2014

def ITI_2010_2014 ():
    # Tax bracket
    TB = 12000
    # Tax rate
    TR = 0.07
    A = float(input('Subjected income: ' ))
    if A <= 0:
        IT = 0
        print('(^_^) Not subject to')
    elif A <= TB and A > 0 :
        IT = A * TR
    else :
        IT = (TB * 0.07) + ((A - TB) * (TR * 2))
    print('------------------------------------------')
    print('Income Tax = ',int(IT),'JD(@_@) ')
    print('Monethly Income Tax = ',int(IT/12),'JD(0_0)')  
ITI_2010_2014 ()
