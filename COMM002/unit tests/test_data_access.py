import wisley.data_access as db
from wisley.models import GeoNode
from wisley.models import ProjNode
from wisley.models import Plant
from wisley.models import Place
from wisley.models import Stage

import pytest
import networkx as nx

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Node test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

@pytest.fixture()
def node3():
    return GeoNode(1, 'Flower Bed 1', '-0.8528091015952259', '51.29180649906897')

@pytest.fixture()
def node4():
    return GeoNode(4, 'Flower Bed 4', '-0.8517447774739522', '51.29174150409153')

@pytest.fixture()
def node5():
    return GeoNode(7, 'Flower Bed 7', '-0.8524337425712866', '51.292041426751496')

@pytest.fixture()
def projnode1():
    # Place 2
    return ProjNode(0, '', 480060.6195600935, 155300.5319708603)

@pytest.fixture()
def projnode2():
    # Node 1
    return ProjNode(1, 'Node 1', 480075.52727804193, 155325.20673843563)

@pytest.fixture()
def projnode3():
    # Node 12
    return ProjNode(12, 'Node 12', 480153.12022010185, 155351.79401970515)

@pytest.fixture()
def geonode8():
    return GeoNode(8, 'Node 8', '-0.85187317079043', '51.2923985767057')

@pytest.fixture()
def geonode9():
    return GeoNode(9, 'Node 9', '-0.85161836093402', '51.2923063246076')

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Place test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

@pytest.fixture()
def place1():
    place = Place(1, 'Picnic Area', '-0.85198112970328', '51.2924438640308')
    place.description = 'Picnic Area Description'

    return place

@pytest.fixture()
def place2():
    place = Place(2, 'Entrance', '-0.85324042683577', '51.2912194132039')
    place.description = 'Entrance Description'

    return place

@pytest.fixture()
def place3():
    place = Place(3, 'Nature Reserve', '-0.8506869638536', '51.2924270909523')
    place.description = 'Nature Reserve Description'

    return place

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
    plant.accepted_botanical_name = '<em>Briza</em> <em>maxima</em>'
    plant.description = '<em>B. maxima</em> is an erect annual grass to 60cm, forming a ' \
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

    plant.common_names.append('great quaking grass')
    plant.common_names.append('pearl grass')
    plant.synonyms.append('<em>Briza</em> <em>major</em>')

    return plant


@pytest.fixture()
def plant2():

    plant = Plant()

    plant.name_num = '97224'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/WSY0034793_4502.jpg'
    plant.height = '0.5-1 metres'
    plant.hardiness = 'H7 (very hardy)'
    plant.preferred_common_name = 'white bachelor\'s buttons'
    plant.spread = '0.1-0.5 metres'
    plant.time_to_full_height = '2-5 years'
    plant.accepted_botanical_name = '<em>Ranunculus</em> <em>aconitifolius</em> \'Flore Pleno\' (d) AGM'
    plant.description = '\'Flore Pleno\' is a vigorous herbaceous perennial to 90cm, with palmately divided dark ' \
                        'green leaves and branched stems bearing long-lasting double, button-like white ' \
                        'flowers 2cm in width'
    plant.soil_type = 'Clay, Loam or Chalk'
    plant.foliage = 'Deciduous'
    plant.uses = 'Cottage/Informal Garden, Flower borders and beds or Cut Flowers'
    plant.aspect = 'South-facing, East-facing or West-facing'
    plant.flower_colour = 'White in Spring and  Summer'
    plant.moisture = 'Moist but well-drained'
    plant.ph = 'Acid, Alkaline or Neutral'
    plant.disease_resistance = 'May be subject to <a ' \
                                       'href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=253\' >powdery ' \
                                       'mildews</a> in dry conditions'
    plant.sunlight = 'Full Sun, Partial Shade'
    plant.exposure = 'Sheltered'
    plant.cultivation = 'Grow in humus-rich, fertile, moist or moist but well-drained soil in full or partial shade'
    plant.low_maintenance = 'False'

    plant.common_names.append('fair maids of France')
    plant.common_names.append('fair maids of Kent')
    plant.synonyms.append('<em>Ranunculus</em> <em>aconitifolius</em>  <em>'
                          'flore</em>  <em>pleno</em> \'Batchelor\'s Button\'')

    return plant

@pytest.fixture()
def plant3():

    plant = Plant()

    plant.name_num = '72209'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/WSY0052080_5834.jpg'
    plant.height = '0.1-0.5 metres'
    plant.hardiness = 'H7 (very hardy)'
    plant.preferred_common_name = 'plantain lily \'Zounds\''
    plant.spread = '0.5-1 metres'
    plant.time_to_full_height = '2-5 years'
    plant.accepted_botanical_name = '<em>Hosta</em> \'Zounds\''
    plant.description = '\'Zounds\' makes a compact mound of puckered, broadly ovate, golden yellow leaves to 25cm ' \
                        'long, with very pale purple flowers in mid summer'
    plant.soil_type = 'Clay or Loam'
    plant.foliage = 'Deciduous'
    plant.uses = 'City/Courtyard Gardens, Coastal, Cottage/Informal Garden, Flower borders and beds, Ground Cover or ' \
                 'Underplanting of Roses and Shrubs'
    plant.aspect = 'East-facing or North-facing'
    plant.flower_colour = 'Pale Purple in Summer'
    plant.moisture = 'Moist but well-drained'
    plant.ph = 'Acid or Neutral'
    plant.disease_resistance = 'May be subject to <a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=188\' ' \
                               '>a virus</a>'
    plant.sunlight = 'Partial Shade'
    plant.exposure = 'Sheltered'
    plant.cultivation = 'Grow in fertile, moist but well-drained soil with shelter from cold, dry winds. ' \
                        'Best in slightly acid or neutral soils; it will grow in alkaline soils if enriched but ' \
                        'shallow, chalky soils can cause leaves to yellow. Partial shade is best but it can ' \
                        'tolerate some sun if the soil is kept moist. Mulch in spring'
    plant.low_maintenance = 'False'


    return plant


@pytest.fixture()
def plant4():

    plant = Plant()

    plant.name_num = '311173'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/RHS_RHS-0004192_7162.JPG'
    plant.height = '0.5-1 metres'
    plant.hardiness = 'H2 (tender - cool or frost-free greenhouse)'
    plant.preferred_common_name = 'marguerite [LaRita White Beauty]'
    plant.spread = '0.5-1 metres'
    plant.time_to_full_height = '1-2 years'
    plant.accepted_botanical_name = '<em>Argyranthemum</em> <span style="font-variant: small-caps">LaRita White ' \
                                    'Beauty</span> \'Kleaf07028\' (LaRita Series) AGM'
    plant.description = '<span style="font-variant: small-caps">LaRita White Beauty</span> forms a mound to 50 x 60 cm ' \
                        'with silvery glaucous foliage and classic white-rayed, yellow-centred flowers to 4.5cm'
    plant.soil_type = 'Sand, Clay or Loam'
    plant.foliage = 'Evergreen'
    plant.uses = 'City/Courtyard Gardens, Coastal, Flower borders and beds, Patio/Container Plants, Mediterranean ' \
                 'Climate Plants or Wall-side Borders'
    plant.aspect = 'South-facing or East-facing'
    plant.flower_colour = 'White and  Yellow in Autumn, Spring and  Summer'
    plant.moisture = 'Well-drained or Moist but well-drained'
    plant.ph = 'Acid, Alkaline or Neutral'
    plant.disease_resistance = 'Crown gall is an occasional problem'
    plant.sunlight = 'Full Sun'
    plant.exposure = 'Sheltered'
    plant.cultivation = 'Grow in moderately fertile, well-drained soil in full sun.  Deadhead regularly to prolong ' \
                        'flowering and pinch growing tips to keep compact. Mulching may protect rootstock from frost, ' \
                        'and helps to conserve water. Water in prolonged dry spells'
    plant.low_maintenance = 'False'

    plant.common_names.append('marguerite \'Kleaf07028\'')

    return plant


@pytest.fixture()
def plant5():

    plant = Plant()

    plant.name_num = '59261'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/WSY0035550_4408.jpg'
    plant.height = '1-1.5 metres'
    plant.hardiness = 'H7 (very hardy)'
    plant.preferred_common_name = 'globe thistle \'Taplow Blue\''
    plant.spread = '0.5-1 metres'
    plant.time_to_full_height = '2-5 years'
    plant.accepted_botanical_name = '<em>Echinops</em> <em>bannaticus</em> \'Taplow Blue\''
    plant.description = '\'Taplow Blue\' is a robust, upright herbaceous perennial, with divided, prickly dark ' \
                        'green leaves whitish beneath. Rounded, steel-blue flower heads on branched, leafy stems'
    plant.soil_type = 'Sand, Loam or Chalk'
    plant.foliage = 'Deciduous'
    plant.uses = 'Cottage/Informal Garden, Flower borders and beds, Cut Flowers, Wildlife Gardens, Gravel ' \
                 'Garden or Low Maintenance'
    plant.aspect = 'South-facing, East-facing or West-facing'
    plant.flower_colour = 'Blue in Summer'
    plant.moisture = 'Well-drained'
    plant.ph = 'Acid, Alkaline or Neutral'
    plant.disease_resistance = 'Generally disease free'
    plant.sunlight = 'Full Sun, Partial Shade'
    plant.exposure = 'Exposed'
    plant.cultivation = 'Best in poor, well-drained soil in full sun but will tolerate most soils in full sun and ' \
                        'can tolerate partial shade'
    plant.low_maintenance = 'False'

    plant.synonyms.append('<em>Echinops</em> <em>ritro</em> \'Taplow Blue\'')
    plant.synonyms.append('<em>Echinops</em> \'Taplow Blue\'')
    plant.synonyms.append('<em>Eryngium</em> \'Taplow Blue\'')

    return plant


@pytest.fixture()
def plant6():

    plant = Plant()

    plant.name_num = '100980'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/RHS_PUB0001908_11407.JPG'
    plant.height = '0.1-0.5 metres'
    plant.hardiness = 'H5 (hardy - cold winter)'
    plant.preferred_common_name = 'tulip Violacea Group'
    plant.spread = '0-0.1 metre'
    plant.time_to_full_height = '2-5 years'
    plant.accepted_botanical_name = '<em>Tulipa</em> <em>humilis</em> Violacea Group (15)'
    plant.description = 'Violacea Group are dwarf perennial bulbs, to 15cm tall, with narrow grey-green leaves. Flowers, pink-purple with a yellow base, appear in late spring'
    plant.soil_type = 'Loam, Chalk or Sand'
    plant.foliage = 'Deciduous'
    plant.uses = 'City/Courtyard Gardens, Cottage/Informal Garden, Flower borders and beds, Patio/Container Plants, Rock Garden or Wildflower meadow'
    plant.aspect = 'South-facing, West-facing or East-facing'
    plant.flower_colour = 'Purple, Yellow and  Dark Pink in Spring'
    plant.moisture = 'Well-drained'
    plant.ph = 'Neutral or Alkaline'
    plant.disease_resistance = 'May be subject to <a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=252\' ' \
                               '>tulip fire</a>, <a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=254\' ' \
                               '>tulip viruses</a> and bulb rots'
    plant.sunlight = 'Full Sun'
    plant.exposure = 'Sheltered'
    plant.cultivation = 'Plant 10-15cm deep in fertile, well-drained soil in full sun, protect from excessive wet ' \
                        'and shelter from strong winds, see <a href=\'http://www.rhs.org.uk/advicesearch/' \
                        'Profile.aspx?pid=684\' >tulip cultivation</a>'
    plant.low_maintenance = 'False'

    plant.synonyms.append('<em>Tulipa</em> <em>humilis</em> purple')
    plant.synonyms.append('<em>Tulipa</em> <em>pulchella</em> \'Violacea\'')
    plant.synonyms.append('<em>Tulipa</em> <em>violacea</em>')

    return plant

@pytest.fixture()
def plant7():

    plant = Plant()

    plant.name_num = '18556'
    plant.pic = 'http://vsorchard/PlantFinderPlus_Test/PlantEntityImages/MAR0034393_10079.jpg'
    plant.height = '0.1-0.5 metres'
    plant.hardiness = 'H6 (hardy - very cold winter)'
    plant.preferred_common_name = 'Vvedensky\'s tulip'
    plant.spread = '0.1-0.5 metres'
    plant.time_to_full_height = '2-5 years'
    plant.accepted_botanical_name = '<em>Tulipa</em> <em>vvedenskyi</em> (15)'
    plant.description = '<em>T. vvedenskyi</em> is a perennial bulb to 40cm tall with narrow, wavy-edged, grey-green, ' \
                        'often prostrate, leaves. The red to orange-red flowers reach up to 10.5cm long, with each ' \
                        'petal marked yellow at the base'
    plant.soil_type = 'Loam, Sand or Chalk'
    plant.foliage = 'Deciduous'
    plant.uses = 'Patio/Container Plants, Gravel Garden, Rock Garden, City/Courtyard Gardens or Cottage/Informal Garden'
    plant.aspect = 'South-facing or West-facing'
    plant.flower_colour = 'Red, Yellow and  Dark Orange in Spring'
    plant.moisture = 'Well-drained'
    plant.ph = 'Acid, Alkaline or Neutral'
    plant.disease_resistance = 'May be subject to <a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=252\' >' \
                               'tulip fire</a> and bulb rots'
    plant.sunlight = 'Full Sun'
    plant.exposure = 'Sheltered'
    plant.cultivation = 'Needs a warm, sunny position with sharp drainage and protection from excessive wet, summer or ' \
                        'winter. See <a href=\'http://www.rhs.org.uk/advicesearch/Profile.aspx?pid=684\' ' \
                        '>tulip cultivation</a>'
    plant.low_maintenance = 'False'

    plant.synonyms.append('<em>Tulipa</em> <em>wedenskyi</em>')

    return plant

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

def assert_place(place1, place2):

    assert type(place1) == type(place2)
    assert place1.id == place2.id
    assert place1.lat == place2.lat
    assert place1.long == place2.long
    assert place1.name == place2.name
    assert place1.description == place2.description

    return

def assert_stage(stage1, stage2):

    assert type(stage1) == type(stage2)
    assert_geonode(stage1.node1, stage2.node1)
    assert_geonode(stage1.node2, stage2.node2)
    assert stage1.length == stage2.length
    assert stage1.instruction == stage2.instruction

    return

def assert_plant(plant1, plant2):

    assert type(plant1) == type(plant2)
    assert plant1.name_num == plant2.name_num
    assert plant1.preferred_common_name == plant2.preferred_common_name
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

    assert len(plant1.common_names) == len(plant2.common_names)

    for i in range(len(plant1.common_names)):
        assert plant1.common_names[i] == plant2.common_names[i]

    assert len(plant1.synonyms) == len(plant2.synonyms)

    for i in range(len(plant1.synonyms)):
        assert plant1.synonyms[i] == plant2.synonyms[i]

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# DAO_Plants Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_DAO_Plants_plant_attributes(plant1, plant2):

    # Find plant with a particular name_number

    dao = db.DAO_Plants()

    act_plant = dao.plant_attributes('76294')

    assert_plant(plant1, act_plant)

    act_plant = dao.plant_attributes('97224')

    assert_plant(plant2, act_plant)

    return

def test_DAO_Plants_plants(plant3, plant4, plant5):

    # Find max of 5 plants containing 'ta' in any field

    dao = db.DAO_Plants()

    act_plants = dao.plants('ta', '5')

    exp_plants = []

    exp_plants.append(plant3)
    exp_plants.append(plant4)
    exp_plants.append(plant5)

    assert len(act_plants) == len(exp_plants)

    for i in range(len(act_plants)):
        assert_plant(act_plants[i], exp_plants[i])

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# DAO_GIS Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_DAO_GIS_flower_beds(projnode1, node3, node5):

     # Find closest 2 flower beds containing plant 64031

     dao = db.DAO_GIS(projnode1)

     act_beds = dao.flower_beds('64031', '2')

     exp_beds = []

     exp_beds.append(node3)
     exp_beds.append(node5)

     assert len(act_beds) == len(exp_beds)

     for i in range(len(act_beds)):
         assert_geonode(act_beds[i], exp_beds[i])

     return


def test_DAO_GIS_places(projnode1, place1, place2, place3):

    # Find all places sorted by proximity to projnode1

    dao = db.DAO_GIS(projnode1)

    act_places = dao.places('0')

    exp_places = []

    exp_places.append(place2)
    exp_places.append(place1)
    exp_places.append(place3)

    assert len(act_places) == len(exp_places)

    for i in range(len(act_places)):
        assert_place(act_places[i], exp_places[i])

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# DAO_PlantLists Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_DAO_PlantLists_seasonal_plants(plant1, plant2, plant5, plant6):

    # Find all plants looking good in May

    dao = db.DAO_PlantLists()

    act_plants = dao.seasonal_plants('5', '0')

    exp_plants = []

    exp_plants.append(plant5)
    exp_plants.append(plant1)
    exp_plants.append(plant2)
    exp_plants.append(plant6)

    assert len(act_plants) == len(exp_plants)

    for i in range(len(act_plants)):
        assert_plant(act_plants[i], exp_plants[i])

    return

def test_DAO_PlantLists_bed_plants(plant1, plant2, plant7):

    # Find first 3 plants in bed 5

    dao = db.DAO_PlantLists()

    act_plants = dao.bed_plants('5', '3')

    exp_plants = []

    exp_plants.append(plant7)
    exp_plants.append(plant1)
    exp_plants.append(plant2)

    assert len(act_plants) == len(exp_plants)

    for i in range(len(act_plants)):
        assert_plant(act_plants[i], exp_plants[i])

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# DAO_Route Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_DAO_Route_setup_graph(projnode1):

    # Check Graph setup

    dao = db.DAO_Route(projnode1)

    act_G = dao.setup_graph()

    exp_G = nx.Graph()

    # Manually set up the expected Graph

    exp_G.add_edge((480075.52727804193, 155325.20673843563), (480110.57192593836, 155345.15844900193),
                   weight=40.33793082308226)
    exp_G.nodes[480075.52727804193, 155325.20673843563]['id'] = 1
    exp_G.nodes[480110.57192593836, 155345.15844900193]['id'] = 2

    exp_G.add_edge((480075.52727804193, 155325.20673843563), (480097.58562198514, 155350.179731822),
                   weight=33.32971510457651)
    exp_G.nodes[480075.52727804193, 155325.20673843563]['id'] = 1
    exp_G.nodes[480097.58562198514, 155350.179731822]['id'] = 10

    exp_G.add_edge((480110.57192593836, 155345.15844900193), (480116.2860712755, 155374.54049788768),
                   weight=29.941273689650515)
    exp_G.nodes[480110.57192593836, 155345.15844900193]['id'] = 2
    exp_G.nodes[480116.2860712755, 155374.54049788768]['id'] = 3

    exp_G.add_edge((480110.57192593836, 155345.15844900193), (480153.12022010185, 155351.79401970515),
                   weight=43.07518790884984)
    exp_G.nodes[480110.57192593836, 155345.15844900193]['id'] = 2
    exp_G.nodes[480153.12022010185, 155351.79401970515]['id'] = 12

    exp_G.add_edge((480116.2860712755, 155374.54049788768), (480121.85640956485, 155389.18057912646),
                   weight=15.668568440186627)
    exp_G.nodes[480116.2860712755, 155374.54049788768]['id'] = 3
    exp_G.nodes[480121.85640956485, 155389.18057912646]['id'] = 4

    exp_G.add_edge((480116.2860712755, 155374.54049788768), (480104.45986591815, 155377.15435603145),
                   weight=12.115160922032716)
    exp_G.nodes[480116.2860712755, 155374.54049788768]['id'] = 3
    exp_G.nodes[480104.45986591815, 155377.15435603145]['id'] = 11

    exp_G.add_edge((480121.85640956485, 155389.18057912646), (480113.02015144937, 155403.96862270025),
                   weight=17.231921670228612)
    exp_G.nodes[480121.85640956485, 155389.18057912646]['id'] = 4
    exp_G.nodes[480113.02015144937, 155403.96862270025]['id'] = 5

    exp_G.add_edge((480113.02015144937, 155403.96862270025), (480098.9963780598, 155403.56291188815),
                   weight=14.033740294973267)
    exp_G.nodes[480113.02015144937, 155403.96862270025]['id'] = 5
    exp_G.nodes[480098.9963780598, 155403.56291188815]['id'] = 6

    exp_G.add_edge((480113.02015144937, 155403.96862270025), (480139.37654836953, 155429.19518049734),
                   weight=36.49406422651829)
    exp_G.nodes[480113.02015144937, 155403.96862270025]['id'] = 5
    exp_G.nodes[480139.37654836953, 155429.19518049734]['id'] = 7

    exp_G.add_edge((480098.9963780598, 155403.56291188815), (480104.45986591815, 155377.15435603145),
                   weight=26.975666498644166)
    exp_G.nodes[480098.9963780598, 155403.56291188815]['id'] = 6
    exp_G.nodes[480104.45986591815, 155377.15435603145]['id'] = 11

    exp_G.add_edge((480139.37654836953, 155429.19518049734), (480153.9059029, 155433.15384258004),
                   weight=15.063387998015651)
    exp_G.nodes[480139.37654836953, 155429.19518049734]['id'] = 7
    exp_G.nodes[480153.9059029, 155433.15384258004]['id'] = 8

    exp_G.add_edge((480153.9059029, 155433.15384258004), (480171.8333823625, 155423.17251680512),
                   weight=20.52479885263658)
    exp_G.nodes[480153.9059029, 155433.15384258004]['id'] = 8
    exp_G.nodes[480171.8333823625, 155423.17251680512]['id'] = 9

    exp_G.add_edge((480097.58562198514, 155350.179731822), (480104.45986591815, 155377.15435603145),
                   weight=27.844900425211215)
    exp_G.nodes[480097.58562198514, 155350.179731822]['id'] = 10
    exp_G.nodes[480104.45986591815, 155377.15435603145]['id'] = 11

    assert act_G.number_of_nodes() == exp_G.number_of_nodes()
    assert act_G.number_of_edges() == exp_G.number_of_edges()
    assert list(act_G.nodes) == list(exp_G.nodes)
    assert list(act_G.edges) == list(exp_G.edges)

    for node in act_G.nodes:

        # Check ids
        assert act_G.nodes[node]['id'] == exp_G.nodes[node]['id']

    return


def test_DAO_Route_nearest_node(projnode1, projnode2):

    # Nearest node to current location (projnode1 - place 2)

    dao = db.DAO_Route(projnode1)

    act_node = dao.nearest_node()

    exp_node = projnode2

    assert_projnode(act_node, exp_node)

    return

def test_DAO_Route_place_nearest_node(projnode1, projnode2):

    # Nearest node to place 2

    dao = db.DAO_Route(projnode1)

    act_node = dao.place_nearest_node('2')

    exp_node = projnode2

    assert_projnode(act_node, exp_node)

    return

def test_DAO_Route_bed_nearest_node(projnode1, projnode3):

    # Nearest node to flower bed 4

    dao = db.DAO_Route(projnode1)

    act_node = dao.bed_nearest_node('4')

    exp_node = projnode3

    assert_projnode(act_node, exp_node)

    return


def test_DAO_Route_bed_details(projnode1, node4):
    # Full details of flower bed 4

    dao = db.DAO_Route(projnode1)

    act_node = dao.bed_details(4)

    exp_node = node4

    assert_geonode(act_node, exp_node)

    return

def test_DAO_Route_place_details(projnode1, place1):

    # Full details of place 1

    dao = db.DAO_Route(projnode1)

    act_place = dao.place_details(1)

    exp_place = place1

    assert_place(act_place, exp_place)

    return

def test_DAO_Route_directions(projnode1, geonode8, geonode9):

    # Directions from node 8 to node 9

    dao = db.DAO_Route(projnode1)

    act_stage = dao.directions(8, 9)

    exp_stage = Stage(geonode8, geonode9, 20.52479885263658,'Directions node 8 to node 9')

    assert_stage(act_stage, exp_stage)

    return