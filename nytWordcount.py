import requests, json, pprint, csv, os

os.chdir(r'C:\Users\micha.DESKTOP-U2HVTMF\MyPythonScripts\VSCode Workspace\API Testing')

#makes request to NYT archive, depending on year/month
response = requests.get('https://api.nytimes.com/svc/archive/v1/2020/8.json?api-key=kHwfza4Tg6ijTQQ9mBQHAi8LeDJaUEAw')
print(response.status_code)

#changes response to json dict
data = response.json()

#creates list for headlines
headlines = []

#gathers headlines from the json dictionary, adds to list
articles = data['response']['docs']
for index in articles:
    headlines.append((index.get('headline').get('main')))

#print(headlines)

#puts top 100 most used words into a list
top100 = []
for word in open('top100.txt'):
    word.lower()
    top100.append(word.rstrip('\n'))

#splits words and adds them into a dictionary, doesn't add if word in top 100 used words
wordCount = {}
for title in headlines:
    wordsList = title.split()
    for word in wordsList:
        wordLower = word.lower()
        if wordLower not in top100:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

#sorts dict of wordcounts
wordCountSorted = sorted(wordCount.items(), key=lambda x: x[1], reverse = True)

#writing list to csv
print(type(wordCountSorted))
with open('nytOutput.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for index in wordCountSorted:
        writer.writerow([index[0], index[1]])