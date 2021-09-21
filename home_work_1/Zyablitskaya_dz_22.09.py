stro = input()
save = ['o']
k = 0
for i in range(0, len(stro), 1):
    if (stro[i] == '(' or stro[i] == '[' or stro[i] == '{'):
        save.append(stro[i])
    else :
        lel = save[-1]
        if ((stro[i] == ')' and lel =='(') or (stro[i] == ']' and lel =='[') or (stro[i] == '}' and lel =='{')):
            save.pop()
        else:
            if (stro[i] == ')'  or stro[i] == ']'  or stro[i] == '}'):
                 k = -12
            

            
if ( save[-1] == 'o' and k!=-12 ): 
    print('correct')
else:
    print('incorrect')
  
    
    

    
   
          
        