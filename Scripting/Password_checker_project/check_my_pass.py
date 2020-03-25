import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # 5 first symbols of HASHED Password
    res = requests.get(url)
    if res.status_code != 200:  # status_code = 200 when user passes 5 str symbols as an argument
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
        # This error will be raised if user gives str that not 5 symbols long
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()  # hashing object must be encoded with utf8
    first5_char, tail = sha1password[:5], sha1password[5:]  # first 5 chars and everything after first 5
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Password: {password} was found {count} times.')
        else:
            print(f'Password: {password} was not found. ')
    return 'done!'


if __name__ == '__main__':
    main(sys.argv[1:])
