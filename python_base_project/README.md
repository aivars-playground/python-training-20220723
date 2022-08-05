* Prepare dev environment
```bash
python3.10 -m pip install --upgrade pip setuptools wheel pipenv
pipenv --python python3.10
```

* Configure vscode
```bash
pipenv --py
pipenv install pylint black --dev
```
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
├── setup.py
├── src/
│   └── python_base/
│       ├── __init__.py
│       └── main_module.py
└── tests/
```

Install a local setup.py into your virtual environment/Pipfile:
```
pipenv install -e .

python_base NAME
```
