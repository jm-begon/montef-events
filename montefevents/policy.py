# -*- coding: utf-8 -*-

from __future__ import unicode_literals

__author__ = "Begon Jean-Michel <jm.begon@gmail.com>"

from datetime import datetime


class Decision(object):
    IGNORE = "IGNORE"
    ANNOUNCE = "ANNOUNCE"
    REMIND = "REMIND"

class Policy(object):
    def __init__(self, ref_date=datetime.today()):
        self.ref_date = ref_date

    def __call__(self, event):
        if not event.is_filled():
            return Decision.IGNORE
        n_days = event.how_many_days_before(self.ref_date)
        if 0 <= n_days < 7:
            # If the seminar is withing the week
            if n_days == 0:
                # If the seminar is today
                return Decision.REMIND
            elif self.ref_date.weekday() == 0:  # Monday
                # If it is monday
                return Decision.ANNOUNCE
            elif self.ref_date.weekday() == 2 and n_days == 5:
                # If it is wendnesday and the seminar is the following monday
                return Decision.ANNOUNCE
        return Decision.IGNORE
