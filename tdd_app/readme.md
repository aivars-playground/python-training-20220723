starting development
---
```bash
make install
```

testing
---
```bash
make test
```

if app is installed
---
```bash
$ python -m tddapp
> HELLO
```

manual test
```py
from tddapp import tree
tree.read(".")
f = open(".ignoreme/out.txt", "wb")
f.write(proc.stdout.read())
f.close()
```