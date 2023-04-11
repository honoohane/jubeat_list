#!/usr/bin/env python3

import pandas as pd


def export_suzuchan(csv="jubeat_list.csv"):
    df = pd.read_csv(csv)
    return pd.concat([pd.DataFrame(data=[(r.title, 'bsc', r.bsc_level),
                                         (r.title, 'adv', r.adv_level),
                                         (r.title, 'ext', r.ext_level)],
                                   columns=['title', 'difficulty', 'level'])
                      for _, r in df.iterrows()], ignore_index=True)
