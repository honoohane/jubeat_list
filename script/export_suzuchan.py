#!/usr/bin/env python3

import pandas as pd
import os


def export_suzuchan(csv="output/jubeat_list.csv"):
    df = pd.read_csv(csv)
    result = pd.concat([pd.DataFrame(data=[(r.title, 'bsc', r.bsc_level),
                                         (r.title, 'adv', r.adv_level),
                                         (r.title, 'ext', r.ext_level)],
                                   columns=['title', 'difficulty', 'level'])
                      for _, r in df.iterrows()], ignore_index=True)
    result.to_csv("output/jubeat_list_per_chart.csv")