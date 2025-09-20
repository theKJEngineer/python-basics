

def convertToSeconds(h,m):
    hToS = h * 60 * 60
    mTos = m * 60
    result = hToS + mTos
    return result

print(convertToSeconds(3, 25))

def convertToHours(m):
    result = m / 60
    return result

print(convertToHours(120))
