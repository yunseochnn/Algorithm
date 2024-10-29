
for test_case in range(1, 11):
    result = 0
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(2,N-2):
        left = max(arr[i-2],arr[i-1])
        right = max(arr[i+1],arr[i+2])
        m_value = max(left,right)
        if arr[i] > m_value:
        	result += arr[i] - m_value
    print(f'#{test_case} {result}')
                                 
    
  