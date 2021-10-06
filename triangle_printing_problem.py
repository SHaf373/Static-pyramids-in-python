print('(a)')
for i in range(11):
    print(i*'*')
print()
print('(b)')
for i in range(10,0,-1):
    print(i*'*')
print('')
print('(c)')
for i in range(10,0,-1):
        print((10-i)*" ",i*"*")
print('')
print('(d)')
for i in range(11):
    print((10-i)*" ",i*"*")
print('')
print('(e)')
for i in range(11):
    print((10-i)*" ",i*"*",i*"*",sep='' )
for i in range (10,0,-1):
    print((10-i)*" ",i*"*",(i)*"*",sep='')
    
    
    
    
input('enter to continue:..........')
