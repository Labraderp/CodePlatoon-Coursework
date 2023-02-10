def armstrong_number(arr):

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

def new_arm(arr):
    results = []

    for num in arr:
        total = 0
        for i in str(num):
            total += int(i) ** len(str(num))
        
        if total == int(num):
            results.append(total)

    return results
        

print(armstrong_number((list(range(0,999)))))
print(new_arm((list(range(0,999)))))