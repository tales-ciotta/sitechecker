import argparse


def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Checa a disponibilidade do site"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Insira uma ou mais URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Lê URLs de um arquivo",
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="Roda a checagem de forma assíncrona",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    print(f'O status de "{url}" é:', end=" ")
    if result:
        print('O site está Online! 👍')
    else:
        print(f'O site está Offline 👎 \n  Erro: "{error}"')