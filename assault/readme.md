assault example
===============

based on:    
Cloud Guru: Programming Use Cases with Python   
https://github.com/kennethreitz/setup.py   


creating environment:
---------------------
```
> pip3.10 install --user pipenv
> pipenv install --python python3.10
> pipenv install twine --dev
> pipenv install pylint --dev
> pipenv install black --dev
```

create ./.vscode/settings.json:
```
{
    "python.defaultInterpreterPath": "~/.local/share/virtualenvs/assault-_0JwWndx/bin/python",
    "python.linting.enabled": true,
    "editor.formatOnSave": true,
}
```


development (CLI)
-----------

```
pipenv install click
```

add click to setup.py. 'required' list


testing
-------
```
python assault/cli.py --help
python assault/cli.py -r 1 -c 2 -j 3 abc
```


development (Async)
-----------
 pipenv install requests  

 Note: 'requests' is not asyncio compatible


 development (Typecheck)
 ---
 install pyright

test
---
 python -m doctest assault/stats.py 


 local install
 ---
 pip install -e .  


sudo docker run -p 8080:80 -d nginxdemos/hello
DEBUG=true assault -c 10 -r 30 http://host.docker.internal:8080

DEBUG=true assault -c 1 -r 2 -j out.json https://google.com