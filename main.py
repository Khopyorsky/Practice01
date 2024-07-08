import argparse

from models import User


def get_args():
    parser = argparse.ArgumentParser(description='Creates User object')
    parser.add_argument('first_name', type=str, help='First name')
    parser.add_argument('last_name', type=str, help='Last name')
    parser.add_argument('age', type=int, help='Age')
    parser.add_argument('password', type=str, help='Password')
    args = parser.parse_args()
    return args.first_name, args.last_name, args.age, args.password


def main():
    args = get_args()
    person = User(*args)
    person.signalize()
    person.save()


if __name__ == '__main__':
    main()
