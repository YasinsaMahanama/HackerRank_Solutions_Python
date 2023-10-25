if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Sort the list in descending order
    arr.sort(reverse=True)
    
    # Find the runner-up score
    runner_up = None
    for score in arr:
        if score < arr[0]:
            runner_up = score
            break

    print(runner_up)
