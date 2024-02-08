import requests
from data import (loginUrl, planLekcjiUrl, payload)
from bs4 import BeautifulSoup


async def lesson_plan():
    with requests.session() as uwu:
        uwu.post(loginUrl, data=payload)
        planLekciSite = uwu.get(planLekcjiUrl)
    soup = BeautifulSoup(planLekciSite.content, 'html.parser')
    monday = soup.find_all('div', class_='bx pz tooltip', style="width:19%;left:0.5%;")
    mondayLessonsList = []
    for mondayPlan in monday:
        mondayPlan = str(mondayPlan.text)
        position_of_2 = mondayPlan.find('2')
        mondayPlan = mondayPlan[:position_of_2 + 1]
        mondayPlan = mondayPlan.replace('2', '')
        mondayLessonsList.append(mondayPlan.replace('\n', ''))
    mondayLessonListLength = len(mondayLessonsList)
    for _ in range(10 - mondayLessonListLength):
        mondayLessonsList.append("None")
    tuesday = soup.find_all('div', class_='bx pz tooltip', style="width:19%;left:20.5%;")
    tuesdayLessonsList = []
    for tuesdayPlan in tuesday:
        tuesdayPlan = str(tuesdayPlan.text)
        position_of_2 = tuesdayPlan.find('2')
        tuesdayPlan = tuesdayPlan[:position_of_2 + 1]
        tuesdayPlan = tuesdayPlan.replace('2', '')
        tuesdayLessonsList.append(tuesdayPlan.replace('\n', ''))
    tuesdayLessonListLength = len(tuesdayLessonsList)
    for _ in range(10 - tuesdayLessonListLength):
        tuesdayLessonsList.append("None")
    wednesday = soup.find_all('div', class_='bx pz tooltip', style="width:19%;left:40.5%;")
    wednesdayLessonsList = []
    for wednesdayPlan in wednesday:
        wednesdayPlan = str(wednesdayPlan.text)
        position_of_2 = wednesdayPlan.find('2')
        wednesdayPlan = wednesdayPlan[:position_of_2 + 1]
        wednesdayPlan = wednesdayPlan.replace('2', '')
        wednesdayLessonsList.append(wednesdayPlan.replace('\n', ''))
    wednesdayLessonListLength = len(wednesdayLessonsList)
    for _ in range(10 - wednesdayLessonListLength):
        wednesdayLessonsList.append("None")
    thursday = soup.find_all('div', class_='bx pz tooltip', style="width:19%;left:60.5%;")
    thursdayLessonsList = []
    for thursdayPlan in thursday:
        thursdayPlan = str(thursdayPlan.text)
        position_of_2 = thursdayPlan.find('2')
        thursdayPlan = thursdayPlan[:position_of_2 + 1]
        thursdayPlan = thursdayPlan.replace('2', '')
        thursdayLessonsList.append(thursdayPlan.replace('\n', ''))
    thursdayLessonListLength = len(thursdayLessonsList)
    for _ in range(10 - thursdayLessonListLength):
        thursdayLessonsList.append("None")
    friday = soup.find_all('div', class_='bx pz tooltip', style="width:19%;left:80.5%;")
    fridayLessonsList = []
    for fridayPlan in friday:
        fridayPlan = str(fridayPlan.text)
        position_of_2 = fridayPlan.find('2')
        fridayPlan = fridayPlan[:position_of_2 + 1]
        fridayPlan = fridayPlan.replace('2', '')
        fridayLessonsList.append(fridayPlan.replace('\n', ''))
    fridayLessonListLength = len(fridayLessonsList)
    for _ in range(10 - fridayLessonListLength):
        fridayLessonsList.append("None")

    return {
        'Monday': {
            'lesson 1': f'{mondayLessonsList[0]}',
            'lesson 2': f'{mondayLessonsList[1]}',
            'lesson 3': f'{mondayLessonsList[2]}',
            'lesson 4': f'{mondayLessonsList[3]}',
            'lesson 5': f'{mondayLessonsList[4]}',
            'lesson 6': f'{mondayLessonsList[5]}',
            'lesson 7': f'{mondayLessonsList[6]}',
            'lesson 8': f'{mondayLessonsList[7]}',
            'lesson 9': f'{mondayLessonsList[8]}',
            'lesson 10': f'{mondayLessonsList[9]}',
        },
        'Tuesday': {
            'lesson 1': f'{tuesdayLessonsList[0]}',
            'lesson 2': f'{tuesdayLessonsList[1]}',
            'lesson 3': f'{tuesdayLessonsList[2]}',
            'lesson 4': f'{tuesdayLessonsList[3]}',
            'lesson 5': f'{tuesdayLessonsList[4]}',
            'lesson 6': f'{tuesdayLessonsList[5]}',
            'lesson 7': f'{tuesdayLessonsList[6]}',
            'lesson 8': f'{tuesdayLessonsList[7]}',
            'lesson 9': f'{tuesdayLessonsList[8]}',
            'lesson 10': f'{tuesdayLessonsList[9]}',

        },
        'Wednesday': {
            'lesson 1': f'{wednesdayLessonsList[0]}',
            'lesson 2': f'{wednesdayLessonsList[1]}',
            'lesson 3': f'{wednesdayLessonsList[2]}',
            'lesson 4': f'{wednesdayLessonsList[3]}',
            'lesson 5': f'{wednesdayLessonsList[4]}',
            'lesson 6': f'{wednesdayLessonsList[5]}',
            'lesson 7': f'{wednesdayLessonsList[6]}',
            'lesson 8': f'{wednesdayLessonsList[7]}',
            'lesson 9': f'{wednesdayLessonsList[8]}',
            'lesson 10': f'{wednesdayLessonsList[9]}',
        },
        'Thursday': {
            'lesson 1': f'{thursdayLessonsList[0]}',
            'lesson 2': f'{thursdayLessonsList[1]}',
            'lesson 3': f'{thursdayLessonsList[2]}',
            'lesson 4': f'{thursdayLessonsList[3]}',
            'lesson 5': f'{thursdayLessonsList[4]}',
            'lesson 6': f'{thursdayLessonsList[5]}',
            'lesson 7': f'{thursdayLessonsList[6]}',
            'lesson 8': f'{thursdayLessonsList[7]}',
            'lesson 9': f'{thursdayLessonsList[8]}',
            'lesson 10': f'{thursdayLessonsList[9]}',
        },
        'Friday': {
            'lesson 1': f'{fridayLessonsList[0]}',
            'lesson 2': f'{fridayLessonsList[1]}',
            'lesson 3': f'{fridayLessonsList[2]}',
            'lesson 4': f'{fridayLessonsList[3]}',
            'lesson 5': f'{fridayLessonsList[4]}',
            'lesson 6': f'{fridayLessonsList[5]}',
            'lesson 7': f'{fridayLessonsList[6]}',
            'lesson 8': f'{fridayLessonsList[7]}',
            'lesson 9': f'{fridayLessonsList[8]}',
            'lesson 10': f'{fridayLessonsList[9]}',
        }
    }
