# 解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print('<%s>' % tag)
  def handle_endtag(self, tag):
    print('</%s>' % tag)  
  def handle_startendtag(self, tag, attrs):
     print('<%s/>' % tag)
  def handle_data(self, data):
    print(data)
  def handle_comment(self, data):
    print('<!--', data, '-->')
  def handle_entityref(self, name):
    # 特殊字符 英文表示 &nbsp;
    print('&%s;' % name)
  def handle_charref(self, name):
    # 特殊字符 数字表示&#1234;
    print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
