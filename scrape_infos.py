import requests
import json
import sys

with open('ids.json', 'r') as f:
    ids = json.load(f)['ids']

infos = []
for i in range(0, len(ids), 5):
    print(i, file=sys.stderr)
    max_i = min(len(ids), i + 5)
    r = requests.get(
        'http://api.ldjam.com/vx/node/get/{}'.format('+'.join([str(id) for id in ids[i:max_i]])))
    infos.extend(r.json()['node'])
print(json.dumps({'infos': infos}))
