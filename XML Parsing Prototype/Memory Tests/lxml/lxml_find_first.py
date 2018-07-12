#!/usr/local/bin/python3.6
# lxml, find, first plant


@profile()
def lxml_find(plant_to_find):

    import lxml.etree as ET

    tree = ET.parse('./big_xml.xml')

    plant = tree.find('EntityDetails/EntityDetailsItems[@PreferredCommonName="' + plant_to_find + '"]')

    plant_name_num = plant.attrib['Name_Num']

    return plant_name_num


if __name__ == '__main__':

    import configparser

    config = configparser.ConfigParser()
    config.read('./config.ini')

    number_of_plants = config['TimeTests']['number_of_plants']

    print('\n\n\n#####lxml, find, ' + number_of_plants + ' plants, first plant#####\n')
    lxml_find('PCN 1')
