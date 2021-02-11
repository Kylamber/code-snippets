# HTML Parser

## Example Usage
### Using the find method
```python
html = HtmlParser('https://wikipedia.org/')

print(html.find('div'))
```
This will output
```
[['<div class="central-textlogo" style="font-size: 1em;">',
  '\n',
  '<img class="central-featured-logo" src="portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png" srcset="portal/wikipedia.org/assets/img/Wikipedia-logo-v2@1.5x.png 1.5x, portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 2x" width="200" height="183" alt="Wikipedia">',
  '\n',
  '<h1 class="central-textlogo-wrapper">',
  '\n',
  '<span class="central-textlogo__image sprite svg-Wikipedia_wordmark">',
  '\nWikipedia\n',
  '</span>',
  '\n',
  '<strong class="jsl10n localized-slogan" data-jsl10n="slogan">',
  'The Free Encyclopedia',
  '</strong>',
  '\n',
  '</h1>',
  '\n',
  '</div>']]
```
With some post processing, we can make it look normal again.
```python
print(''.join(html.find('div')[0]))
```
the output becomes
```html
<div class="central-textlogo" style="font-size: 1em;">
<img class="central-featured-logo" src="portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png" srcset="portal/wikipedia.org/assets/img/Wikipedia-logo-v2@1.5x.png 1.5x, portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 2x" width="200" height="183" alt="Wikipedia">
<h1 class="central-textlogo-wrapper">
<span class="central-textlogo__image sprite svg-Wikipedia_wordmark">
Wikipedia
</span>
<strong class="jsl10n localized-slogan" data-jsl10n="slogan">The Free Encyclopedia</strong>
</h1>
</div>
```

### Getting all URLs inside a website
```python
html = HtmlParser('https://testwebsite.com/')

def getURLs():
  acquired_urls = set()
  base_url = html.parsed_html[0]
  
  if not base_url:
    return []
  
  for a_tag in parsed_html.find('a', get_all = True): # find the a tag '<a>
    for param in a_tag[0].split():
      if 'href=' in param and '#' not in param: # if exist 'href' inside the a tag and doesn't have the # character.
        param = param.replace('href=', '').replace('"', '').replace("'", "").replace('>', '') # take only the url
        
        if 'http' not in param: # if it's relative, add the base_url to it
          param = base_url + param 
        
        acquired_urls.add(param)
  return acquired_urls
```

## How it works:
This program works by taking the tags and the contents between tags into an ordered list using these lines of code in the `parseHTML` method.
```python
for char in raw_html:
  if char == '<':
    processed_html.append(temp_text)
    temp_text = ''
    temp_text += char
  elif char == '>'
    temp_text += char
    processed_html.append(temp_text)
    temp_text = ''
  else:
    temp_text += char
```
at the end, the list should look something like this,
```python
>>> processed_html
['<body>', '<div class="test">', 'Contents inside the div', '<div />', ..., '<body />']
```
This orderly manner ease the finding of tags and its contents. The `find` method will search for the beginning and end of a tag. If `get_all` is set to `True`, all of the tags that matches will be listed. 
