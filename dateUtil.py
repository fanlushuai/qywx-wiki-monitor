import datetime


def today():
    return datetime.date.today().strftime('%Y-%m-%d')


def yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday.strftime('%Y-%m-%d')


if __name__ == "__main__":
    print today()
    print yesterday()
