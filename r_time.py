from datetime import datetime


def deadlines(year=2022, mouth=6, day=30):
    now = datetime.now().timestamp()
    expire = datetime(year, mouth, day, 0, 0).timestamp()
    res = expire - now
    if res < 0:
        raise Exception


if __name__ == '__main__':
    deadlines()
    print('ok')
