"""
    #1546
    Sam f*ed up his test. Sam decided to pick max score from his tests, call this M, and fixed all test scores/M * 100.
    For example, Sam's max score is 70, and his other score is 50. Then his 50 becomes 50/70*100=71.43

    First line input: number of test scores
    Second line input: test scores
    Output: New average of test scores
"""





n = int(input())
lst = list(map(int,input().split()))
m = max(lst) # using the max function
for i in range(n):
    lst[i] = lst[i]/m*100 # updating test scores

sum_scores = sum(lst)
avg_score = sum_scores/n
print(avg_score)
