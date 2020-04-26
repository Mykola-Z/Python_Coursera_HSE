# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:49:38 2020

@author: mzly903
"""

from itertools import groupby
print(
    len(
        list(
            groupby(
                sorted(
                    set(
                        input().split()
                    )
                    )
                )
            )
        )
)
