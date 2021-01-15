import mysql.connector

class Connection:
    def __init__(self, conn_parameters):
        self.conn = mysql.connector.connect(**conn_parameters)

    def query(self):
        """You can implement a lot of functions, like on to query based on sql string"""
        pass
