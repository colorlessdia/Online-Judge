import sys
from heapq import heappush, heappop

def add_client(waiting_list, priority, client):
    heappush(waiting_list, (priority, client))

def del_client(wating_list, client_state):
    served_client = []

    while wating_list:
        _, client = heappop(wating_list)

        if not client_state[client]:
            continue
        
        served_client.append(client)
        client_state[client] = 0
        break
    
    return served_client

input = sys.stdin.readline

asc_waiting_list = []
des_waiting_list = []
client_state = dict()

while 1:
    line = list(map(int, input().split()))
    command = line[0]

    if command == 0:
        break
    
    if command == 1:
        client = line[1]
        priority = line[2]

        add_client(asc_waiting_list, priority, client)
        add_client(des_waiting_list, -priority, client)

        client_state[client] = 1
        continue
        
    if command == 2:
        served_client = del_client(des_waiting_list, client_state)

        if served_client:
            print(*served_client)
        else:
            print(0)

        continue
        
    if command == 3:
        served_client = del_client(asc_waiting_list, client_state)

        if served_client:
            print(*served_client)
        else:
            print(0)
        
        continue