def print_transaction(money, _name, _owned, _prices):
    
    decision = []
    output = []
    
    for i in range(len(_name)):        
        owned, prices = _owned[i], _prices[i]
        avg = avg_list(prices[:-1])
        
        margin = prices[-1] - avg
        decision.append((i, owned, margin))
        
    decision_sorted = sorted(decision, key=lambda tup: tup[2])
    
    
    for i in decision_sorted:
        index, owned, margin = i
        if((-1)*margin > 0 and money > 0):
            last_price = _prices[index][-1]            
            units = int(money/last_price)                
            if units > 0: 
                #print "appending"
                money -= units * last_price
                output.append((_name[index], "BUY", units))            
        elif(margin > 0 and owned > 0):
            #print "appending"
            output.append((_name[index], "SELL", owned))
    
    print len(output)
    for t in output:
        print_decision(t[0], t[1], t[2])
    return

def print_decision(name, decision, units):
    print "%s %s %s" % (name, decision, units)

def avg_list(list):
    return reduce(lambda x, y: x + y, list) / len(list)

if __name__ == '__main__':
    _in = raw_input().split()
    _m = float(_in[0])
    _k, _d = (int(i) for i in _in[1:])
    _name, _owned, _prices = ['']*_k, [0]*_k, [[]]*_k
    
    for i in range(_k):
        name, owned, prices = raw_input().split(' ',2)        
        _name[i], _owned[i] = name, int(owned)
        _prices[i] = [float(j) for j in prices.split()]        
    
    print_transaction(_m, _name, _owned, _prices)
    
