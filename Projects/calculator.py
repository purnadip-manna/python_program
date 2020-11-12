opr = "+-*/^"
def priority(ele):
    if ele == '^':
        return 5
    elif ele == '*' or ele == '/':
        return 4
    elif ele == '+' or ele == '-':
        return 3
    else:
        return 2

def evaluation(postlist):
    stack = []
    for x in postlist:
        if x in opr:
            b = float(stack.pop())
            a = float(stack.pop())
            if x == '+':
                stack.append(a+b)
            elif x == '-':
                stack.append(a-b)
            elif x == '*':
                stack.append(a*b)
            elif x == '/':
                stack.append(a/b)
            elif x == '^':
                stack.append(a**b)

        else:
            stack.append(x)

    return (stack.pop())

def postfix(infix):
    p = []
    stack = []
    top = -1
    for x in infix:
        if x == '(':
            top+=1
            stack.append(x)
            
        elif x == ')':
            temp = stack.pop()
            top-=1
            while temp!='(':
                p.append(temp)
                temp = stack.pop()
                top-=1

        elif x in opr:
            while(priority(stack[top])>=priority(x)):
                temp = stack.pop()
                top-=1
                p.append(temp)
            top+=1    
            stack.append(x)

        elif x == '':
            top+=1
            stack.append(x)
        else:
            p.append(x)       
    return p
                

def calculator(s):
    s = '('+s+')'
    s = list(s)
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = '(,'
        elif s[i] == ')':
            s[i] = ',)'
        elif s[i] in opr:
            s[i] = ','+s[i]+','     
        
    exp = ''
    for x in s:
        exp+=x
    exp = list(exp.split(','))
    p_exp = postfix(exp)
    return (evaluation(p_exp))


s = input("Enter the expression: ")
print('Ans:',calculator(s))
