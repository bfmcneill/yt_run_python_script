# Python Project Template

## setup

### 1. clone the repo

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
