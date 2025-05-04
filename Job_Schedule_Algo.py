def printJobScheduling(arr, t):
    # Sort jobs based on profit in descending order
    arr.sort(key=lambda x: x[2], reverse=True)
    
    result = [False] * t  # To track free time slots
    job = ['-1'] * t  # Store job sequence
    
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:  # If the slot is free
                result[j] = True
                job[j] = arr[i][0]  # Assign job to the slot
                break
    
    # Print the job sequence
    print("Following is the maximum profit sequence of jobs:")
    print(" -> ".join(job))

# Driver code
arr = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
       ['d', 1, 25], ['e', 3, 15]]
printJobScheduling(arr, 3)
