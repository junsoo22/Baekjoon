def solution(phone_book):
    phone_book.sort()
    # print(phone_book)
    
    for i in range(len(phone_book) - 1):
        # 앞 번호가 뒤 번호의 접두어인지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True