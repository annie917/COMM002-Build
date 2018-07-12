#!/usr/local/bin/python3.6

import timeit


def lxml_find(plant_to_find):

    import lxml.etree as ET

    tree = ET.parse('./big_xml.xml')

    plant = tree.find('EntityDetails/EntityDetailsItems[@PreferredCommonName="' + plant_to_find + '"]')

    s = plant.attrib['Name_Num']


# lxml, find, last plant

import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

number_of_plants = int(config['TimeTests']['number_of_plants'])
runs = int(config['TimeTests']['runs'])
repeats = int(config['TimeTests']['repeats'])

mysetup = 'from __main__ import lxml_find'

mycode = 'plant_to_find = \'PCN ' + str(number_of_plants) + '\'\n' + 'lxml_find(plant_to_find)'

print('Time using lxml.etree._ElementTree.find (' + str(number_of_plants) + ' plants, last plant): ',
      min(timeit.repeat(setup=mysetup, stmt=mycode, number=runs, repeat=repeats))/float(runs),
      '      (' + str(runs) + ' runs, ' + str(repeats) + ' repeats)')

