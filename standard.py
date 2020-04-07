import shodan
import sys

API_KEY = "3ZWAFIxgKX9KTQWJEnf5LdcXMfvhqN5U"

if len(sys.argv) == 1:
    print('Usage: %s <search query>' % sys.argv[0])

try:
    api = shodan.Shodan(API_KEY)
    
    query = ' '.join(sys.argv[1:])
    result = api.search(query)

    for service in result['matches']:
        print('http://'+service['ip_str']+':'+str(service['port']))
        #print(  service['ip_str'] )
except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)