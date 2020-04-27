from urllib.request import urlopen, Request
import re
import sys

urlOficial = "https://tags.premiumads.com.br/ads.txt"
url = sys.argv[1]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

reqFileSite = Request(url=url, headers=headers)
reqFileOficial = Request(url=urlOficial, headers=headers)

fileSite = urlopen(reqFileSite).readlines()
fileOficial = urlopen(reqFileOficial).readlines()

#print(fileSite)

linesOficial = []
linesSite = []

def clearLine(lineToClear):
  line = lineToClear.decode("utf-8")
  line = line.replace('\r\n', '')
  return line

def checkExistsInSite(oficial):    
  result = False or oficial == "\ufeff#Premium Programmatic" or re.search("^#[a-zA-Z]{0,}", oficial) != None
  for line in linesSite:
    if line.strip() == oficial.strip() or re.search(oficial, line) != None:
      result = True
  
  return result

for lineOficial in fileOficial:
  line = clearLine(lineOficial)
  if line != "":
    linesOficial.append(line)

for lineSite in fileSite:  
  line = clearLine(lineSite)
  if line != "":
    linesSite.append(line)

linhasFaltantes = []

for oficial in linesOficial:
  result = checkExistsInSite(oficial)
  if result == False:    
    linhasFaltantes.append(oficial)

if len(linhasFaltantes) == 0:
  print("Ads.txt Atualizado!!!")
else:
  print("Ads.txt precisa ser atualizado!")
  for l in linhasFaltantes:
    print(l)

#print(linesCompared)



