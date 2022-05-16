


cid = input()
i = 0
s = 0

for i in range(12):
    
    s += (13-i)*int(cid[i])
   

n12 = (11-(s%11))%10
print(cid[0], cid[1:5], cid[5:10], cid[10:12], n12)



