import requests
import json

def main():
    print('Searching HOLLIS for "The Cat in the Hat"')

    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'http'
    hostname = 'webservices.lib.harvard.edu'
    path = '/rest/v2/hollisplus/search/dc/'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'q': 'The Cat in the Hat',
             'limit': 2
    }

    # Add a field to the request header saying what we accept
    accept = {'Accept': 'application/json'}

    response = requests.get(url, params=query, headers=accept)

    # Read the response body in JSON format and print it
    j = response.json()
    print("response.json() =", json.dumps(j, indent=4))

    print('')

    # Print the title from each returned response
    for i, item in enumerate(j['results']['resultSet']['item']):
        print(f"Title #{i}: {item['dc:title']}")

if __name__ == '__main__':
    main()