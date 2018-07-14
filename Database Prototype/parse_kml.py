import xml.etree.ElementTree as ET

def import_polygons():

    # Parses KML into SQL to insert polygons into database

    tree = ET.parse('./Elvetham.kml')

    f = open('create_polygons.sql','w')
    f.write('USE wisley_pt;\n')

    for polygon in tree.iter(tag='Polygon'):

        sql = 'INSERT INTO flower_bed (polygon) VALUES (ST_PolyFromText(\'POLYGON('

        for elem in polygon.iter(tag='coordinates'):

            corners = elem.text.split('\n')

            # Grab first node and convert to projected coordinates as will be used for geometry calculations
            node1 = GeoNode.from_kml_string(corners.pop(0)).convert()

            coord_text = '(' + node1.coord_str()

            for corner in corners:

                node = GeoNode.from_kml_string(corner).convert()

                coord_text += ', ' + node.coord_str()

            # Repeat first coordinate as SQL requires polygons to be closed and add to SQL statement
            coord_text +=  ', ' + node1.coord_str() + ')'


            sql += coord_text + ')\'));\n'

            f.write(sql)

    f.close()

    return


def import_points():

    tree = ET.parse('./nodes.kml')

    f = open('create_nodes.sql', 'w')

    f.write('USE wisley_pt;\n')

    # Check if Placemark is a Point and if so, grab name

    for placemark in tree.iter(tag='Placemark'):

        if placemark.find('Point'):

            name = placemark.find('name').text

            for point in placemark.iter(tag='Point'):

                sql = 'INSERT INTO node (coordinates, proj_coord, name) VALUES ('

                geo_node = GeoNode.from_kml_string(point.find('coordinates').text)
                proj_node = geo_node.convert()

                # replace , in coordinate pair with a space, then add name
                sql += geo_node.point_string() + ', ' + proj_node.point_string() + ', \'' + name + '\');\n'

                f.write(sql)

    f.close()

    return


def populate_places():

    f = open('create_places.sql', 'w')
    f.write('USE wisley_pt;\n')

    geo_node = GeoNode.from_db_string('POINT(-0.85198112970328 51.2924438640308)')
    proj_node = geo_node.convert()


    sql = 'INSERT INTO place (name, coordinates, proj_coord, description) VALUES (\'Picnic Area\', '

    sql += geo_node.point_string() + ', ' + proj_node.point_string() + ', \'Picnic Area Description\');\n'

    f.write(sql)

    geo_node = GeoNode.from_db_string('POINT(-0.85324042683577 51.2912194132039)')
    proj_node = geo_node.convert()

    sql = 'INSERT INTO place (name, coordinates, proj_coord, description) VALUES (\'Entrance\', '

    sql += geo_node.point_string() + ', ' + proj_node.point_string() + ', \'Entrance Description\');\n'

    f.write(sql)

    geo_node = GeoNode.from_db_string('POINT(-0.8506869638536 51.2924270909523)')
    proj_node = geo_node.convert()

    sql = 'INSERT INTO place (name, coordinates, proj_coord, description) VALUES (\'Nature Reserve\', '

    sql += geo_node.point_string() + ', ' + proj_node.point_string() + ', \'Nature Reserve Description\');\n'

    f.write(sql)

    return


def coords_from_string(db_string):

    x1, y1 = db_string.lstrip('POINT(').rstrip(')').split(' ')
    x1, y1 = tuple(float(x) for x in (x1, y1))

    return (x1, y1)

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

geo_string = config['Projections']['geographic']
proj_string = config['Projections']['projected']


import_polygons()
import_points()
populate_places()
