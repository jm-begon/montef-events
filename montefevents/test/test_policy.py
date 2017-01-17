# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from nose.tools import assert_equal

from datetime import datetime, timedelta

from montefevents import Seminar, Decision, Policy


def _today():
    return datetime.today()

def _day_after(date=_today()):
    return date + timedelta(days=1)

def _yesterday(date=_today()):
    return date - timedelta(days=-1)

def _last_week(date=_today()):
    return date - timedelta(days=-7)

def _day_after_day_after(date=_today()):
    return date + timedelta(days=2)

def _next_week(date=_today()):
    return date + timedelta(days=7)

def _much_later(date=_today()):
    return date + timedelta(days=30)


def _basic_seminar(date):
    return Seminar("test seminar", "test speaker",
                   date,
                   "test location", "test contact", "test abstract")

def _tba_seminar(date):
    return Seminar("TBA", "test speaker",
                   date,
                   "test location", "test contact", "test abstract")


def test_last_week():
    policy = Policy()
    sem = _basic_seminar(_last_week())
    tba = _tba_seminar(_last_week())
    assert_equal(policy(sem), Decision.IGNORE)
    assert_equal(policy(tba), Decision.IGNORE)


def test_yesterday():
    policy = Policy()
    sem = _basic_seminar(_yesterday())
    tba = _tba_seminar(_yesterday())
    assert_equal(policy(sem), Decision.IGNORE)
    assert_equal(policy(tba), Decision.IGNORE)



def test_today():
    policy = Policy()
    sem = _basic_seminar(_today())
    tba = _tba_seminar(_today())
    assert_equal(policy(sem), Decision.REMIND)
    assert_equal(policy(tba), Decision.IGNORE)



def test_day_after():
    ref_dates = [datetime(2016, 12, 5, 4, 10, 00),  # Monday
                 datetime(2016, 12, 6, 4, 10, 00)]  # Tuesday
    expectations = [Decision.ANNOUNCE, Decision.IGNORE]
    for ref_date, expectation in zip(ref_dates, expectations):
        policy = Policy(ref_date)
        seminar_date = _day_after(ref_date)
        sem = _basic_seminar(seminar_date)
        tba = _tba_seminar(seminar_date)
        assert_equal(sem.how_many_days_before(ref_date), 1)
        assert_equal(policy(sem), expectation)
        assert_equal(policy(tba), Decision.IGNORE)



def test_day_after_day_after():
    ref_dates = [datetime(2016, 12, 5, 4, 10, 00),  # Monday
                 datetime(2016, 12, 6, 4, 10, 00)]  # Tuesday
    expectations = [Decision.ANNOUNCE, Decision.IGNORE]
    for ref_date, expectation in zip(ref_dates, expectations):
        policy = Policy(ref_date)
        seminar_date = _day_after_day_after(ref_date)
        sem = _basic_seminar(seminar_date)
        tba = _tba_seminar(seminar_date)
        assert_equal(sem.how_many_days_before(ref_date), 2)
        assert_equal(policy(sem), expectation)
        assert_equal(policy(tba), Decision.IGNORE)


def test_next_week():
    policy = Policy()
    sem = _basic_seminar(_much_later())
    tba = _tba_seminar(_much_later())
    assert_equal(policy(sem), Decision.IGNORE)
    assert_equal(policy(tba), Decision.IGNORE)


def test_much_later():
    policy = Policy()
    sem = _basic_seminar(_much_later())
    tba = _tba_seminar(_much_later())
    assert_equal(policy(sem), Decision.IGNORE)
    assert_equal(policy(tba), Decision.IGNORE)


def test_mondays():
    ref_dates_wrong = [datetime(2017, 1, 16, 10, 00),  # Monday
                       datetime(2017, 1, 17, 10, 00),  # Tuesday
                       datetime(2017, 1, 19, 10, 00),  # Thursday
                       datetime(2017, 1, 20, 10, 00),  # Friday
                       datetime(2017, 1, 21, 10, 00),  # Saturday
                       datetime(2017, 1, 22, 10, 00),  # Sunday
                       ]

    ref_date_announce = datetime(2017, 1, 18, 10, 00)  # Wendnesday
    seminar_date = datetime(2017, 1, 23, 10, 00)  # Monday

    sem = _basic_seminar(seminar_date)
    policy = Policy(ref_date_announce)
    assert_equal(policy(sem), Decision.ANNOUNCE)
    policy = Policy(seminar_date)
    assert_equal(policy(sem), Decision.REMIND)

    for ref_date in ref_dates_wrong:
        policy = Policy(ref_date)
        assert_equal(policy(sem), Decision.IGNORE)



