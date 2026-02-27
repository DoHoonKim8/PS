def char_to_num(char):
    if char == 'A':
        return 0
    if char == 'E':
        return 1
    if char == 'I':
        return 2
    if char == 'O':
        return 3
    if char == 'U':
        return 4

def solution(word):
    answer = 0
    chars = list(word)
    steps = [781, 156, 31, 6, 1]
    for i in range(len(chars)):
        answer += char_to_num(chars[i]) * steps[i]
    answer += len(chars)
    return answer
