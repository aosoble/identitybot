import os
import MySQLdb

class Introduction:
    def __init__(self):
        MYSQLDB_ENDPOINT = os.environ['MYSQLDB_ENDPOINT']
        MYSQLDB_USERNAME = os.environ['MYSQLDB_USERNAME']
        MYSQLDB_PASSWORD = os.environ['MYSQLDB_PASSWORD']
        MYSQLDB_DATABASE = os.environ['MYSQLDB_DATABASE']

        self.conn = MySQLdb.connect(host = MYSQLDB_ENDPOINT, user = MYSQLDB_USERNAME, passwd = MYSQLDB_PASSWORD, db = MYSQLDB_DATABASE)

    def addIntroduction(self, server_id, user_id, message):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO introduction (server_id,user_id,message) VALUES (%s,%s,%s)", (server_id, user_id, message,)
        )
        self.conn.commit()

    def editIntroduction(self, introduction_id, message):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE introduction SET message = %s WHERE id = %s", (message, introduction_id,)
        )
        self.conn.commit()

    def newIntroduction(self, server_id, user_id, message):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id FROM introduction WHERE server_id = %s AND user_id = %s", (server_id, user_id,)
        )
        if cursor.rowcount:
            introduction_id = cursor.fetchone()[0]
            self.editIntroduction(introduction_id,message)
        else:
            self.addIntroduction(server_id,user_id,message)
    
    def getIntroduction(self, server_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT message FROM introduction WHERE server_id = %s AND user_id = %s", (server_id, user_id,)
        )
        intro = cursor.fetchone()
        if intro:
            return intro[0]
        else:
            return None

    def listIntroducedUsers(self, server_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT user_id FROM introduction WHERE server_id = %s", (server_id,)
        )
        results = cursor.fetchall()
        users = []
        for user in results:
            users.append(user[0])
        return users

    def deleteIntroduction(self, server_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM introduction WHERE server_id = %s AND user_id = %s", (server_id,user_id,)
        )
        self.conn.commit()