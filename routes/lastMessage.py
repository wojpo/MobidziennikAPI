import requests
from data import (loginUrl, messagesUrl,lastMessageUrl, payload)
from bs4 import BeautifulSoup


async def last_message():
    with requests.session() as uwu:
        uwu.post(loginUrl, data=payload)
        messageSite = uwu.get(messagesUrl)
        soup = BeautifulSoup(messageSite.content, 'html.parser')
        lastMessage = soup.find_all('td')
        title = lastMessage[0]
        sender = lastMessage[3]
        idd = lastMessage[6]
        idd = str(idd)
        idd = idd.replace('<td style="text-align:center;"><input name="skasuj_odebrane[]" rel="','')
        idd = idd[:6]
        lastMessageUrlSite = lastMessageUrl
        lastMessageUrlSite += idd
        LastMessageSite = uwu.get(lastMessageUrlSite)
        soup2 = BeautifulSoup(LastMessageSite.content,'html.parser')
        messageContent = soup2.find_all('p')
        print(messageContent)
        for messageContentUwU in messageContent:
            print(messageContentUwU.text)


    print(title.text)
    print(sender.text)
    print(idd)
    return {
        'title': f'{title.text}',
        'sender': f'{sender.text}',
        'content': f'{messageContentUwU.text}'
    }
