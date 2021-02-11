import requests

class htmlParser:
  def __init__(self, url):
    self.url = url
    self.logPrefix = '[HTMLParser]' # Has no significant use, only for decorations
    self.parsedHTML = self.parseHTML()
  
  def parseHTML(self):
    try:
      get = requests.get(self.url, timeout=5)
    except Exception as e:
      print(f'{self.logPrefix} {e}')
      return '', '', []

    baseURL = '/'.join(self.url.split('/')[:3])
    rawHTML = get.text
    processedHTML = []
    
    tempText = ''

    for char in rawHTML:
      if char == '<':
        processedHTML.append(tempText)
        tempText = ''
        tempText += char
      elif char == '>':
        tempText += char
        processedHTML.append(tempText)
        tempText = ''
      else:
        tempText += char
    
    return baseURL, rawHTML, processedHTML
  
  def find(self, tag, getAll = False):
    found = []
    startEnd = []
    processedHTML = self.parsedHTML[2]
    for i, thing in enumerate(processedHTML):
      if f'<{tag} ' in thing or f'<{tag}>' in thing or f'</{tag}>' in thing:
        if '/>' in thing:
          found.append([thing])
          startEnd = []
          continue
        startEnd.append(i)
      if len(startEnd) == 2:
        found.append(processedHTML[startEnd[0]:startEnd[1] + 1])
        startEnd = []
        if not getAll:
          break
    
    return found
