import json
import logging as log


class Config:
    def __init__(self, passwd):
        self.dbpass = passwd

    def get_config(self):

        log.info('opening config file...')
        try:
            with open("conf/config.json", "r") as conf:
                data = json.load(conf)
        except IOError:
            log.fatal('error opening config file.')
            exit(1)

        log.info('file: config.json was opened successfully.')
        log.info('initializing programm config...')

        self.order_range = data["orderRange"]
        self.orderHistoryRange = data["orderHistoryRange"]
        self.alpha = data["alpha"]
        self.module = data["module"]
        self.step = data["step"]
        self.volumeAlpha = data["volumeAlpha"]
        self.volumeModule = data["volumeModule"]
        self.volumeStep = data["volumeStep"]
        self.timeAlpha = data["timeAlpha"]
        self.timeModule = data["timeModule"]
        self.timeStep = data["timeStep"]

        self.startDate = data["startDate"]
        self.endDate = data["endDate"]
        self.block1 = data["startBlock1"]
        self.block2 = data["startBlock2"]
        self.block3 = data["startBlock3"]
        self.timestampDiff = data["timestampDiff"]

        log.info('program config initialize finished.')

        log.info('opening dbConfig file...')
        try:
            with open("conf/dbConfig.json", "r") as conf:
                dbData = json.load(conf)
        except IOError:
            log.fatal('Error opening dbConfig file.')
            exit(1)

        log.info('file: dbConfig.json was opened successfully.')

        log.info('initializing database config...')
        self.dbHost = dbData["host"]
        self.dbPort = dbData["port"]
        self.dbUser = dbData["user"]
        self.dbPass = self.dbpass
        self.dbName = dbData["database"]

        log.info('database config initialize finished.')
