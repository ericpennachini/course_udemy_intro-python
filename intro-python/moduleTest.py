from camelcase import CamelCase
import colorama

c = CamelCase()

s = 'this sentences needs CamelCase'

r = c.hump(s)

print(r)

