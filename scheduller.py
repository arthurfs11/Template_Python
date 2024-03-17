import schedule
import time
from app import main
from dateUts import *
from app.Config import logger

logger.success(now(fmt="brz+hr"))

schedule.every(10).seconds.do(main)

while(1):
    schedule.run_pending()
    time.sleep(10)