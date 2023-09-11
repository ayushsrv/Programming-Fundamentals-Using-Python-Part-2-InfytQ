

def check_numbers(num1,num2):
    num_list=set()
    
    for label in range(num1, num2 + 1):
        for divisor in range(num1, num2 + 1):
            if label != divisor and label % divisor == 0:
                num_list.add(label)
    count=len(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))