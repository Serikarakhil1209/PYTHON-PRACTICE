#Break

for i in range(1,20):
    if i==5:
        break
    print(i)


for i in range(1,21):
    print("akki")
     
    break

for i in range(1,20):
    print("akki")
    if i<=10:
        break

#continue--> while hiting on the continue statement it will skip the that itteration. 

for i in range(1,20):
    print(i)
    continue


#both
for i in range(1,20):
    print(i) #print 1to 19
    continue #it will not go for the next line and it will go back
    print(i) #print nothing
    break #it will not go in side the break statement 

for i in range(1,20):
    print(i) #print 1
    break #it will not go for the next line and it will stop
    print(i) #print nothing
    continue 

#Nested loops 
for i in range(1,11):
    # if i==5;
    #    break     ** loop will stop here only it will not go further
    for j in range(1,31):
        if j ==16:
            break # inner loop will be stop when the condition satify and after that outer loop will continue itteratio  
        print(i,j)

for i in range(1,11):
    if i%2==0:
        for j in range(1,31):
            if j >= 16:
               break
            print(i,j)
    else:
        for j in range(1,31):
            print(i,j) 
        
        
        

    
    
    
