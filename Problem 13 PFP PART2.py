

def close_number(num1,num2,num3):
    #start writing your code here
    if abs(num1-num2)<=1 and abs(num2-num3)>=2 and abs(num1-num3)>=2:
      return True
    if abs(num2-num3)<=1 and abs(num1-num2)>=2 and abs(num1-num3)>=2:
      return True
    if abs(num3-num1)<=1 and abs(num2-num3)>=2 and abs(num2-num1)>=2:
      return True

    return False
print(close_number(5,4,2))