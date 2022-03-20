import requests

if __name__=="__main__":
    headers = {"content-type": "application/json"}
    url = "https://explorer.primecoin.net/api/rest/blockchain/getblock/"
    count = {}
    for i in range(0, 17) :
        count[i] = 0
    for i in range(4651555, 4651565): #4651595
        response = requests.get(url + str(i), headers = headers).json()
        difficulty = response["result"]["difficulty"]
        primeChain = response["result"]["primechain"]
        chainLength = int(primeChain[3:5], 16)
        print(chainLength)
        print(difficulty)
        if (chainLength == int(difficulty)) :
            count[chainLength] += 1 / (int(difficulty) + 1 - difficulty)
        else:
            count[chainLength] += 1
    print(count)
    
