
    
for i in range(11):
    print(i)
    
    
test=[5,7,9]
'''
for i in test:
    print(i)
test[0]=test[0]+1
test[1]=test[1]+1
test[2]=test[2]+1
   ''' 
for i in range(3):
    test[i]=test[i]+1
print(test)


for i in range(len(test)):
    test[i]=test[i]+1
print(test)
#for i in range(11):
#    print(i)

print(list(map(lambda x : x+1,test)))