import os

import ipaddress as ipaddr

from phenix_apps.apps   import AppBase
from phenix_apps.common import logger, utils, settings

class Test(AppBase):
    def __init__(self):
        AppBase.__init__(self, 'test')


        self.execute_stage()

        # We don't (currently) let the parent AppBase class handle this step
        # just in case app developers want to do any additional manipulation
        # after the appropriate stage function has completed.
        print(self.experiment.to_json())


    def configure(self):
        logger.log('INFO', f'Configuring user app: {self.name}')

        logger.log('INFO', f'Configured user app: {self.name}')


    def pre_start(self):
        logger.log('INFO', f'Starting user application: {self.name}')

        logger.log('INFO', f'Started user application: {self.name}')


def main():
  Test()


if __name__ == '__main__':
  main()
