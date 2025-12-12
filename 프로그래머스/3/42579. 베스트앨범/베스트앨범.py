from collections import defaultdict

def solution(genres, plays):
    genre_total=defaultdict(int)
    genre_songs=defaultdict(list)
    for i in range(len(genres)):
        genre=genres[i]
        play=plays[i]
        
        genre_total[genre]+=play
        genre_songs[genre].append((play,i))
    print(genre_total)
    print(genre_songs)
      # 2️⃣ 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda x: -genre_total[x],
        # reverse=True
    )
    print(sorted_genres)
    answer=[]
     # 3️⃣ 각 장르에서 상위 2곡 선택
    for genre in sorted_genres:
        # 재생 수 ↓, 고유번호 ↑
        songs = sorted(
            genre_songs[genre],
            key=lambda x: (-x[0], x[1])
        )
        for play, idx in songs[:2]:
            answer.append(idx)
    
    return answer