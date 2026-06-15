# Break used to terminate a loop when encountered.

# continue terminates execution in the current iteration & and continues execution of loop with next iteration.

# Break
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("End of Loop")

# Continue
i = 1
while i <=5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1