#coding: utf-8

from abc import ABCMeta, abstractmethod

class DocumentMaker:
  __metaclass__ = ABCMeta

  def __init__(self, transactions):
    self.transactions = transactions

  def generate_doc(self):
    return "%s %s %s" % (self.make_header(), self.make_body(), self.make_footer())

  @abstractmethod
  def make_header(self): 
    pass

  @abstractmethod
  def make_body(self): 
    pass

  @abstractmethod
  def make_footer(self):
    pass

class HtmlDocument(DocumentMaker):

  def make_header(self):
    return "<html><head><title>Template Method</title></head>"

  def make_body(self):
    content = "<h1>Relatório de Transações</h1><br><ul>"
    for t in self.transactions:
      content += "<li>%s - %s</li>" % (t.description, t.value)
    
    content += "</ul>"
    return "<body><strong>%s</strong>" % content

  def make_footer(self):
    return "<hr>Total: %s </body></html>" % reduce(lambda x,y : x + y, [t.value for t in self.transactions])

class CsvDocument(DocumentMaker):

  def make_header(self):
    return "Descrição;Valor"

  def make_body(self):
    content = ""
    for t in self.transactions:
      content += "%s;%s" % (t.description, t.value)
    
    return content

  def make_footer(self):
    return "Total;%s" % reduce(lambda x,y : x + y, [t.value for t in self.transactions])

