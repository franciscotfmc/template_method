#/usr/bin/env python2.7
#coding: utf-8

import argparse
from patterns.template import HtmlDocument, CsvDocument
from transaction import Product

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--format', help='the output format can be html or csv')
  args = parser.parse_args()

  items = [Product("Gasolina", 3.20), Product("Gás Natural", 2.10), Product("Diesel", 2.20)]
  
  if args.format == "html":
    document = HtmlDocument(items)
  else:
    document = CsvDocument(items)

  output = document.generate_doc()
  f_output = open("output.{0}".format(args.format),"w")
  f_output.write(output)
  f_output.close()

if __name__ == '__main__':
  main()