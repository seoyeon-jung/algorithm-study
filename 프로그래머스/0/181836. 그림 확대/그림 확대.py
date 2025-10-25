def solution(picture, k):
    answer = []
    new_pic = ''
    new_pic_arr = []
    for pic in picture:
        for pic_i in pic:
            new_pic += pic_i * k
        for _ in range(k):
            new_pic_arr.append(new_pic)
        new_pic = ''
    answer = new_pic_arr
    return answer