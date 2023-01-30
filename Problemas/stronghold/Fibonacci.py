def Fibonacci_Loop_Pythonic(months, offsrpings):
    parrent, child = 1, 1
    for itr in range(months - 1):
        child, parrent = parrent, parrent + (child * offsrpings)
    return child

print(Fibonacci_Loop_Pythonic(33, 3))
