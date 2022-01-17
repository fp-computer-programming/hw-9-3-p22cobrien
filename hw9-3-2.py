# Author: CMOB 1/17/2022

try:
    print('Enter the net sales for')
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print("Please input a number.")

except ZeroDivisionError: 
    print("Please use numbers other than just zeros")
