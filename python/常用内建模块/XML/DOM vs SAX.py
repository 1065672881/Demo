# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
#
# 正常情况下，优先考虑SAX，因为DOM实在太占内存。
#
# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
#
# 举个例子，当SAX解析器读到一个节点时
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print(name, str(attrs))

    def ent_element(self, name):
        print(name)

    def char_data(self, text):
        print(text)


xml = r'''<?xml version="1.0"?>
          <ol>
              <li><a href="/python">Python</a></li>
              <li><a href="/ruby">Ruby</a></li>
          </ol>
      '''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.ent_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
