My code / solutions for [Advent of Code 2022](https://adventofcode.com/2022).



### [Day 7](https://adventofcode.com/2022/day/7)

After looking up some other solutions, there are a few notes about my initial solution:

- can use str.is_digit() rather than a regex match for the file size
- can use a list for the present working directory (pwd). `cd ..` would pop. `cd a` would append. Then use `'/'.join(list)`. In order to reverse recursively, I would need a deepcopy first I believe.
- So the method I used for change directory can be overhauled.
- It would be better to use two different cases for `cd`. One for `cd ..` and one for `cd <directory>`
- I probably don't need the initial "/" it should be assumed it is always there. So when doing the reverse recursion, it can be dealt with at the end.


```python
from copy import deepcopy
value = 8 # or whatever
pwd = ["a", "b", "c"]
temp_pwd = deepcopy(pwd)
for x in range(len(temp_pwd)):
    directory = "/".join(temp_pwd)
    filesystem[directory] += value
    temp_pwd.pop()
filesystem["/"] += value
```

I did this refactor: `day07-refactor.py`

---

Another approach I would like to try from scratch is using Objects.

- object for `file` and `directory`
- a `directory` will have a list of it's contents. It can also have it's full path.
- it would be good to maintain a $PWD that gets popped or appended to. This can be used when making a directory object.
- How do I store the whole of the file system? As a dictionary? A list of directories?
    - all directory objects could be stored in a dictionary:
        - key = full path (use from $PWD)
        - value = directory object
        - then to find out the size, `for dir in directories.values(): dir.get_size()`
        - dictionary will be better than a list because of changing directories - what about changing back to a directory I already have? This will be easy to look up with a dictionary key.

- How do implement recursion in a dynamic way? My initial implementation had a somewhat hard coded approach to recursion. If I created a `get_size()` method, then it should initiatiate that method on child directories as well.

    ```python
    # a possible approach
    def get_size():
        size = 0
        for x in self.contents:
            if x is type(directory):
                size += x.get_size()
            if x is type(file):
                size += file.size
        return size
    ```
