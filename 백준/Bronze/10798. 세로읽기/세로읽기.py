arr = [input() for _ in range(5)]
max_len = max(len(element) for element in arr)
result = ""
for i in range(max_len):
    for j in range(5):
        if i < len(arr[j]):
            result+=arr[j][i]
print(result)