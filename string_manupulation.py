def FindNumber(text):
    result=""
    isdigitStart=False
    for ch in text:
        if ch.isdigit():
            result+=ch
            isdigitStart=True
        else:
            if(isdigitStart):
                break
    if not(isdigitStart):
        return 0
    return int(result)

