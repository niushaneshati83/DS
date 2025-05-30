data = []
list_ans = []

n, d = list(map(int, input().split()))

for i in range(n):
    a, t, s = input().split()
    data.append((int(a), int(t), int(s)))

data.sort(key=lambda x: x[2], reverse=True)
stack = [0 for i in range(d)]  # days

total_cost = 0
for i in range(n):  # teachers
    # pdb.set_trace()
    start_day_i, num_days_i, cost_i = data[i]
    counter_days = 0
    counter_j = start_day_i - 1
    while counter_days < num_days_i and counter_j < d:
        if stack[counter_j] == 0:
            stack[counter_j] = 1
            counter_days += 1
        counter_j += 1
    if num_days_i > counter_days:
        total_cost += cost_i * (num_days_i - counter_days)


print(total_cost)