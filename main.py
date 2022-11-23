import argparse
from threading import Thread

import config
import synchronous_server
import client


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

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    server_thread = Thread(target=server.server, args=(args.host, args.port), daemon=True)
    server_thread.start()

    client.requests(args.count, args.host, args.port)

    server_thread.join()


if __name__ == '__main__':
    main()
