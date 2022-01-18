from __future__ import annotations

import logging
import time
from argparse import ArgumentParser
from pathlib import Path

import numpy
import pandas

logger = logging.getLogger(__name__)


logging_formatter = "%(levelname)-8s : %(asctime)s : %(name)s : %(message)s"
logging.basicConfig(format=logging_formatter)
logging.getLogger(__name__).setLevel(level=logging.DEBUG)


def output_assigned_table(input_csv: Path, table_count: int, output_csv: Path):
    df = pandas.read_csv(input_csv)
    users = df.iloc[:, 1].dropna().values
    logger.debug(f"user_count = {len(users)}")
    logger.debug(f"original users:: {users}")

    numpy.random.seed(int(time.time()))
    numpy.random.shuffle(users)
    logger.debug(f"shuffled users: {users}")

    codepoint_A = ord("A")

    results = []
    for index, user in enumerate(users):
        table_index = index % table_count
        table_name = chr(codepoint_A + table_index)
        results.append({"user": user, "table_name": table_name})

    df_output = pandas.DataFrame(results)
    df_output.sort_values(["user"], inplace=True)
    logger.debug(df_output)
    df_output.to_csv(str(output_csv), index=False, encoding="utf_8_sig")
    return df_output


def parse_args():
    parser = ArgumentParser(allow_abbrev=False, description="NGK2022Sの懇親会用に参加者のテーブルを決める。")
    parser.add_argument("-i", "--input", type=Path, required=True, help="ユーザの一覧が記載されたCSVのパス。2列目のユーザ名を読み込む。")
    parser.add_argument("--table_count", type=int, required=True, help="テーブルごとのユーザ数")
    parser.add_argument("-o", "--output", type=Path, required=True, help="出力先CSVのパス")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_assigned_table(input_csv=args.input, table_count=args.table_count, output_csv=args.output)


if __name__ == "__main__":
    main()
