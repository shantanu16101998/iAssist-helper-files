import requests
import json

# enter the hostname
url = 'https://api.tickertape.in'

# enter the path of wordlistfile
wordlistFilePath = 'wordlist.txt'


# enter the type of scan
"""
    200 only - only shows pages having 200 as status code
    not 404 - only shows pages which is not having 404 mark
    success info - shows sucess info
"""

typeOfScan = "not 404";


wordListLines = open(wordlistFilePath,"r").readlines();

for i in range(0,len(wordListLines)):
    word = wordListLines[i].replace("\n","");

    response = requests.get(url + "/" + word);

    if typeOfScan == "200 only":
        if response.status_code == 200:
            print("+ " + "[" + str(response.status_code) + "]"  + " " + url + "/" + word);
    
    elif typeOfScan == "not 404":
        if response.status_code != 404:
            if response.status_code == 200:
                print("+ " + "[" + str(response.status_code) + "]"  + " " + url + "/" + word);
            else:
                print("- " + "[" + str(response.status_code) + "]"  + " " + url + "/" + word);

    elif typeOfScan == "success info":
        if response.status_code != 404:
            try:
                responseArray = json.loads(response.text)
                success = responseArray['success']
                if response.status_code == 200:
                    print("+ " + "[" + str(response.status_code) + "]" + "[ sucess = "  + str(success) + " ]"  + " " + url + "/" + word);
                else:
                    print("- " + "[" + str(response.status_code) + "]" + "[ sucess = "  + str(success) + " ]"  + " " + url + "/" + word);

            except Exception as e:
                print(e)

