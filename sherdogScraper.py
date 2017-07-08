#!/usr/bin/python
from bs4 import BeautifulSoup
import requests, Fighter, re
Soup = BeautifulSoup

baseUrl = "http://www.sherdog.com/fighter/"
fighterIndex = 1
fighterUrl = baseUrl + str(fighterIndex)

pageload = requests.get(fighterUrl)
pageContents = Soup(pageload.content, "html5lib")

print(fighterIndex)

fighterName = pageContents.find('span', class_ = 'fn').getText()
print('Fighter name: %s' % fighterName)

#fighterNickname = pageContents.find('span', class_ = 'nickname').getText()
#print(fighterNickname)

fighterBirthday = pageContents.find('span', class_ = 'item birthday').span.getText()
print("Birthday: %s" % fighterBirthday)

fighterAge = pageContents.find('span', class_ = 'item birthday').strong.getText()
fighterAgeInt = str(fighterAge).lstrip('AGE: ')
print(fighterAgeInt)

fighterHeightUS = pageContents.find('span', class_ = 'item height').strong.getText()
print(fighterHeightUS)

fighterWeightUS = pageContents.find('span', class_ = 'item weight').strong.getText()
fighterWeightUSInt = str(fighterWeightUS).rstrip(' lbs')
print(fighterWeightUSInt)

weightclass = pageContents.find('h6', class_ = 'item wclass').strong.getText()
print(weightclass)

fighterAddress = pageContents.find('span', class_ = 'locality').getText()
print(fighterAddress)

fighterCountry = pageContents.find('span', class_ = 'item birthplace').strong.getText()
print(fighterCountry)

winRecord = pageContents.find('div', class_ = 'left_side').div.find('span', class_ = 'counter').getText()
print(winRecord)

loseRecord = pageContents.find('div', class_ = 'bio_graph loser').find('span', class_ = 'counter').getText()
print(loseRecord)

drawRecord = pageContents.find('div', class_ = 'right_side').div.find('span', class_ = 'counter').getText()
print(drawRecord)

wKO = pageContents.find('div', class_ = 'bio_graph').contents[5].getText()
print(wKO)

wSub = pageContents.find('div', class_ = 'bio_graph').contents[9].getText()
print(wSub)

wDec = pageContents.find('div', class_ = 'bio_graph').contents[13].getText()
print(wDec)

lKO = pageContents.find('div', class_ = 'bio_graph loser').contents[5].getText()
print(lKO)

lSub = pageContents.find('div', class_ = 'bio_graph loser').contents[9].getText()
print(lSub)

lDec = pageContents.find('div', class_ = 'bio_graph loser').contents[13].getText()
print(lDec)

#print(pageContents.find('div', {"class" : "bio_graph loser"}).findChild('span', {'class':'result'}))

recordTable = pageContents.find('div', {"class" : "content table"}).tbody
tableHead = recordTable.findChild('tr', {'class':'table_head'})
tableRows = recordTable.findAll(class_ = {'odd','even'})
#print(recordTable)

#print(tableHead)
#print(len(tableHead.findChildren()))

fightRecord = []

for row in tableRows:
    cells = row.findAll('td')
    result = cells[0].getText()
    opponent = cells[1].getText()
    eventName = cells[2].find('a').getText()
    eventUrl = cells[2].find('a').get('href')
    eventDate = cells[2].find('span', {'class':'sub_line'}).getText()
    method = cells[3].next
    referee = cells[3].next.next.next.getText()
    resultRound = cells[4].getText()
    finalRoundTime = cells[5].getText()
    #print("%s, %s, %s, %s, %s, %s, %s, %s, %s" % (result, opponent, eventName, eventUrl, eventDate, method, referee, resultRound, finalRoundTime))
    rowList = [result,opponent,eventName,eventUrl,eventDate,method,referee,resultRound,finalRoundTime]
    fightRecord.append(rowList)

for record in fightRecord:
    for i in range(len(record)):
        print record[i]
