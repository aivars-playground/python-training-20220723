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

manual test:  call tree
```py
from tddapp import tree
tree.read(".")
f = open(".ignoreme/out.txt", "wb")
f.write(proc.stdout.read())
f.close()
```

manual test:  copy file
```py
infile = open(".ignoreme/out.txt", "rb")
copy = open(".ignoreme/copy.txt", "wb")
from tddapp import writer
writer.local(infile,copy)
```


AWS
---
install awscli outside of virtualenv
```
aws s3api create-bucket --bucket  `echo my-tb-$EPOCHSECONDS`
```