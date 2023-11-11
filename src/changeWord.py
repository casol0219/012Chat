#금칙어 리스트
forbidden_words = ["시발", "미친", "꺼져", "놈"]

def changeWord(message):
    for word in forbidden_words:
        if word in message:
            replacement = '@' * len(word)   #금칙어에 걸린 문자열의 길이만큼 '@'로 대체
            message = message.replace(word, replacement)
    return message
