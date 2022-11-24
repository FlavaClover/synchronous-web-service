import socket
import logging
import time
from threading import Thread

import config


logger = logging.getLogger(__name__)


def handle_request(client: socket, address: tuple) -> bytes:
    with client:
        request = client.recv(config.RECEIVE_SIZE)

        logger.debug(
            'Client %s:%s send \'%s\'',
            address[0], address[1], request.decode(encoding='utf-8')
        )

        time.sleep(config.DELAY_BEFORE_RESPONSE)

        response = b'Your\'s message to server: ' + request
        client.sendall(response)
        logger.info('Server send response to client %s:%s', address[0], address[1])

    return response


def server(host: str = config.HOST, port: int = config.PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.bind((host, port))
        skt.listen()
        logger.info('Socket created. Bind to %s:%s', host, port)

        while True:
            try:
                client, address = skt.accept()
            except KeyboardInterrupt:
                logger.info('Server stopped')
                return

            logger.info('Client %s:%s connected', address[0], address[1])

            client_thread = Thread(
                target=handle_request, args=(client, address), daemon=True
            )

            client_thread.name = client_thread.name + ' Handle request'

            client_thread.start()
