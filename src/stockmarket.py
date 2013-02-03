import pickle

def loadStockHistory(f):
    try:
        d = pickle.load(open(f,"rb"))
    except:
        d = {}
    return d

def writeStockHistory(f, d):
    pickle.dump(d, open(f, "wb"))
    return

def print_transaction(_file, money, _name, _owned, _prices):
    decision = []
    output = []
    
    historicalBuys = loadStockHistory(_file)
    
    for i in range(len(_name)):
        historical_price = None
        if historicalBuys.has_key(_name[i]):
            historical_price = historicalBuys.get(_name[i])
                    
        owned, prices = _owned[i], _prices[i]        
        avg = avg_list(prices[:-1])
        
        if historical_price is not None:
            margin = prices[-1] - (historical_price if historical_price > avg else avg)
        else:
            margin = prices[-1] - avg 
        #margin = prices[-1] - avg
        decision.append((i, owned, margin))
        
    decision_sorted = sorted(decision, key=lambda tup: tup[2])
    
    
    for i in decision_sorted:
        index, owned, margin = i
        name = _name[index]
        if((-1)*margin > 0 and money > 0):
            last_price = _prices[index][-1]            
            units = int(money/last_price)                
            if units > 0: 
                #print "appending"
                money -= units * last_price
                output.append((name, "BUY", units)) 
                historicalBuys[name] = last_price #overwrite historical data.
                            
        elif(margin > 0 and owned > 0):
            #print "appending"
            output.append((name, "SELL", owned))
            if historicalBuys.has_key(name): historicalBuys.pop(name)
    
    print len(output)
    for t in output:
        print_decision(t[0], t[1], t[2])
    
    writeStockHistory(_f, historicalBuys)
    return

def print_decision(name, decision, units):
    print "%s %s %s" % (name, decision, units)

def avg_list(list):
    return reduce(lambda x, y: x + y, list) / len(list)

if __name__ == '__main__':
    _f = "murphy_stockpredictor.tmp"
    _in = raw_input().split()
    _m = float(_in[0])
    _k, _d = (int(i) for i in _in[1:])
    _name, _owned, _prices = ['']*_k, [0]*_k, [[]]*_k
    
    for i in range(_k):
        name, owned, prices = raw_input().split(' ',2)        
        _name[i], _owned[i] = name, int(owned)
        _prices[i] = [float(j) for j in prices.split()]        
    
    print_transaction(_f, _m, _name, _owned, _prices)
    
