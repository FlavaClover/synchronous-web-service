import os
import logging

from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s\t%(name)-20s\t%(threadName)-35s\t%(levelname)-20s\t%(message)s'
)

load_dotenv()


HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))
RECEIVE_SIZE = int(os.environ.get('RECEIVE_SIZE', 1024))
DELAY_BEFORE_RESPONSE = int(os.environ.get('DELAY_BEFORE_RESPONSE'))
