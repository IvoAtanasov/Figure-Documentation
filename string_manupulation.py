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
    return result

print(FindNumber("Step42.teststep1"))
