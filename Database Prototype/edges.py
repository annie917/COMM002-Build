def initialise_edges():

    import mysql.connector
    from geopy.distance import geodesic


    # Reads edges from adjacency file
    # Reads nodes from database, calculates weight(length) of each edge
    # and generates SQL to insert into edges table

    # First of all, retrieve all nodes from database and store in dictionary keyed on node id
    cnx = mysql.connector.connect(user=user, host=host, database=database, password=password)

    cursor = cnx.cursor()

    query = 'SELECT id, ST_AsText(coordinates) FROM node'

    cursor.execute(query)

    node_lat_long = {}

    for id, coords in cursor:

        # Distance calculation done on ellipsoid with lat and long.
        # geodesic calculation takes order lat-long, so store like this in tuple
        node = GeoNode.from_db_string(coords)
        node_lat_long[id] = float(node.lat), float(node.long)

    cursor.close()
    cnx.close()

    # Open adjacency file

    f1 = open('./adj_list.txt', 'r')
    f2 = open('create_edges.sql', 'w')
    f2.write('USE wisley;\n')

    for line in f1:

        node_ids = line.split()

        # Separate out first node in line
        origin_node_id = node_ids.pop(0)

        # Loop through remaining nodes on line (adjacent to origin_node) and generate SQL
        for id in node_ids:

            # Use geodesic method to calculate distance between nodes (in metres)
            distance = (geodesic(node_lat_long[int(origin_node_id)], node_lat_long[int(id)]).m)

            query = 'INSERT INTO edge (node1, node2, weight) VALUES (\'' + \
                    origin_node_id + '\', \'' + id + '\', ' + str(distance) +');'

            f2.write(query + '\n')

    f2.close()
    f1.close()

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

    
import configparser

config = configparser.ConfigParser()
config.read('../Common Files/config.ini')

user = config['MySql']['user']
host = config['MySql']['host']
database = config['MySql']['database']
password = config['MySql']['password']
geo_string = config['Projections']['geographic']
proj_string = config['Projections']['projected']

initialise_edges()
