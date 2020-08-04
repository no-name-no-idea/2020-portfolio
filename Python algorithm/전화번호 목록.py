def solution(phone_book):
    phone_book.sort()
    
    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp in phone_book and temp != phone_num:
                return False
    return True
