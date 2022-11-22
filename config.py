import os
import logging

from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)

load_dotenv()


HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))
RECEIVE_SIZE = int(os.environ.get('RECEIVE_SIZE', 1024))
DELAY_BEFORE_RESPONSE = int(os.environ.get('DELAY_BEFORE_RESPONSE'))
