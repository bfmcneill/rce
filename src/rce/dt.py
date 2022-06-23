import pendulum


def date_range(after=None, before=None, tz="UTC"):
    if not before:
        before = pendulum.now(tz=tz)
    if not after:
        after = before.subtract(hours=1)

    if isinstance(before, str):
        before = pendulum.parse(before, tz=tz)

    if isinstance(after, str):
        after = pendulum.parse(after, tz=tz)

    return dict(after=after, before=before)
