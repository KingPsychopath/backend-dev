from heapq import *

def getServerIndex(n, arrival, burstTime):
    m = len(arrival)
    available_servers = list(range(1, n + 1))
    process = []
    heapify(available_servers)
    ans = [0] * m

    for a, i, b in sorted(zip(arrival, list(range(m)), burstTime)):
        while process and process[0][0] <= a:
            heappush(available_servers, heappop(process)[1])
        if available_servers:
            server = heappop(available_servers)
            ans[i] = server
            heappush(process, (a + b, server))
        else:
            ans[i] = -1

    return ans

# Example usage
n = 4
arrival = [3, 5, 1, 6, 8]
burstTime = [9, 2, 10, 4, 5]
print(getServerIndex(n, arrival, burstTime))

n = 2
arrival = [2, 2, 2, 3]
burstTime= [11, 3, 1, 2]
print(getServerIndex(n, arrival, burstTime))

# Test the function
n = 3
arrival = [2, 4, 1, 8, 9]
burstTime = [7, 9, 2, 4, 5]
print(getServerIndex(n, arrival, burstTime))  # Expected output: [1, 2, 1, 3, 2]