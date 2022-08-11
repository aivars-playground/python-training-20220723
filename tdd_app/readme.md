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

manual test:  copy to s3
```py
from tddapp import writer
import boto3

client = boto3.client('s3')
infile = open(".ignoreme/out.txt", "rb")
writer.s3(client, infile, "my-tb-1660200353", "export.txt")
```
```bash
aws s3api list-objects --bucket my-tb-1660200353
```

final test
```bash
python -m tddapp.cli . --target s3://my-tb-1660200353/export.txt
python -m tddapp.cli . --target file://.ignoreme/export.txt
python -m tddapp.cli .
```