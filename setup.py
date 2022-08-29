import logging as log
from getpass import getpass
from config import Config
from workflow import Workflow


class Setup:

    def get_db_pass(self):
        db_pass = getpass(prompt='Please, enter db password: ', stream=None)
        return db_pass

    def setup(self):
        log.basicConfig(filename="logs/log", format='%(levelname)s: %(message)s  at %(asctime)s', level=log.DEBUG)
        dbpass = self.get_db_pass()

        config = Config(passwd=dbpass)

        workflow = Workflow(setupconfig=config.get_config())
        workflow.workflow()
