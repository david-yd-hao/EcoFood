# ------------------------------------------------------------------------
# EcoFood
# Copyright (c) 2022 OpenAI-Hackathon Team 34. All Rights Reserved.
# Licensed under the MIT-style license found in the LICENSE file in the root directory
# ------------------------------------------------------------------------


import argparse
import datetime
import json
import random
import time
import os
from pathlib import Path
import numpy as np


from food import get_recipe_metric

def get_args_parser():
    parser = argparse.ArgumentParser("EcoFood", add_help=False)
    parser.add_argument("--user", default=1, type=float)
    parser.add_argument("--output_dir", default="outputs", type=str)

    return parser


def main(args):
    print("Hello World")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser("ECOFOOD MAIN PYTHON", parents=[get_args_parser()])
    args = parser.parse_args()
    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    main(args)
