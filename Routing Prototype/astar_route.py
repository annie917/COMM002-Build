def calc_astar_route(source_id, destination_id):

    import networkx as nx
    import mysql.connector

    # Sets up a Graph object then calculate shortest path based on source and destination.

    cnx = mysql.connector.connect(user=user, host=host, database=database, password=password)

    # Get source and destination coordinates from database
    cursor = cnx.cursor()

    query = 'SELECT ST_AsText(proj_coord) FROM node where id=' + source_id

    cursor.execute(query)

    source_coords = coords_from_string(cursor.fetchone()[0])

    query = 'SELECT ST_AsText(proj_coord) FROM node where id=' + destination_id

    cursor.execute(query)

    dest_coords = coords_from_string(cursor.fetchone()[0])

    # Fetch edges from database and construct Graph object
    query = 'SELECT node1, node2, ST_AsText(proj1), ST_AsText(proj2), weight ' \
            'FROM edge'

    cursor.execute(query)

    G = nx.Graph()

    for id1, id2, proj1, proj2, weight in cursor:

        x1, y1 = coords_from_string(proj1)
        x2, y2 = coords_from_string(proj2)

        G.add_edge((x1, y1), (x2, y2), weight=weight)
        G.nodes[x1, y1]['id'] = id1
        G.nodes[x2, y2]['id'] = id2

    cursor.close()

    # Calculate path, path length and print them to screen
    path = nx.astar_path(G, source_coords, dest_coords, heuristic=dist, weight='weight')

    for node in path:
        print('Node: ' + str(G.nodes[node]['id']), ', Coordinates (projected): ' + str(node))

    print('\nTotal path length: ',
          nx.astar_path_length(G, source_coords, dest_coords, heuristic=dist, weight='weight'), ' metres')

    return


def dist(a, b):

   #  Euclidean distance function for shortest path algorithm
   (x1, y1) = a
   (x2, y2) = b

   h = ((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2) ** 0.5

   return h


def coords_from_string(db_string):

    x1, y1 = db_string.lstrip('POINT(').rstrip(')').split(' ')
    x1, y1 = tuple(float(x) for x in (x1, y1))

    return (x1, y1)


# Main


#  Read configuration file

import configparser

config = configparser.ConfigParser()
config.read('../Common Files/config.ini')

user = config['MySql']['user']
host = config['MySql']['host']
database = config['MySql']['database']
password = config['MySql']['password']

# Get source and destination nodes
source = input('Enter source node id: ')
destination = input('Enter destination node id: ')

calc_astar_route(source, destination)