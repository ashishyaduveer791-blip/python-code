# WAP to input a list of scores for N students in a list data type. Find the score of the runner
# up and print the output. 
# Sample Input 
# N = 5 
# Scores= 2 3 6 6 5 
# Sample output 
# 5 
# Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, 
# we print 5 as the runner-up score. 
# 
    
   
# Take number of students
N = int(input("Enter number of students: "))

# Take scores
scores = []
for i in range(N):
    num = int(input("Enter score: "))
    scores.append(num)

# Remove duplicate values
unique_scores = []
for s in scores:
    if s not in unique_scores:
        unique_scores.append(s)

# Find highest score
highest = max(unique_scores)

# Remove highest score
unique_scores.remove(highest)

# Find second highest (runner-up)
runner_up = max(unique_scores)

# Print result
print("Runner-up score is:", runner_up)

