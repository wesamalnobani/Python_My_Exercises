
#Json

import json
import collections

tree = lambda: collections.defaultdict(tree)
root = tree()

root ['menu']['id'] = 'file'
root ['menu']['value'] = 'File'
root ['menu']['menuitems']['new']['value'] = 'New'
root ['menu']['menuitems']['new']['oneclick'] = 'new();'
root ['menu']['menuitems']['open']['value'] = 'Open'
root ['menu']['menuitems']['open']['oneclick'] = 'open( );'
root ['menu']['menuitems']['close']['value'] = 'Close'
root ['menu']['menuitems']['close']['oneclick'] = 'close( );'

print(json.dumps(root , sort_keys = True, indent=4, separators =(',',':')))
