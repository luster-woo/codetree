def palindrome(arr,n):
    for i in range(n):
        if arr[i] == arr[n-i-1]:
            continue
        else:
            return "No"
    return "Yes" 
A = input()
result = palindrome(A,len(A))
print(result)
