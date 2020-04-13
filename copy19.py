import requests
import itertools
import threading
import time
import sys
from bs4 import BeautifulSoup
from texttable import Texttable
from colorama import Fore
from colorama import Style

print(f'''{Fore.GREEN}

        d8888  .d8888b.  d888  8888888b.  .d8888b. 888     888 
       d8P888 d88P  Y88bd8888  888  "Y88bd88P  Y88b888     888 
      d8P 888 888         888  888    888888    888888     888 
     d8P  888 888d888b.   888  888    888888    888888     888 
    d88   888 888P "Y88b  888  888    888888    888888     888 
    8888888888888    888  888  888    888888    888888     888 
          888 Y88b  d88P  888  888  .d88PY88b  d88PY88b. .d88P 
          888  "Y8888P" 88888888888888P"  "Y8888P"  "Y88888P"

  {Style.RESET_ALL}
''')
print(f'  {Fore.BLUE}CoviPy-19 v1.0{Style.RESET_ALL} by Abdelhalim')
print('  Track CoronaVirus(COVID-19) ')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', "\\"]):
        if done:
            break
        sys.stdout.write('\r  loading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rStay Home     \n')
    sys.stdout.write('\n')

tim = threading.Thread(target=animate)
tim.start()



worldmetter = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(worldmetter.content, 'html.parser')
totalNumber = soup.findAll("div", {"class" : "maincounter-number"})
totalcases = totalNumber[0].text
death = totalNumber[1].text
recovred = totalNumber[2].text

t = Texttable()
t.add_rows([['Total cases', 'Deaths', 'Recovered'], [totalcases, death, recovred]])
print('\n')
print(t.draw())

done = True
