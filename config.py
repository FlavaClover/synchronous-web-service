import os

from dotenv import load_dotenv

load_dotenv()


HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))