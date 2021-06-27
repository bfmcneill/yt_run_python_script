# Python Project Template

## setup

### 1. clone the repo

- clone this >> [yt_run_python_script](https://github.com/bfmcneill/yt_run_python_script)

### 2. install a virtual environment

```powershell
python -m venv .venv
```

### 3. activate virutal environment (windows)

```powershell
.venv\scripts\activate
```

### 4. upgrade virtual environment

```powershell
python -m pip install -- upgrade pip pip-tools
```

### 5. install setup.py file

```powershell
pip install -e .
```

## usage

The entry point to the cli will only work if you have gone through the setup steps.

### trigger the entrypoint (must have virtual environment activated)

```powershell
pycmd
```

## References

- [Explain Python entry points?](https://stackoverflow.com/questions/774824/explain-python-entry-points)
- [setup.py: renaming src package to project name](https://stackoverflow.com/a/14421176)
- [Setup.py ReadTheDocs.io](https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html)
- [Click](https://click.palletsprojects.com/en/latest/)
