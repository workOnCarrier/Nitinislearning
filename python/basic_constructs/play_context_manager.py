

from time import sleep
import logging
from copy import copy

logging.basicConfig(filename="trial_logging.log",
                    level=logging.INFO,
                    format="%(asctime)s:%(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)


class ToyWithContextMgr():
    def __init__(self, sleep_counter:int ) -> None:
        logger.info("creating obj")
        self.sleep_counter = sleep_counter
        self.operation = lambda x:x*2

    def __enter__(self):
        logger.info("entering")
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        logger.info("exiting")
        pass
    def sleep(self):
        sleep_for = copy(self.sleep_counter)
        while sleep_for > 0:
            logger.info(f"sleeping for {sleep_for} secs : operation {self.operation(sleep_for)}")
            sleep(1)
            sleep_for = sleep_for - 1



def play_with_toys():
    with ToyWithContextMgr(3) as three_sec_sleep:
        logger.info("about to sleep")
        three_sec_sleep.sleep()
        logger.info("awake now")



if __name__ == "__main__":
    play_with_toys()