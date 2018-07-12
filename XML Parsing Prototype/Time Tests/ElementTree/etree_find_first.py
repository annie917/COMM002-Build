#!/usr/local/bin/python3.6

import timeit


def elemtree_find(plant_to_find):

    import xml.etree.ElementTree as ET

    tree = ET.parse('./big_xml.xml')

    plant = tree.find('EntityDetails/EntityDetailsItems[@PreferredCommonName="' + plant_to_find + '"]')

    s = plant.attrib['Name_Num']

    return


# ElementTree, find, first plant

import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

number_of_plants = int(config['TimeTests']['number_of_plants'])
runs = int(config['TimeTests']['runs'])
repeats = int(config['TimeTests']['repeats'])

mysetup = 'from __main__ import elemtree_find'

mycode = '''

plant_to_find = 'PCN 1'
elemtree_find(plant_to_find)
                               '''
print('Time using xml.etree.ElementTree.ElementTree.find (' + str(number_of_plants) + ' plants, first plant): ',
      min(timeit.repeat(setup=mysetup, stmt=mycode, number=runs, repeat=repeats))/float(runs),
      '      (' + str(runs) + ' runs, ' + str(repeats) + ' repeats)')
