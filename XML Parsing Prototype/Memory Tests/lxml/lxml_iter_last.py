#!/usr/local/bin/python3.6
# lxml, iterparse, last plant


@profile()
def lxml_iterparse(plant_to_find):

    import lxml.etree as ET

    for event, elem in ET.iterparse('./big_xml.xml', events=("start", "end")):
        if event == "start":
            if elem.tag == 'EntityDetailsItems':
                if elem.attrib['PreferredCommonName'] == plant_to_find:
                    plant_name_num = elem.attrib['Name_Num']
                    break

        elem.clear()

    return plant_name_num


if __name__ == '__main__':

    import configparser

    config = configparser.ConfigParser()
    config.read('./config.ini')

    number_of_plants = config['TimeTests']['number_of_plants']

    print('\n\n\n#####lxml, iterparse, ' + number_of_plants + ' plants, last plant#####\n')
    lxml_iterparse('PCN ' + number_of_plants)

