def populate_months():

    # Populate season table with each plant from plant_bed and allocate it a random season

    import mysql.connector
    import random

    cnx = mysql.connector.connect(user=user, host=host, database='wisley_pt', password=password)

    cursor = cnx.cursor()

    query = 'SELECT DISTINCT plant_id FROM plant_bed'

    cursor.execute(query)

    # Open file to store SQL statements
    f = open('write_months.sql', 'w')
    f.write('USE wisley_pt;\n')

    for plant in cursor:

        # Pick two random months
        r = random.sample(range(1,13), 2)

        sql = 'INSERT INTO plant_month (plant_id, month_id) VALUES (\'' + \
                str(plant[0]) + '\', ' + str(r[0]) + ');\n'
        f.write(sql)

        sql = 'INSERT INTO plant_month (plant_id, month_id) VALUES (\'' + \
                str(plant[0]) + '\', ' + str(r[1]) + ');\n'

        f.write(sql)

    cursor.close()
    cnx.close()

    f.close()


    return


# Main


#  Read configuration file

import configparser

config = configparser.ConfigParser()
config.read('../Common Files/config.ini')

user = config['MySql']['user']
host = config['MySql']['host']
password = config['MySql']['password']

populate_months()
