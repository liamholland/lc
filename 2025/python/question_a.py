def get_grade(result):
    grade = "Unknown"

    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:          # iii
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    else:
        grade = "Unsuccessful"

    return grade

# Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] # Initialise the list
N = len(results) # Initialise N to the number of results
total = 0 # Initialise the running total to 0

# Loop N times
for i in range(N):
    total = total + results[i] # Running total

# Divide by the total number of results to give the mean
arithmetic_mean = total/(len(results))      # ii

# i
arithmetic_mean = round(arithmetic_mean, 2)

# Display the answer
print("The mean percentage mark is", arithmetic_mean)

# iv
grade = get_grade(arithmetic_mean)

print("The grade for the average result is", grade)

# v
min_result = min(results)
max_result = max(results)

print(f"The lowest score is {min_result}\nThe highest score is {max_result}")

# vi
below_forty_count = len([r for r in results if r < 40])                             # a
between_fifty_and_seventy_nine = len([r for r in results if r >= 50 and r <= 79])   # b

print(f"The number of scores below 40 is {below_forty_count}\nThe number of scores between 50 and 79 is {between_fifty_and_seventy_nine}")

# vii
def get_longest_increasing_run(results):
    longest = []
    run = [results[0]]  # the first value will always be added, and we want to easily check the previous value during iteration

    i = 1
    while i < len(results):
        if results[i] > results[i - 1]: # as above, i - 1 would crash if we started at 0
            run.append(results[i])
        elif len(run) > len(longest):   # assuming that equal lengths do not supercede previous best
            longest = run
            run = [results[i]]
        else:
            run = [results[i]]
        
        i = i + 1

    return longest

longest_run = get_longest_increasing_run(results)

print(f"The longest run of increases is {longest_run}")