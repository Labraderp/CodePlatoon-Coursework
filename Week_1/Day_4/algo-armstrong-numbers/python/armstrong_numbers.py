results = []
for i in range(len(arr)):
    string_num = str(arr[i])
    n = len(string_num)
    answer = 0
    for num in range(len(string_num)):
        new_num = int(string_num[num])
        answer += new_num ** n
    if answer == arr[i]:
        results.append(answer)

    return results

print(armstrong_number((list(range(0,999)))))