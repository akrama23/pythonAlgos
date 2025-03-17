#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places
ia = int(input())
ib = int(input())
ic = int(input())

eA = 15.62 * ia
eB = 41.85 * ib
eC = 32.67 * ic

print(f'Distance: {(eA + eB + eC):.2f} miles')