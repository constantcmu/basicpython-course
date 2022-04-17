# def total(pocket): 
#     sum_pocket = 0
#     for i in pocket:
#         sum_pocket += i*pocket[i]
#     return sum_pocket


# def take(pocket,money_in):
#     for i in money_in:
#         if i in pocket:
#             pocket[i] += money_in[i]
#         else:
#             pocket[i] = money_in[i]
#     return pocket

# def pay(pocket,amt):
#     money_out = {}
#     for i in sorted(pocket.keys())[::-1]:
#         if amt >= i:
#             c = min(pocket[i],amt//i)
#             money_out[i] = c
#             pocket[i] -=c
#             amt -= i*c

#     return money_out




# p={100:5};take(p,{100:2, 1:3});print(p)




#09-2

# def factor(N):
#     N_list = []
#     k = 2 
#     while k <= N :
#         if N%k == 0:
#             c = 0
#             while N%k == 0:
#                 N //= k
#                 c +=1
#             N_list.append([k,c])

#         k +=1    
            
#     return N_list


#09-3
def read_mtrix():
    m = [ ]
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x :
            r.append(float(e))
        m.append(r)
    return m 

def mult_c(c,A):

    








exec(input().strip( ))