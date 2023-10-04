import sys

i = 1

while 1:
    n = int(sys.stdin.readline())
    
    if n == 0: break
    
    song_list = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
    
    print(i)
    for song in song_list:
        print(song)
    
    i += 1