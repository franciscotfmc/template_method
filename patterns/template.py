#coding: utf-8

import locale
from abc import ABCMeta, abstractmethod

class DocumentMaker:
  __metaclass__ = ABCMeta

  def __init__(self, transactions):
    self.transactions = transactions

  def generate_doc(self):
    return "%s%s%s" % (self.make_header(), self.make_body(), self.make_footer())

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
    return "<html><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /><title>Template Method</title></head>"

  def make_body(self):
    content = "<h1>Relatório de Transações</h1><br><ul>"
    for t in self.transactions:
      content += "<li>%s - %s</li>" % (t.description, locale.currency(t.value))

    content += "</ul>"
    return "<body><strong>%s</strong>" % content

  def make_footer(self):
    return "<hr>Total: %s </body></html>" % locale.currency(reduce(lambda x,y : x + y, [t.value for t in self.transactions]))

class CsvDocument(DocumentMaker):

  def make_header(self):
    return "Descrição;Valor\n"

  def make_body(self):
    content = ""
    for t in self.transactions:
      content += "%s;%s\n" % (t.description, locale.currency(t.value))

    return content

  def make_footer(self):
    return "Total;%s" % locale.currency(reduce(lambda x,y : x + y, [t.value for t in self.transactions]))

