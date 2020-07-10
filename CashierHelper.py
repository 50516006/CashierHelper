import copy
#Coins must be dictionary<int,int> key = value,value = count

#get summary of inputed keys*values

def Summary(coins:dict):
    return sum([i*v for i,v in coins.items()])


def InitWith(f10000,f5000,f1000,c500,c100,c50,c10,c5,c1):
    coins =dict()
    coins[10000]=f10000
    coins[5000]=f5000
    coins[1000]=f1000
    coins[500]=c500
    coins[100]=c100
    coins[50]=c50
    coins[10]=c10
    coins[5]=c5
    coins[1]=c1
    return coins

def CountMaximum(coins:dict,target):
    table = dict()
    table[0]=dict()

    for coinvalue,coincount in coins.items():
        nt = dict()
        for i in range(coincount+1):
            for sumvalue,sumdict in table.items():
                sumcount = sum([i for i in sumdict.values()])
                newcount = sumcount+i
                newvalue = sumvalue+i*coinvalue
                if newvalue > target:
                    continue
                if not newvalue in nt: 
                    newdict = copy.deepcopy(sumdict)
                    newdict[coinvalue]=i
                    nt[newvalue]=newdict
                    continue
                oldcount=sum([i for i in nt[newvalue].values()])
                if newcount > oldcount:
                    newdict = copy.deepcopy(sumdict)
                    newdict[coinvalue]=i
                    nt[newvalue]=newdict
        table = nt
    
    if not target in table:
        return -1
    return table[target]

