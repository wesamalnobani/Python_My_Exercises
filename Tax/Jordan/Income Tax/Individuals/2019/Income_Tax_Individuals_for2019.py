#Income_Tax_Individuals_2019
A = float(input("Enter the amount to be taxed  (p_q): " ))
# Tax bracket
TB = 5000
# Tax rate
TR  = 0.05
IT  = [A*TR,
      (TB*TR)+ ((A-TB)*(TR*2)),
      (TB*TR)+(TB*(TR*2))+ ((A-(TB*2))*(TR*3)),
      (TB*TR)+(TB*(TR*2))+(TB*(TR*3))+ ((A- (TB*3))*(TR*4)),
      (TB*TR)+(TB*(TR*2))+(TB*(TR*3))+(TB*(TR*4))+ ((A-(TB*4))*(TR*5)),
      (TB*TR)+(TB*(TR*2))+(TB*(TR*3))+(TB*(TR*4))+(((TB*200)-(TB*4))*(TR*5))+ ((A-(TB*200))*(TR*6))]
for T in range(1):
    if A <= 0 :
        IT = 0
        print('------------------------------------------')
        print(IT,'(^_^) Not subject to')
        print('Monethly Income Tax = ',int(IT/12),'JD(0_0)')
    elif A <= TB and A > 0 :
        print('------------------------------------------')
        print( A,'X 5%  = ',IT[0])
        print('------------------------------------------')
        print('Income Tax = ',IT[0],'JD(@_@) ')
        print('Monethly Income Tax = ',int(IT[0]/12),'JD(0_0)')
    elif A > TB and A <= (TB * 2):
        print('------------------------------------------')
        print('5000    X 5%  = 250')
        print((A-TB),'X 10% = ',IT[1]-250)
        print('------------------------------------------')
        print('Income Tax = ',IT[1],'JD(@_@) ')
        print('Monethly Income Tax = ',int(IT[1]/12),'JD(0_0)')
    elif A > (TB * 2) and A <= (TB * 3):
        print('------------------------------------------')
        print('5000   X  5%  = 250')
        print('5000   X  10% = 500')
        print((A-(TB*2)),' X  15% =',IT[2]-750)
        print('------------------------------------------')
        print('Income Tax = ',IT[2],'JD(@_@) ')
        print('Monethly Income Tax = ',int(IT[2]/12),'JD(0_0)')
    elif A > (TB * 3) and A <= (TB * 4):
        print('------------------------------------------')
        print('5000   X  5%  = 250')
        print('5000   X  10% = 500')
        print('5000   X  15% = 750')
        print((A-(TB*3)),'X  20% =',IT[3]-1500)
        print('------------------------------------------')
        print('Income Tax = ',IT[3],'JD(@_@) ')
        print('Monethly Income Tax = ',int(IT[3]/12),'JD(0_0)')
    elif A > (TB * 4) and A <= (TB*200) :
        print('------------------------------------------')
        print('5000   X 5%  =  250')
        print('5000   X 10% =  500')
        print('5000   X 15% =  750')
        print('5000   X 20% =  1000')
        print((A-(TB*4)),'  X 25% =',IT[4]-2500)
        print('------------------------------------------')
        print('Income Tax = ',IT[4],'JD(@_@) ')
        print('Monethly Income Tax = ',int(IT[4]/12),'JD(0_0)')
    else:
        print('------------------------------------------')
        print('5000   X 5%  =  250')
        print('5000   X 10% =  500')
        print('5000   X 15% =  750')
        print('5000   X 20% =  1000')
        print('980000 X 25% = 245000')
        print(A-(TB*200),'  X 30% = ',IT[5]-247500)
        print('------------------------------------------')
        print('Income Tax = ',IT[5],'JD(0_0)')
        print('Monethly Income Tax = ',int(IT[5]/12),'JD(0_0)')
'''
Wesam Al-Nobani
'''

