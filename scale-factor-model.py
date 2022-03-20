import requests

if __name__=="__main__":
    headers = {"content-type": "application/json"}
    url = "https://explorer.primecoin.net/api/rest/blockchain/getblock/"
    Count = {}
    for i in range(0, 15) :
        Count[i] = 0
    for i in range(4651555, 4651595): #4651595
        response = requests.get(url + str(i), headers = headers).json()
        difficulty = response["result"]["difficulty"]
        primeChain = response["result"]["primechain"]
        chainLength = int(primeChain[3:5], 16)
        print(chainLength)
        print(difficulty)
        if (chainLength == 10) :
            if difficulty >= 10 and difficulty < 11:
                Count[10] += 1 / (11 - difficulty)
            else:
                Count[10] += 1
        else:
            Count[chainLength] += 1
    print(Count)
    
