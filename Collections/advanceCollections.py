# here in this i have done a practice of advance collections
from collections import namedtuple
from math import sqrt
# like a tuple but more readable and with named fields
Point=namedtuple("Point",["x","y"])

p1 = Point(10,20)
p2 = Point(30,40)
# Access like attributes
distance=sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
print(distance)
# we can also access the values through index values
# Makes code self-documenting (p1.x instead of p1[0]).

# deque
from collections import deque
nums=[1,2,3,4,5]
window_size=3
dq=deque()
window_sum=0
# Regular list pop(0) is O(n), deque popleft() is O(1).
for num in nums:
    dq.append(num)
    window_sum+=num
    if len(dq)>window_size:
        window_sum-=dq.popleft()
    if(len(dq)==window_size):
        print(f"window: {list(dq)},Sum:{window_sum}")

#counter
from collections import Counter
# One-liner for counting instead of manual loops.
text="1 1 2 3 2 1 2 4"
numbers=text.split()
Counter=Counter(numbers)
print(Counter)
print(Counter.most_common(3))

# defaultDict
from collections import defaultdict
words=["apple","bat","cat","elephant","dog"]
grouped=defaultdict(list)

for word in words:
    grouped[len(word)].append(word)
print(dict(grouped))

# ordered_dict
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Simulate "using" 'a'
od.move_to_end('a')
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Chainmap
from collections import ChainMap

defaults={"theme":"light","language":"EN"}
env_config={"language":"FR"}
user_config={"theme":"dark"}

confiq=ChainMap(user_config,env_config,defaults)
print(confiq["theme"])
print(confiq["language"])