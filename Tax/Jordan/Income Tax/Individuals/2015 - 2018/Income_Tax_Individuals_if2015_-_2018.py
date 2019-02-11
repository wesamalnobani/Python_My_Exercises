#Income_Tax_Individuals_2015_-_2017
def ITI_2015_2018 ():
    TB = 10000 
    A = float(input("Enter the amount to be taxed  (p_q): " ))
    if A <= 0 :
        IT = 0
    elif A <= TB and A > 0 :
        IT = A * 0.07
        if IT <= 1 :
            IT = 1
    elif A > TB and A <= (TB * 2):
        IT =(TB * 0.07)+((A -TB) * 0.14)
    else :
        IT = (TB*0.07)+(TB*0.14)+((A-(TB *2))*0.20)
    print('------------------------------------------')
    print('Income Tax = ',int(IT),'JD(@_@) ')
    print('Monethly Income Tax = ',int(IT/12),'JD(0_0)')
ITI_2015_2018 ()


    
