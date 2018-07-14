class BLO_Plants(object):

    # Business logic class for dealing with the corresponding DAO_Plants data layer object.
    # Handles requests for list of plants that only involve the XML data source.

    def __init__(self):

        from wisley.data_access import DAO_Plants

        # Set up data access object (does not require location or database connection).
        self.dao = DAO_Plants()

    def get_plants(self, search_string, n):

        # Pass parameters to corresponding data layer method.
        # Returns - a list of populated Plant objects, or an empty list if the search string was not found.

        plants = self.dao.plants(search_string, n)

        return plants


class BLO_PlantLists(object):

    # Business logic class for dealing with the corresponding DAO_PlantLists data layer object.
    # Handles requests for lists of plants with no spatial component.

    def __init__(self):

        from wisley.data_access import DAO_PlantLists

        # Set up a data access object and connect to db.
        self.dao = DAO_PlantLists()

    def get_seasonal_plants(self, month, n):

        # Pass parameters to corresponding data layer method.
        # Returns - a list of Plant Objects representing the n seasonal plants,
        # or an empty list if the plant was not found.

        plants = self.dao.seasonal_plants(month, n)

        return plants

    def get_bed_plants(self, id, n):

        # Pass parameters to corresponding data layer method.
        # Returns - a list of Plant Objects representing the n plant in bed with id,
        # or an empty list if the bed was not found or was empty.

        plants = self.dao.bed_plants(id, n)

        return plants


class BLO_GIS(object):

    # Business logic class for dealing with the corresponding DAO_GIS data layer object.
    # Handles requests for lists of flower beds and places near a location.

    def __init__(self, location):

        from wisley.data_access import DAO_GIS

        # Set up a data access object with location (projected coordinates) and connect to db.
        self.dao = DAO_GIS(location.convert())

    def get_flower_beds(self, plant, n):

        # Pass parameters to corresponding data layer method.
        # Returns - a list of GeoNode Objects representing the n flower beds, or an empty list if the plant was not found.

        flower_beds = self.dao.flower_beds(plant, n)

        self.dao.db_close()

        return flower_beds

    def get_places(self, n):

        # Pass parameters to corresponding data layer method.
        # Returns - a list of Place Objects representing the n places, or an empty list not found.

        places = self.dao.places(n)

        self.dao.db_close()

        return places


class BLO_Route(object):

    # Business logic class for dealing with the corresponding DAO_Route data layer object.
    # Handles requests for routes to flower beds and places.

    def __init__(self, location):

        from wisley.data_access import DAO_Route

        # Set up a data access object with location (projected coordinates) and connect to db
        self.dao = DAO_Route(location.convert())

    def get_place_route(self, id):

        # Get node closest to place and calculate route between location and given place
        route = self._get_route(self.dao.place_nearest_node(id))
        # Populate destination details
        route.destination = self.dao.place_details(id)

        return route

    def get_bed_route(self, id):

        # Get node closest to flower bed and calculate route between location and given flower bed
        route = self._get_route(self.dao.bed_nearest_node(id))
        # Populate destination details
        route.destination = self.dao.bed_details(id)

        return route

    def _get_route(self, node):

        import networkx as nx
        from wisley.models import Route

        # Arguments:
        # node - destination node
        # Returns - a Route object populated with the shortest route between location and destination node

        # Read in network from database
        G = self.dao.setup_graph()

        # Find node closet to location for starting point
        start_node = self.dao.nearest_node()

        route = Route()

        # Calculate shortest route
        nodes = nx.astar_path(G, (start_node.x, start_node.y), (node.x, node.y), heuristic=self._dist, weight='weight')

        # Loop through nodes getting full details and directions from database

        node1_id = 0

        for node in nodes:

            # Retrieve node id using id attribute
            node2_id = G.nodes[node]['id']

            if node1_id != 0:
                route.stages.append(self.dao.directions(node1_id, node2_id))
                route.length += route.stages[-1].length

            node1_id = node2_id

        return route

    def _dist(self, current, destination):

        # Heuristic function for A* algorithm.  Calculates Euclidean distance between two points

        x1 = current[0]
        y1 = current[1]
        x2 = destination[0]
        y2 = destination[1]

        h = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        return h

