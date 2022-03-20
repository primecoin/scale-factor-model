import requests

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
	    primeChain = response["result"]["primechain"]
	    chainLens = int(primeChain[3:5], 16)
	    print(chainLens)
	    print(difficulty)
	    if chainLens == 13 :
	        cnt_13 += 1
	    elif chainLens == 12 :
	        cnt_12 += 1
	    elif chainLens == 11 :
	        cnt_11 += 1
	    elif chainLens == 10 :
                if difficulty >= 10 and difficulty < 11:
                    cnt_10 += 1 / (11 - difficulty)
                else :
                    cnt_10 += 1 
    print(cnt_10)
    print(cnt_11)    
    print(cnt_12)
    print(cnt_13)
    
