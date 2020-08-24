import requests
from bs4 import BeautifulSoup
import re

def main():
  url = 'https://m.hanshintigers.jp/game/score/'
  # replace YOUR-USER-AGENT to your User-Agent
  headers = {'User-Agent': 'YOUR-USER-AGENT'}
  request = requests.get(url, headers=headers)

  soup = BeautifulSoup(request.text, 'lxml')
  inning = soup.find(class_='inning').text
  teamPointList = []

  for i in soup.find_all(class_='number'):
      teamPointList.append(i.text)

  home_team_name = soup.find(class_='l_left').text
  away_team_name = soup.find(class_='l_right').text
  home_team_point = teamPointList[0]
  away_team_point = teamPointList[1]

  print(inning + '\n' + home_team_name + home_team_point + ' - ' + away_team_name + away_team_point)

if __name__ == '__main__':
  main()
