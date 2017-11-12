import json
import numpy as np
print(np.arange(15))
obj = {
  'one': 1,
  'two': 2,
  'three': [1, 2, 3]
}
# json 转为 str
encoded = json.dumps(obj)
print(type(encoded))
print(encoded)
# str再转为json
decoded = json.loads(encoded)
print(type(decoded))
print(decoded)
