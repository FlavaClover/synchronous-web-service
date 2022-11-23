import socket
import logging
import time

import config


logger = logging.getLogger(__name__)


def handle_request(request: bytes) -> bytes:
    time.sleep(config.DELAY_BEFORE_RESPONSE)

    response = b'Your\'s message to server: ' + request
    return response


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.bind((config.HOST, config.PORT))
        skt.listen()
        logger.info('Socket created. Bind to %s:%s', config.HOST, config.PORT)

        while True:
            try:
                client, address = skt.accept()
            except KeyboardInterrupt:
                logger.info('Server stopped')
                return

            logger.info('Client %s:%s connected', address[0], address[1])

            with client:
                request = client.recv(config.RECEIVE_SIZE)
                response = handle_request(request)
                client.sendall(response)
