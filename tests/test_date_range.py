from rce import dt


def test_date_range():
    after = "2022-06-05"
    before = "2022-06-09"
    tz = None
    dr = dt.date_range(after, before, tz)
    print(f'after: {int(dr["after"].timestamp())}')
    print(f'before: {int(dr["before"].timestamp())}')
