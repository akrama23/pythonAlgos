def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return(f'{((miles_driven / miles_per_gallon) * dollars_per_gallon):.2f}')

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    
    print(driving_cost(miles_per_gallon, dollars_per_gallon, 10))
    print(driving_cost(miles_per_gallon, dollars_per_gallon, 50))
    print(driving_cost(miles_per_gallon, dollars_per_gallon, 400))

