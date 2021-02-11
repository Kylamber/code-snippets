import requests

class HtmlParser:
  def __init__(self, url, verbose = 0):
    self.url = url
    self.verbose = verbose
    self.log_prefix = '[HTMLParser]' # For logs
    self.parsed_html = self.parseHTML()
  
  def parseHTML(self):
    try:
      get = requests.get(self.url, timeout=5)
    except Exception as e:
      if self.verbose:
        print(f'{self.log_prefix} {e}')
      return '', '', []

    base_url = '/'.join(self.url.split('/')[:3])
    raw_html = get.text
    processed_html = []
    
    temp_text = ''

    for char in raw_html:
      if char == '<':
        processed_html.append(temp_text)
        temp_text = ''
        temp_text += char
      elif char == '>':
        temp_text += char
        processed_html.append(temp_text)
        temp_text = ''
      else:
        temp_text += char
    
    return base_url, raw_html, processed_html
  
  def findTag(self, tag, get_all = False):
    found = []
    start_end = []
    processed_html = self.parsed_html[2]
    for i, thing in enumerate(processed_html):
      if f'<{tag} ' in thing or f'<{tag}>' in thing or f'</{tag}>' in thing:
        if '/>' in thing:
          found.append([thing])
          start_end = []
          continue
        start_end.append(i)
      if len(start_end) == 2:
        found.append(processed_html[start_end[0]:start_end[1] + 1])
        start_end = []
        if not get_all:
          break
    
    return found
