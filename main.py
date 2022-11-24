import enum
import argparse
from threading import Thread

import synchronous_server
import thread_server
import config
import client


class ServerType(enum.Enum):
    SYNCHRONOUS = 'S'
    THREAD = 'T'
    ASYNCHRONOUS = 'A'


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('Testing of synchronous web-service')

    parser.add_argument(
        '--host', '-H', help='Set host of server', type=str,
        default=config.HOST
    )
    parser.add_argument(
        '--port', '-p', help='Set port of server', type=int,
        default=config.PORT
    )

    parser.add_argument(
        '--count', '-c', help='Set count of clients', type=int,
        default=1
    )

    parser.add_argument(
        '--type', '-t', help='Type of server. S - synchronous, T - threads, A - asynchronous',
        type=ServerType, required=True
    )

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.type == ServerType.SYNCHRONOUS:
        server = synchronous_server
    elif args.type == ServerType.THREAD:
        server = thread_server
    else:
        print('A')

    server_thread = Thread(target=server.server, args=(args.host, args.port), daemon=True)
    server_thread.start()

    client.requests(args.count, args.host, args.port)

    server_thread.join()


if __name__ == '__main__':
    main()
