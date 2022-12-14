from dbIface import DbIface
import logging as log
import pymysql
from constants import *

class DB(DbIface):

    def __init__(self, config):
        self.dbconfig = config

    def dbConnect(self):
        try:
            connection = pymysql.connect(
                host=self.dbconfig.dbHost,
                port=self.dbconfig.dbPort,
                user=self.dbconfig.dbUser,
                password=self.dbconfig.dbPass,
                database=self.dbconfig.dbName,
            )
        except Exception as ConnectionError:
            log.error("Connection failed")
            log.error(ConnectionError)
            exit(2)
        finally:
            log.info("Successfully connected to db")

        return connection

    def generateQuery(self, list):
        log.info("Generating sql query...")
        sql_query = "INSERT INTO `order_history`(`id`, `creation_date`, `change_date`, `state`, `direction`, `instrument`, `initial_volume`, `fill_volume`, `initial_price`, `fill_price`) VALUES"
        for index in range(orderHistoryRange):
            sql_query += f"({orderHistory[index][ID]}," \
                         f"'{orderHistory[index][CREATIONDATE]}'," \
                         f"'{orderHistory[index][CHANGEDATE]}'," \
                         f"'{orderHistory[index][STATE]}'," \
                         f"'{orderHistory[index][INSTRUMENT]}'," \
                         f"'{orderHistory[index][DIRECTION]}'," \
                         f"{orderHistory[index][INITALVOLUME]}," \
                         f"{orderHistory[index][FILLVOLUME]}," \
                         f"{orderHistory[index][INITALPRICE]}," \
                         f"{orderHistory[index][FILLPRICE]}),"
        log.info("Successfully generated sql query")

        return sql_query[:-1] + ";"

    def dbInsert(self, list):
        query = self.generateQuery(list)
        log.info("Inserting data to db...")
        connection = self.dbConnect()
        try:
            connection.query(query)
            connection.commit()
        except pymysql.Error as error:
            log.error("Failed to insert query")
            log.error(error)
            exit(2)
        finally:
            log.info("Successfully inserted to db")
            log.info("Process finished!")
            connection.close()
