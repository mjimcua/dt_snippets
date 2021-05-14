import datetime
from datetime import timedelta


def get_first_day_of_week(date: datetime.date):
    return date - timedelta(days=date.weekday())


def get_last_day_of_week(date: datetime.date):
    return get_first_day_of_week(date) + timedelta(days=6)


def get_first_day_of_month(date: datetime.date):
    year = date.year
    month = date.month
    return datetime.date(day=1, month=month, year=year)


def get_last_day_of_month(date: datetime.date):
    next_month = date.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def get_week_number(date: datetime.date):
    return date.isocalendar()[1]


def get_dates_day_by_day(start_date, end_date):
    dates = []
    while start_date <= end_date:
        dates.append(start_date)
        start_date += datetime.timedelta(days=1)
    return dates


def get_dates_week_by_week(start_date, end_date):
    start_date = get_first_day_of_week(start_date)
    end_date = get_last_day_of_week(end_date)
    dates = []
    week = -1
    while start_date <= end_date:
        if week != get_week_number(start_date):
            dates.append(start_date)
            week = get_week_number(start_date)
        start_date += datetime.timedelta(days=1)

    return dates


def get_dates_month_by_month(start_date, end_date):

    dates = []
    month = -1
    while start_date <= end_date:
        if month != start_date.month:
            dates.append(start_date)
            month = start_date.month
        start_date += datetime.timedelta(days=1)
    return dates


def get_dates_year_from_month_by_period(start_date, period):

    dates = []
    month = start_date.month
    year = start_date.year
    if period == 'prior_1':
        year -= 1
    if period == 'prior_2':
        year -= 2
    date = datetime.date(day=1, month=month, year=year)
    dates.append(date)
    return dates


def get_dates_year_from_period(start_date, end_date, period):
    dates = []
    start_month = start_date.month
    start_year = start_date.year
    end_month = end_date.month
    end_year = end_date.year

    if period == 'prior_1':
        start_year -= 1
        end_year -= 1
    if period == 'prior_2':
        start_year -= 2
        end_year -= 2

    star_date_p = datetime.date(day=1, month=start_month, year=start_year)
    end_date_p = datetime.date(day=1, month=end_month, year=end_year)
    return get_dates_month_by_month(star_date_p, end_date_p)


def get_week_days_from_date(date: datetime.date):

    first_day_week = get_first_day_of_week(date)
    last_day_week = get_last_day_of_week(date)

    dates = []
    while first_day_week <= last_day_week:
        dates.append(first_day_week)
        first_day_week += datetime.timedelta(days=1)

    return dates


def get_month_days_from_date(date: datetime.date):
    """
    A Partir de una fecha devuelve un listado con todos los días del mes al que pertenece dicha fecha
    :param date:
    :return: list[dates]
    """

    year = date.year
    month = date.month
    dates = []

    add_day = datetime.timedelta(days=1)
    month_first_day = datetime.date(year, month, 1)

    reference_day = month_first_day
    while reference_day.month == month:
        dates.append(reference_day)
        reference_day += add_day

    return dates


def get_month_weeks_from_date(date: datetime.date):

    start_date = get_first_day_of_month(date)
    end_date = get_last_day_of_month(date)
    dates = []
    week = -1

    while start_date <= end_date:
        if week != get_week_number(start_date):
            dates.append(start_date)
            week = get_week_number(start_date)
        start_date += datetime.timedelta(days=1)

    return dates


def ordinal_to_date(ordinal):
    return datetime.datetime.fromordinal(ordinal)


def ordinal_to_month_date(ordinal):
    ref_date = ordinal_to_date(ordinal)
    return datetime.datetime(day=1, month=ref_date.month, year=ref_date.year)


def datetime_to_ordinal(date_object):
    return datetime.datetime.toordinal(date_object)