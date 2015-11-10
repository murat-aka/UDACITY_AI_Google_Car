#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    #
    #ADD YOUR CODE HERE
    q=[]
    for i in range(len(p)):
        if(world[i]==Z):
            p[i]=p[i]*pHit
        else:
            p[i]=p[i] * pMiss
        
        q.append(p[i])
        
    return q
    #
    
print sense(p,Z)
