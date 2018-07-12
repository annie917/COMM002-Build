#!/usr/local/bin/python3.6

import timeit


def lxml_iterparse(plant_to_find):

    import lxml.etree as ET

    for event, elem in ET.iterparse('./big_xml.xml', events=("start", "end")):
        if event == "start":
            if elem.tag == 'EntityDetailsItems':
                if elem.attrib['PreferredCommonName'] == plant_to_find:
                    s = elem.attrib['Name_Num']
                    break

        elem.clear()


# lxml, very big file, iterparse, first plant

import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

number_of_plants = int(config['TimeTests']['number_of_plants'])
runs = int(config['TimeTests']['runs'])
repeats = int(config['TimeTests']['repeats'])

mysetup = 'from __main__ import lxml_iterparse'

mycode = '''

plant_to_find = 'PCN 1'
lxml_iterparse(plant_to_find)
                               '''

print('Time using lxml.etree.iterparse (' + str(number_of_plants) + ' plants, first plant): ',
      min(timeit.repeat(setup=mysetup, stmt=mycode, number=runs, repeat=repeats))/float(runs),
      '      (' + str(runs) + ' runs, ' + str(repeats) + ' repeats)')

