import wisley.bus_layer as bl
from wisley.models import GeoNode
from wisley.models import Place
from wisley.models import Stage
from wisley.models import Route

import pytest

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Node test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*


@pytest.fixture()
def geonode1():
    return GeoNode(1, 'Node 1', '-0.85302115624881', '51.2914391458255')

@pytest.fixture()
def geonode2():
    return GeoNode(2, 'Node 2', '-0.85251421874499', '51.2916135892949')

@pytest.fixture()
def geonode3():
    return GeoNode(3, 'Node 3', '-0.8524257058475', '51.2918769305846')

@pytest.fixture()
def geonode4():
    return GeoNode(4, 'Node 4', '-0.85234255736804', '51.2920077620013')

@pytest.fixture()
def geonode12():
    return GeoNode(12, 'Node 12', '-0.8519026750896', '51.2916672640752')

@pytest.fixture()
def geonode0():
    # centre of bed 4
    return GeoNode(0, '', '-0.8517447', '51.2917413')

@pytest.fixture()
def geonode5():
    return GeoNode(7, 'Flower Bed 7', '-0.8524337425712866', '51.292041426751496')

@pytest.fixture()
def geonode6():
    # place 2
    return GeoNode(0, '', '-0.85324042683577', '51.2912194132039')

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Place test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

@pytest.fixture()
def place2():
    place = Place(2, 'Entrance', '-0.85324042683577', '51.2912194132039')
    place.description = 'Entrance Description'

    return place

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Stage test fixtures
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

@pytest.fixture()
def stage_1_2(geonode1, geonode2):
    return Stage(geonode1, geonode2, 40.33793082308226, 'Directions node 1 to node 2')

@pytest.fixture()
def stage_2_1(geonode1, geonode2):
    return Stage(geonode2, geonode1, 40.33793082308226, 'Directions node 2 to node 1')

@pytest.fixture()
def stage_2_3(geonode2, geonode3):
    return Stage(geonode2, geonode3, 29.941273689650515, 'Directions node 2 to node 3')

@pytest.fixture()
def stage_3_4(geonode3, geonode4):
    return Stage(geonode3, geonode4, 15.668568440186627, 'Directions node 3 to node 4')

@pytest.fixture()
def stage_12_2(geonode2, geonode12):
    return Stage(geonode12, geonode2, 43.07518790884984, 'Directions node 12 to node 2')

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

def assert_stage(stage1, stage2):

    assert type(stage1) == type(stage2)
    assert_geonode(stage1.node1, stage2.node1)
    assert_geonode(stage1.node2, stage2.node2)
    assert stage1.length == stage2.length
    assert stage1.instruction == stage2.instruction

    return

def assert_route(route1, route2):

    assert type(route1) == type(route2)
    assert route1.length == route2.length
    assert_geonode(route1.destination, route2.destination)
    assert len(route1.stages) == len(route2.stages)

    for i in range(len(route1.stages)):
        assert_stage(route1.stages[i], route2.stages[i])

    return

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# BLO_Route Tests
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

def test_BLO_Route_get_place_route(geonode0, place2, stage_12_2, stage_2_1):

    blo = bl.BLO_Route(geonode0)

    act_route = blo.get_place_route(2)

    exp_route = Route()

    exp_route.length = 83.4131187319321
    exp_route.destination = place2
    exp_route.stages = []
    exp_route.stages.append(stage_12_2)
    exp_route.stages.append(stage_2_1)

    assert_route(act_route, exp_route)

    return

def test_BLO_Route_get_bed_route(geonode6, geonode5, stage_1_2, stage_2_3, stage_3_4):

    blo = bl.BLO_Route(geonode6)

    act_route = blo.get_bed_route(7)

    exp_route = Route()

    exp_route.length = 85.94777295291941
    exp_route.destination = geonode5
    exp_route.stages = []
    exp_route.stages.append(stage_1_2)
    exp_route.stages.append(stage_2_3)
    exp_route.stages.append(stage_3_4)

    assert_route(act_route, exp_route)

    return