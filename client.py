import logging
import socket
from threading import Thread

from mimesis.locales import Locale
from mimesis import Person, Text

import config


logger = logging.getLogger(__name__)


def client_request(client_name: str, msg: str, host: str, port: int):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with skt:
        skt.connect((host, port))
        skt.sendall(msg.encode(encoding='utf-8'))
        logger.info('%s send message to server', client_name)

        response = skt.recv(config.RECEIVE_SIZE)
        logger.debug('%s receive message from server', response.decode(encoding='utf-8'))


def requests(client_count: int, host: str = config.HOST, port: int = config.PORT):
    randomizer_person = Person(Locale.EN)
    randomizer_text = Text(Locale.EN)

    request_threads = [
        Thread(
            target=client_request,
            name=f'Thread-{i}',
            args=(
                randomizer_person.full_name(), randomizer_text.word(),
                host, port
            )
        )
        for i in range(client_count)
    ]

    logger.info('Clients created')

    for request_thread in request_threads:
        request_thread.start()

    for request_thread in request_threads:
        request_thread.join()
