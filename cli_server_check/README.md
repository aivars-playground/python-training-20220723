* Prepare dev environment
```bash
python3.10 -m pip install --upgrade pip pdm
pdm install
```

* Configure vscode
```json
// <project_root>/.vscode/settings.json
{
    "python.defaultInterpreterPath": "~/.local/share/virtualenvs/<ENV_NAME>/bin/python",
    "python.linting.enabled": true,
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
}
```

* project structure
https://packaging.python.org/en/latest/tutorials/packaging-projects/
```
project/
├── README.md
├── python.toml
├── src/
│   └── python_base/
│       ├── __init__.py
│       └── __main__.py
│       └── a_module.py
│       └── b_module.py
└── tests/
```

Install a local folder:
```
> pdm install --dev 

> cli_server_check
```
=cli_server_check is package and script name, script name could be different=


```json
// ./.ignoreme/in.json
[
    "https://google.com:80",
    "https://yahoo.com:80"
]
```
cli_server_check -f .ignoreme/in.json -s "https://bing.com:80"

```


test in ipython
```python
from cli_server_check.http import ping_servers
servers = {"https://google.com", "https://google.c"}
ping_servers(servers)
```


call as script  (see __main__.py)
```
python -m cli_server_check              //(calling __main__.py)
python -m cli_server_check.http         //(calling http.py)
```


