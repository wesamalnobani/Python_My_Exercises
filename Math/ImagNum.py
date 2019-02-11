def imag_number():
    x = float(input('Enter Numbet:'))
    y = x/(x-1)
    print('----------------------------')
    print('Imag Without round =', y)
    print('Imag With round    =',round(y,3))
    print('----------------------------')
    print(x,'+',y,'=',x+y)
    print(x,'x',y,'=',x+y)
imag_number()

