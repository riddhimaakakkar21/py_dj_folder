
"J A V A T P O I N T"
'''
[start-point  :  end-point  :  step-count]
Simple basic rule for slicing...

2> --> [start-point  :  end-point]
        Defaultly equals to 1
3> --> reverse indexing , which is in negative state.
In every negative states [-1] step count. Means in reverse negative states have step count default == -1
[]

'''

'0   1    2    3    4    5    6    7     8     9'
"J   A    V    A    T    P    O    I     N     T"
'-10 -9  -8    -7   -6  -5    -4   -3     -2    -1'

# x='JAVATPOINT'

# print(x[-10:-6:]) 





# statement = "this is JS Python Node, I'm doing this for my JavaScript. "
# #  python, code , my, practice, doing
# # print(statement.find("python"))
# # print(statement.find("practice"))
# # print(statement[11:17])
# # print(statement[7:11])
# # print(statement[18:22])
# # print(statement[-11:-2:])
# ListValues = []
# ListValues.extend([statement[11:17],statement[8:11],statement[18:22],statement[-12:-2:]])
# # print(ListValues)
# AmountValues = [23000,18000,12000, 9000]

# fees = {}
# count = 0
# for i in ListValues:
#     fees[i]=AmountValues[count]
#     count+=1
# print(fees)



'''
fucntion new()
list1 = [1,2,3,4,5,6,7,8]
list2 = ['a' ,'b' ,'c' 'd' ,'e', 'f'] 

DIct = {}

list3 = ['z' ,'x','c','v' ,'b','n','m']

function new2(dict)
print(dict)
dict = {key , ['value' , 'value2']}
'''

dict1={}

def fnc1():
    list1 = [1,2,3,4,5,6]
    list2 = ['a' ,'b' ,'c' ,'d' ,'e', 'f']
    print(list1,type(list2))
    count=0
    for i in list1:
        dict1[i]=[list2[count]]
        count+=1
    print(dict1)
fnc1()    

def fnc2(abc ):
    '''{1: ['a'], 2: ['b'], 3: ['c'], 4: ['d'], 5: ['e'], 6: ['f']}'''
    print('---',abc)
    list3 = ['z' ,'x','c','v' ,'b','n']
    count = 0
    for i , j in abc.items():
        print(j)
        j.append(list3[count])
        
        
        #-------------OR---------------


        # j.extend([list3[count]])
        count+=1
    print(abc)
    # for j in abc:
         
fnc2(abc =dict1 )

