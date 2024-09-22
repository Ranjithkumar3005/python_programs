def min_time_to_complete_tasks(tasks):
    total_sum = sum(tasks) 
    prefix_sum = 0
    min_time = float('inf')
    
    for i in range(len(tasks)):
        prefix_sum += tasks[i]  
        time_processor_1 = prefix_sum
        time_processor_2 = total_sum - prefix_sum
        min_time = min(min_time, max(time_processor_1, time_processor_2))
    
    return min_time

# Example usage
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(min_time_to_complete_tasks(A))
