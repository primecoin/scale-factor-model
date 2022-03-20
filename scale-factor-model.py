import requests

def get_diff(Str) :
    Str = Str[3:]
    Int = 0
    Float = 0
    flag = 0
    temp = 1 / 16
    for i in Str :
        if i == '.' :
            flag = 1
        elif flag == 0 :
            if i >= '0' and i <= '9' :
                num = int(i) - int('0')
            elif i >= 'a' and i <= 'e' :
                num = ord(i) - ord('a') + 10
            else :
                num = ord(i) - ord('A') + 10
            Int = Int * 16 + num
        elif flag == 1 :
            if i >= '0' and i <= '9' :
                num = ord(i) - ord('0')
            elif i >= 'a' and i <= 'e' :
                num = ord(i) - ord('a') + 10
            else :
                num = ord(i) - ord('A') + 10
            Float = Float + num * temp
            temp = temp / 16
    return Int + Float
    

if __name__=="__main__":
    headers = {"content-type": "application/json"}
    url = "https://explorer.primecoin.net/api/rest/blockchain/getblock/"
    cnt_10 = 0
    cnt_11 = 0
    cnt_12 = 0
    cnt_13 = 0
    for i in range(4650595, 4651595): #4651595
	    response = requests.get(url + str(i), headers = headers).json()
	    difficulty = response["result"]["difficulty"]
	    primechain = response["result"]["primechain"]
	    diff = get_diff(primechain)
	    print(diff)
	    print(difficulty)
	    if diff >= 13 and diff < 14 :
	        cnt_13 += 1
	    if diff >= 12 and diff < 13 :
	        cnt_12 += 1
	    if diff >= 11 and diff < 12 :
	        cnt_11 += 1
	    elif diff >= 10 and diff < 11 :
                if difficulty >= 10 and difficulty < 11:
                    cnt_10 += 1 / (11 - difficulty)
                else :
                    cnt_10 += 1 
    print(cnt_10)
    print(cnt_11)    
    print(cnt_12)
    print(cnt_13)
    
