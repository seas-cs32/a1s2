import requests
import json
import webbrowser

def hlib(book):
    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'http'
    hostname = 'webservices.lib.harvard.edu'
    path = '/rest/v2/hollisplus/search/dc/'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'q': book, 'limit': 5}

    # Add a field to the request header saying what we accept
    accept = {'Accept': 'application/json'}

    response = requests.get(url, params=query, headers=accept)

    # Return a list of matching items from the received response
    if response.json()['results']['resultSet'] == {}:
        return []
    else:
        return response.json()['results']['resultSet']['item']


def main():
    desired_book = input("What's the title of your desired book? ")

    print(f'Searching HOLLIS for "{desired_book}"')
    items = hlib(desired_book)

    # Launch a browser window if we find the desired book
    for item in items:
        if item['dc:title'].lower() == desired_book.lower():
            # Grab this book's HOLLIS number
            hollis_num = item['id']

            # Open a browser window to the appropriate HOLLIS page
            url = f'http://id.lib.harvard.edu/alma/{hollis_num}/catalog'
            browser = webbrowser.get('safari')
            browser.open(url)
            break
    else:
        print("Your desired book isn't in HOLLIS.")


if __name__ == '__main__':
    main()