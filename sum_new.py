

x = [10, 20, 30, 40, 50, 60, 1000]

result = x[0] + x[1] + x[2] + x[3] # 10 + 20 + 30

result_new = 0
for xi in x:
    # xi = 10       first iteration
    # xi = 20       second iteration
    # xi = 30       third iteration    
    print(xi)
    result_new = result_new + xi


N = len(x) 
counter = 0
while counter < N:
    xi = x[counter]
    counter = counter + 1


print("the result: ", result_new)