from wisley.models import GeoNode
from wisley.models import ProjNode
from wisley.models import Plant

import pytest
import xml.etree.ElementTree as etree

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Node test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

@pytest.fixture()
def geonode1():
    return GeoNode(1, 'Node 1', '-0.84571884220576', '51.2945043901003')

@pytest.fixture()
def geonode2():
    return GeoNode(2, 'Node 2', '-0.85302115624881', '51.2914391458255')

@pytest.fixture()
def geonode3():
    return GeoNode(0, '', '-0.84571884220576', '51.2945043901003')

@pytest.fixture()
def projnode1():
    return ProjNode(1, 'Node 1', 480075.52727804193, 155325.20673843563)

@pytest.fixture()
def projnode2():
    return ProjNode(2, 'Node 2', 480075.52727804193, 155325.20673843563)

@pytest.fixture()
def projnode3():
    return ProjNode(0, '', 480075.52727804193, 155325.20673843563)

@pytest.fixture()
def point1():
    return 'POINT(-0.84571884220576 51.2945043901003)'

@pytest.fixture()
def point2():
    return 'POINT(480075.52727804193 155325.20673843563)'

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Plant test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

@pytest.fixture()
def plant1():

    plant = Plant()

    plant.name_num = '76294'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/WSY0035651_4061.jpg'
    plant.height = '0.5-1 metres'
    plant.hardiness = 'H6 (hardy - very cold winter)'
    plant.preferred_common_name = 'greater quaking grass'
    plant.spread = '0.1-0.5 metres'
    plant.time_to_full_height = '1-2 years'
    plant.accepted_botanical_name = '&lt;em&gt;Briza&lt;/em&gt; &lt;em&gt;maxima&lt;/em&gt;'
    plant.description = '&lt;em&gt;B. maxima&lt;/em&gt; is an erect annual grass to 60cm, forming a ' \
                                       'tuft of flat, linear leaves, with panicles of large, flat, ovate, pale yellow' \
                                       ' spikelets which dangle from slender branches'
    plant.soil_type = 'Loam, Chalk, Sand or Clay'
    plant.foliage = 'Deciduous'
    plant.uses = 'City/Courtyard Gardens, Cottage/Informal Garden, Flower borders and beds, ' \
                                        'Cut Flowers or Low Maintenance'
    plant.aspect = 'South-facing, North-facing, West-facing or East-facing'
    plant.flower_colour = 'Pale Yellow in Summer'
    plant.moisture = 'Well-drained or Moist but well-drained'
    plant.ph = 'Acid, Alkaline or Neutral'
    plant.disease_resistance = 'Generally disease free'
    plant.sunlight = 'Full Sun'
    plant.exposure = 'Exposed or Sheltered'
    plant.cultivation = 'Easy to grow in most well-drained fertile soils in a sunny position'
    plant.low_maintenance = 'False'

    return plant

@pytest.fixture()
def elem1():

    elem = etree.Element('EntityDetailItems')

    elem.attrib['Name_Num'] = '76294'
    elem.attrib['PlantImagePath'] = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/WSY0035651_4061.jpg'
    elem.attrib['Height'] = '0.5-1 metres'
    elem.attrib['Hardiness'] = 'H6 (hardy - very cold winter)'
    elem.attrib['PreferredCommonName'] = 'greater quaking grass'
    elem.attrib['Spread'] = '0.1-0.5 metres'
    elem.attrib['TimeToFullHeight'] = '1-2 years'
    elem.attrib['AcceptedBotanicalName'] = '&lt;em&gt;Briza&lt;/em&gt; &lt;em&gt;maxima&lt;/em&gt;'
    elem.attrib['EntityDescription'] = '&lt;em&gt;B. maxima&lt;/em&gt; is an erect annual grass to 60cm, forming a ' \
                                       'tuft of flat, linear leaves, with panicles of large, flat, ovate, pale yellow' \
                                       ' spikelets which dangle from slender branches'
    elem.attrib['SoilType'] = 'Loam, Chalk, Sand or Clay'
    elem.attrib['Foliage'] = 'Deciduous'
    elem.attrib['SuggestedPlantUses'] = 'City/Courtyard Gardens, Cottage/Informal Garden, Flower borders and beds, ' \
                                        'Cut Flowers or Low Maintenance'
    elem.attrib['Aspect'] = 'South-facing, North-facing, West-facing or East-facing'
    elem.attrib['Flower'] = 'Pale Yellow in Summer'
    elem.attrib['Moisture'] = 'Well-drained or Moist but well-drained'
    elem.attrib['PH']= 'Acid, Alkaline or Neutral'
    elem.attrib['DiseaseResistance'] = 'Generally disease free'
    elem.attrib['Sunlight'] = 'Full Sun'
    elem.attrib['Exposure'] = 'Exposed or Sheltered'
    elem.attrib['Cultivation'] = 'Easy to grow in most well-drained fertile soils in a sunny position'
    elem.attrib['LowMaintenance'] = 'False'

    return elem

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Custom Assert functions
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def assert_geonode(node1, node2):

    assert type(node1) == type(node2)
    assert node1.id == node2.id
    assert node1.lat == node2.lat
    assert node1.long == node2.long
    assert node1.name == node2.name

    return

def assert_projnode(node1, node2):

    assert type(node1) == type(node2)
    assert node1.id == node2.id
    assert node1.x == node2.x
    assert node1.y == node2.y
    assert node1.name == node2.name

    return

def assert_plant(plant1, plant2):

    assert type(plant1) == type(plant2)
    assert plant1.name_num == plant2.name_num
    assert plant1.preferred_common_name  == plant2.preferred_common_name
    assert plant1.pic == plant2.pic
    assert plant1.height == plant2.height
    assert plant1.spread == plant2.spread
    assert plant1.time_to_full_height == plant2.time_to_full_height
    assert plant1.hardiness == plant2.hardiness
    assert plant1.accepted_botanical_name == plant2.accepted_botanical_name
    assert plant1.description == plant2.description
    assert plant1.soil_type == plant2.soil_type
    assert plant1.foliage == plant2.foliage
    assert plant1.uses == plant2.uses
    assert plant1.aspect == plant2.aspect
    assert plant1.flower_colour == plant2.flower_colour
    assert plant1.moisture == plant2.moisture
    assert plant1.ph == plant2.ph
    assert plant1.disease_resistance == plant2.disease_resistance
    assert plant1.sunlight == plant2.sunlight
    assert plant1.exposure == plant2.exposure
    assert plant1.cultivation == plant2.cultivation
    assert plant1.low_maintenance == plant2.low_maintenance

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# GeoNode Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_geonode_constructor(geonode1):

    # Trivial test for classic constructor

    act_node = GeoNode(1, 'Node 1', '-0.84571884220576', '51.2945043901003')

    assert_geonode(geonode1, act_node)

    return

def test_geonode_from_db_string(geonode3, point1):

    # Tests GeoNode constructor from_db_string

    act_node = GeoNode.from_db_string(point1)

    assert_geonode(geonode3, act_node)

    return


def test_geonode_from_db_row(geonode1):

    # Tests GeoNode constructor from_db_row

    db_row = (1, 'POINT(-0.84571884220576 51.2945043901003)', 'Node 1')

    act_node = GeoNode.from_db_row(db_row)

    assert_geonode(geonode1, act_node)

    return


def test_geonode_to_point(geonode1, point1):

    # Tests point_string() method of GeoNode class

    exp_ret_val = 'ST_PointFromText(\'' + point1 + '\', 4326)'

    act_ret_val = geonode1.point_string()

    assert act_ret_val == exp_ret_val

    return

def test_geonode_convert(geonode2, projnode2):

    act_node = geonode2.convert()

    assert_projnode(projnode2, act_node)

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# ProjNode Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_projnode_constructor(projnode1):

    # Trivial test for classic constructor

    act_node = ProjNode(1, 'Node 1', 480075.52727804193, 155325.20673843563)

    assert_projnode(projnode1, act_node)

    return

def test_projnode_from_db_string(projnode3, point2):

    # Tests ProjNode constructor from_db_string

    act_node = ProjNode.from_db_string(point2)

    assert_projnode(projnode3, act_node)

    return


def test_projnode_from_db_row(projnode1):

    # Tests ProjNode constructor from_db_row

    db_row = (1, 'POINT(480075.52727804193 155325.20673843563)', 'Node 1')

    act_node = ProjNode.from_db_row(db_row)

    assert_projnode(projnode1, act_node)


    return

def test_projnode_to_point(projnode1, point2):

    # Tests point_string() method of ProjNode class

    exp_ret_val = 'ST_PointFromText(\'' + point2 + '\')'

    act_ret_val = projnode1.point_string()

    assert act_ret_val == exp_ret_val

    return

def test_projnode_convert(projnode2, geonode2):

    act_node = geonode2.convert()

    assert_projnode(projnode2, act_node)

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Plant Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_populate_plant(elem1, plant1):

    # Tests populate_xml method of Plant class
    act_plant = Plant()
    act_plant.populate_xml(elem1)

    assert_plant(plant1, act_plant)

    return

