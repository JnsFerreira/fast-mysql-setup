from connection import Connection


def main():
    params = {'user': 'root',
              'password': 'dockerIsAwesome',
              'host': 'localhost',
              'port':'3001',
              'raise_on_warnings': True}

    db = Connection(conn_parameters = params)
    
    print(db.conn)


if __name__ == '__main__':
    main()
