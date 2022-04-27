import numpy as np

prices = [25, 30, 45]
dailysales = [[75, 120 ,70 ,90 ,80],
           [80 ,90, 100 ,70, 50],
            [50, 45, 70, 65, 50]]
breakeven = 7500           

def report(prices, dailysales, breakeven) :
    days = ["MO", "TU", "WE", "TH", "FR"]
    menus = ["Curry Rice", "Fried Rice", "Seafood Suki"]
    dailyincomes = np.dot (prices, dailysales)
    for i in range (len (days)):
        print (days [i], '-->', dailyincomes [i])
    print("weekly income =", np.sum (dailyincomes))
    print("daily average =", np.mean (dailyincomes))
    print("Best sales day =", days [np.argmax (dailyincomes)])
    
    loss = np.array (days) [dailyincomes < breakeven]
    print("Sales loss on:", ", ".join (loss))
    print("-------")
    menuincomes = np.sum (dailysales, axis=1) *prices
    for i in range (len (menus)) :
        print (menus[i], '-->', menuincomes [i])
    print("Best menu =", menus [np.argmax (menuincomes) ])

report(prices, dailysales, breakeven)