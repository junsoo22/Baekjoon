for tc in range(1, 11):
    n = int(input())  # 원본 암호문 길이
    arr = list(map(int, input().split()))  # 암호문 리스트

    k = int(input())  # 명령어 개수
    commands = input().split()  # 모든 명령을 한 줄로 받음
    idx=0
    for i in range(k):
        cmd=commands[idx]
        idx+=1
        if cmd=='I':  #삽입
            x=int(commands[idx])
            y=int(commands[idx+1])
            idx+=2
            s=list(map(int, commands[idx:idx+y]))
            idx+=y
            arr=arr[:x]+s+arr[x:]  # x 위치에 s 삽입
        elif cmd=='D':  #삭제
            x=int(commands[idx])
            y=int(commands[idx+1])
            idx+=2
            arr=arr[:x]+arr[x+y:]  # x부터 y개 삭제
        elif cmd=='A':  #추가
            y=int(commands[idx])
            idx+=1
            s=list(map(int, commands[idx:idx+y]))
            idx+=y
            arr=arr+s  # 맨 뒤에 s 추가
    
    print(f"#{tc}", *arr[:10])  
