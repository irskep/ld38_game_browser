import requests
import json
import sys

ids = [];
for i in range(0, 2951, 25):
    print(i, file=sys.stderr)
    r = requests.get(
        'http://api.ldjam.com/vx/node/feed/9405/parent/item/game?limit=25&offset={}'.format(i))
    ids.extend([row['id'] for row in r.json()['feed']])
print(json.dumps({'ids': ids}))
