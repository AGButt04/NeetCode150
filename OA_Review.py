# Online Assessment Preparation and Review
import math
from collections import defaultdict

def longestSubarray1(nums: list[int], k: int) -> int:
    length = len(nums)
    if length <= 0:
        return 0

    max_subarray = 0

    for i in range(length):
        curr_sum = 0
        for j in range(i, length):
            curr_sum += nums[j]

            if curr_sum == k:
                max_subarray = max(max_subarray, j - i + 1)

    return max_subarray

def longestSubarray(nums: list[int], k: int) -> int:
    # Efficient Version
    length = len(nums)
    if length <= 0:
        return 0

    prefix_sums = { 0 : -1 }
    pre_sum = 0
    max_subarray = 0
    for i in range(length):
        pre_sum += nums[i]

        if pre_sum - k in prefix_sums:
            max_subarray = max(max_subarray, i - prefix_sums[pre_sum - k])
        if pre_sum not in prefix_sums:
            prefix_sums[pre_sum] = i

    return max_subarray

def lengthOfLongestSubstring(s: str) -> int:
    map = {}
    left, right = 0, 0
    longest_arr = 0

    while right < len(s):
        char = s[right]

        if char in map:
            left = max(left, map[char] + 1)

        map[char] = right
        longest_arr = max(longest_arr, right - left + 1)
        right += 1

    return longest_arr

def minWindow(s: str, t: str) -> str:
    t_map = defaultdict(int)
    required_chars = len(t)
    min_win = None
    left = 0

    for c_t in t:
        t_map[c_t] += 1

    for right, c_s in enumerate(s):
        if c_s in t_map:
            t_map[c_s] -= 1
            if t_map[c_s] >= 0:
                required_chars -= 1

        while required_chars == 0:
            curr_win = s[left: right + 1]
            
            if min_win is None or len(curr_win) < len(min_win):
                min_win = curr_win

            if s[left] in t_map:
                t_map[s[left]] += 1

                if t_map[s[left]] > 0:
                    required_chars += 1

            left += 1

    return "" if min_win is None else min_win

def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left)// 2
        num = nums[mid]

        if num > nums[right]:
            left = mid + 1
        elif num <= nums[right]:
            right = mid

    return nums[right]

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temperatures)

    for idx, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            t, old_id = stack.pop()
            answer[old_id] = idx - old_id

        stack.append((temp, idx))

    return answer

def detectAnomalies(transactions: list[tuple[str, int, int]], W: int, T: int) -> list[str]:
    data_map = {}
    anamolies = []

    for tran in transactions:
        key, time, trans = tran[0], tran[1], tran[2]

        if key not in data_map:
            data_map[key] = [(time, trans)]
        else:
            data_map[key].append((time, trans))

    for user, time_tran in data_map.items():
        anomaly = False
        total = 0
        left = 0

        for ti, tr in time_tran:
            curr_window = ti - time_tran[left][0]
            total += tr
            
            while curr_window > W:
                total -= time_tran[left][1]
                left += 1
                curr_window = ti - time_tran[left][0]

            if curr_window <= W and total > T:
                anomaly = True
                break

        if anomaly: 
            anamolies.append(user)

    return sorted(anamolies)

def largestOnlineNetwork(n: int, connections: list[list[int]], failed: list[int]) -> int:
    graph = {}
    max_network = 0
    visited = set()
    failed = set(failed)

    for a, b in connections:
        if a not in failed:
            if a not in graph and b not in failed:
                graph[a] = [b]
            elif b not in failed:
                graph[a].append(b)

        if b not in failed:
            if b not in graph and a not in failed:
                graph[b] = [a]
            elif a not in failed:
                graph[b].append(a)

    for start in graph.keys():
        if start in visited:
            continue

        stack = [start]
        visited.add(start)
        curr_network = 0

        while stack:
            curr = stack.pop()
            neighbors = graph[curr]
            curr_network += 1

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        max_network = max(max_network, curr_network)

    if n > len(failed):
        max_network = max(max_network, 1)

    return max_network

    

if __name__ == '__main__':
    # Test 1 — Basic disconnected networks
    n = 7
    connections = [[0,1], [1,2], [2,3], [4,5], [5,6], [3,4]]
    failed = [2,5]
    print(largestOnlineNetwork(n, connections, failed))

    # Test 2 — No failed servers
    n = 5
    connections = [[0,1], [1,2], [3,4]]
    failed = []
    print(largestOnlineNetwork(n, connections, failed))


    # Test 3 — All servers offline
    n = 4
    connections = [[0,1], [1,2], [2,3]]
    failed = [0,1,2,3]
    print(largestOnlineNetwork(n, connections, failed))


    # Test 4 — Isolated online servers
    n = 5
    connections = []
    failed = [1,3]
    print(largestOnlineNetwork(n, connections, failed))


    # Test 5 — Failed server breaks connectivity
    n = 6
    connections = [[0,1], [1,2], [2,3], [3,4], [4,5]]
    failed = [2]
    print(largestOnlineNetwork(n, connections, failed))


    # Test 6 — Cycle with one failed server
    n = 5
    connections = [[0,1], [1,2], [2,3], [3,0], [3,4]]
    failed = [1]
    print(largestOnlineNetwork(n, connections, failed))


    # Test 7 — Only one server
    n = 1
    connections = []
    failed = []
    print(largestOnlineNetwork(n, connections, failed))
