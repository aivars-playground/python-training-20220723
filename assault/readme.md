assault example
===============

based on:    
Cloud Guru: Programming Use Cases with Python   
https://github.com/kennethreitz/setup.py   


creating environment:
---------------------
```
> pip3.10 install --user pipenv
> pipenv install --python python3.10 twine --dev
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


development
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
