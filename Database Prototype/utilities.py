def nearest_node_to_bed():

    import mysql.connector

    #     Works out the nearest node to each flower bed and stores it in the flower beds table

    # Open file to store SQL statements
    f = open('update_beds.sql', 'w')
    f.write('USE wisley_pt;\n')

    # First of all, retrieve all flower beds from database in a buffered cursor
    cnx = mysql.connector.connect(user=user, host=host, database='wisley_pt', password=password)

    cursor_beds = cnx.cursor(buffered=True)
    cursor_dist = cnx.cursor(buffered=True)

    query = 'SELECT id, ST_AsText(polygon) FROM flower_bed'

    cursor_beds.execute(query)

    # Loop through beds and find the nearest node using mysql spatial query
    for id, poly in cursor_beds:

        query = 'SELECT id, ST_Distance(ST_PolyFromText(\'' + poly + '\'), proj_coord) AS res ' \
                                                                          'FROM node ORDER BY res'
        cursor_dist.execute(query)

        # Results already sorted on distance, so first node is the one we want
        sql = 'UPDATE flower_bed SET nearest_node = ' + str(cursor_dist.fetchone()[0]) + \
              ' WHERE id = ' + str(id) + ';\n'
        f.write(sql)

    cursor_dist.close()
    cursor_beds.close()
    cnx.close()
    f.close()

    return


def nearest_node_to_place():

    import mysql.connector

    #     Works out the nearest node to each place and stores it in the place table

    # Open file to store SQL statements
    f = open('update_place.sql', 'w')
    f.write('USE wisley_pt;\n')

    # First of all, retrieve all points of interest from database in a buffered cursor
    cnx = mysql.connector.connect(user=user, host=host, database='wisley_pt', password=password)

    cursor_poi = cnx.cursor(buffered=True)
    cursor_dist = cnx.cursor(buffered=True)

    query = 'SELECT id, ST_AsText(proj_coord) FROM place'

    cursor_poi.execute(query)

    # Loop through points of interest and find the nearest node using mysql spatial query
    for id, point in cursor_poi:

        query = 'SELECT id, ST_Distance(ST_PointFromText(\'' + point + '\'), proj_coord) AS res ' \
                                                                          'FROM node ORDER BY res'
        cursor_dist.execute(query)

        # Results already sorted on distance, so first node is the one we want
        sql = 'UPDATE place SET nearest_node = ' + str(cursor_dist.fetchone()[0]) + \
              ' WHERE id = ' + str(id) + ';\n'
        f.write(sql)

    cursor_dist.close()
    cursor_poi.close()
    cnx.close()
    f.close()

    return

def populate_beds():

    import random
    import xml.etree.ElementTree as ET

    # Read in and store the plant name nums
    tree = ET.parse('../Common Files/plantselector.xml')

    plants = []

    for plant in tree.iter(tag='EntityDetailsItems'):

        plants.append(plant.attrib['Name_Num'])

    # Open file to store SQL statements
    f = open('insert_plant_beds.sql', 'w')
    f.write('USE wisley_pt;\n')

    for bed in range(7):

        bed_plants = random.sample(plants, 5)

        for plant in bed_plants:

            sql = 'INSERT INTO plant_bed (plant_id, bed_id) VALUES (' + plant + ', ' + str(bed+1) + ');\n'
            f.write(sql)

    return


def populate_directions():

    import mysql.connector

    # Reads edges from adjacency file
    # Reads nodes from database, calculates weight(length) of each edge
    # and generates SQL to insert into edges table

    # First of all, retrieve all nodes from database and store in dictionary keyed on node id
    cnx = mysql.connector.connect(user=user, host=host, database='wisley_pt', password=password)

    cursor = cnx.cursor()

    query = 'SELECT node1, node2 FROM edge'

    cursor.execute(query)

    # Open file to store SQL statements
    f = open('update_edges_directions.sql', 'w')
    f.write('USE wisley_pt;\n')

    for node1, node2 in cursor:

        # Read in node ids and generate SQL staements to update edges with dummy directions
        sql = 'UPDATE edge '\
            'SET direction_1_to_2 = \'Directions node ' + str(node1) + ' to node ' + str(node2) + '\', ' \
            'direction_2_to_1 = \'Directions node ' + str(node2) + ' to node ' + str(node1) + '\' ' \
            'WHERE node1 = ' + str(node1) + ' AND node2 = ' + str(node2) + ';\n'


        f.write(sql)

    cursor.close()
    cnx.close()

    f.close()

    return


def copy_proj_coordinates():

    import mysql.connector

    #     Works out the nearest node to each flower bed and stores it in the flower beds table

    # Open file to store SQL statements
    f = open('update_proj_coords.sql', 'w')
    f.write('USE wisley_pt;\n')

    # First of all, retrieve all flower beds from database in a buffered cursor
    cnx = mysql.connector.connect(user=user, host=host, database='wisley_pt', password=password)

    cursor = cnx.cursor()

    query = 'SELECT e.node1, e.node2, ST_AsText(n.proj_coord) ' \
            'FROM wisley_pt.edge AS e ' \
            'JOIN wisley_pt.node AS n ' \
            'ON e.node1 = n.id;'

    cursor.execute(query)

    for node1, node2, proj1 in cursor:

        sql = 'UPDATE edge SET proj1 = ST_PointFromText(\'' + proj1 + '\') WHERE node1 = ' + \
              str(node1) + ' AND node2 = ' + str(node2) + ';\n'

        f.write(sql)

    cursor.close()

    cursor = cnx.cursor()

    query = 'SELECT e.node1, e.node2, ST_AsText(n.proj_coord) ' \
            'FROM wisley_pt.edge AS e ' \
            'JOIN wisley_pt.node AS n ' \
            'ON e.node2 = n.id;'

    cursor.execute(query)

    for node1, node2, proj2 in cursor:

        sql = 'UPDATE edge SET proj2 = ST_PointFromText(\'' + proj2 + '\') WHERE node1 = ' + \
              str(node1) + ' AND node2 = ' + str(node2) + ';\n'

        f.write(sql)


    cnx.close()
    f.close()

    return

class Node(object):

    # Base Node class for GeoNode and ProjNode.  Abstract.
    def __init__(self, id, name):

        self.id = id  # int
        self.name = name  # string

        return

class GeoNode(Node):

    # Sub class for storing nodes in geographic coordinate systems - lat, long
    def __init__(self, id, name, long, lat):

        Node.__init__(self, id, name)
        self.long = long  #String
        self.lat = lat   #String

    @classmethod
    # Alternative constructor - populates GeoNode from MySQL POINT string
    def from_db_string(cls, db_string):

        long_and_lat = db_string.lstrip('POINT(').rstrip(')').split(' ')

        return cls(0, '', long_and_lat[0], long_and_lat[1])

    @classmethod
    def from_db_row(cls, db_row):

        # Alternative constructor - populates Node from a database row tuple
        long_and_lat = db_row[1].lstrip('POINT(').rstrip(')').split(' ')

        return cls(db_row[0], db_row[2], long_and_lat[0], long_and_lat[1])

    @classmethod
    def from_kml_string(cls, kml_string):
        # Alternative constructor - populates GeoNode from a KML string
        long_and_lat = kml_string.split(',')

        return cls(0, '', long_and_lat[0], long_and_lat[1])

    def point_string(self):
        # Returns node in format for putting into db as POINT, with srid=4326 (GPS)
        return 'ST_PointFromText(\'POINT(' + self.long + ' ' + self.lat + ')\', 4326)'

    def convert(self):

        # Produces a projected node object from this object
        from pyproj import Proj, transform

        p1 = Proj(geo_string)
        p2 = Proj(proj_string)

        x, y = transform(p1, p2, float(self.long), float(self.lat))

        return ProjNode(self.id, self.name, x, y)
    
class ProjNode(Node):

    # Sub class for storing node in projected coordinate system
    def __init__(self, id, name, x, y):

        Node.__init__(self, id, name)
        self.x = x
        self.y = y

    @classmethod
    # Alternative constructor - populates ProjNode from MySQL POINT string
    def from_db_string(cls, db_string):

        x_and_y = db_string.lstrip('POINT(').rstrip(')').split(' ')

        return cls(0, '', x_and_y[0], x_and_y[1])

    def point_string(self):

        # Returns node in format for putting into db as POINT, with srid=0 (cartesian)
        return 'ST_PointFromText(\'POINT(' + str(self.x) + ' ' + str(self.y) + ')\')'

    def convert(self):

        # Produces a node object with geographic coordinates (lat/long)
        # Should only be done to convert the result of a geometric calculation as accuracy will be lost
        from pyproj import Proj, transform

        p1 = Proj(proj_string)
        p2 = Proj(geo_string)

        long, lat = transform(p1, p2, float(self.x), float(self.y))

        return GeoNode(self.id, self.name, str(long), str(lat))

    def coord_str(self):
        # Construct coordinate string required for polygon corners
        return str(self.x) + ' ' + str(self.y)
    
# Main


#  Read configuration file

import configparser

config = configparser.ConfigParser()
config.read('../Common Files/config.ini')

user = config['MySql']['user']
host = config['MySql']['host']
password = config['MySql']['password']
geo_string = config['Projections']['geographic']
proj_string = config['Projections']['projected']

populate_directions()
copy_proj_coordinates()
nearest_node_to_bed()
nearest_node_to_place()
populate_beds()