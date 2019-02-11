import math

#Tax Payable
TP = input('Enter the taxpayable (p_q) :')
# From Date / input - (Date)
FD = input()
# To Date / input - (Date)
TD = input()
#Numbers Days / (sub - result)
ND = TD - FD
# Number Days of Week (Fixed)
NDW = 7
# Ratio Fine (Fixed)
RF = 0.004
# Number Weeks (result)
NW =  ND / NDW
# Number Weeks with part
NWP = math.ceil(NW)
# Value Fine (result)
VF = TP * NWP * RF

print('---------------------------------')
print(NW,'Week' , NWP)
print(VF,'JD(@__@) ')
print(TP + VF,'JD(*__@)')

'''
Wesam Al-Nobani
'''




