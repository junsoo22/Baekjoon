from collections import deque
import sys

input = sys.stdin.readline
n,w,l=map(int,input().split())

trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
bridge_weight = 0
time = 0

while trucks or bridge_weight > 0:
    time += 1

    # 다리에서 트럭 나감
    bridge_weight -= bridge.popleft()


    if trucks:
        if bridge_weight + trucks[0] <= l:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)

print(time)