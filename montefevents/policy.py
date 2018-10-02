# -*- coding: utf-8 -*-

from __future__ import unicode_literals

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
        return self.make_decision(event)

    def make_decision(self, event):
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
                # If it is wednesday and the seminar is the following monday
                return Decision.ANNOUNCE
        return Decision.IGNORE


class AnnouncePolicy(Policy):
    """
    Announce all the seminar of a given day.
    """
    def make_decision(self, event):
        n_days = event.how_many_days_before(self.ref_date)
        if n_days == 0:
            return Decision.ANNOUNCE

        return Decision.IGNORE


class RemindOnlyPolicy(Policy):
    """
    Send only reminders
    """
    def make_decision(self, event):
        n_days = event.how_many_days_before(self.ref_date)
        if n_days == 0:
            return Decision.REMIND
        return Decision.IGNORE


