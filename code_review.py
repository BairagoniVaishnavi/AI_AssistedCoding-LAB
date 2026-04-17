#Basic code 
def calc(x,y):
 if x>0:
  if y>0:
   return x+y
  else:
   return 0
 else:
  return -1
 
 #Improved code 
 def calc(x, y):
    if x > 0:
        if y > 0:
            return x + y
        else:
            return 0
    else:
        return -1


def calculate_sum_if_positive(num1, num2):
    """
    Returns:
    - Sum if both numbers are positive
    - 0 if first is positive but second is not
    - -1 if first number is not positive
    """

    if num1 <= 0:
        return -1

    if num2 <= 0:
        return 0

    return num1 + num2


# Test cases (must be AFTER function)
print(calculate_sum_if_positive(5, 3))   # 8
print(calculate_sum_if_positive(5, -2))  # 0
print(calculate_sum_if_positive(-1, 3))  # -1