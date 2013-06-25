#/usr/bin/env python2.7
#coding: utf-8

from patterns.template import HtmlDocument
from transaction import Product

def main():
  print HtmlDocument([Product("Gasolina", 3.20), Product("Gás Natural", 2.10), Product("Diesel", 2.20)]).generate_doc()

if __name__ == '__main__':
  main()