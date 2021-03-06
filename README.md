# Python package template
A package template for quickly creating a new package with test and publishing to pypi as workflow

[![Build](https://github.com/jerinka/PackageSnippet1/actions/workflows/main.yml/badge.svg)](https://github.com/jerinka/PackageSnippet1/actions/workflows/main.yml)


# Install from Pypi
```pip install PackageSnippet1```

# Local install
```git clone https://github.com/jerinka/PackageSnippet1```\
```pip3 install -e PackageSnippet1```

# build
```pip install wheel```\
```python setup.py sdist bdist_wheel```

# Coverage test
```coverage run --source=PackageSnippet1/ -m pytest -v test/ && coverage report -m```

# testpypi
```twine upload --repository testpypi dist/* ```\
```pip install -i https://test.pypi.org/simple/ PackageSnippet1 ```

# pypi
```twine upload dist/*```\
```pip install -U PackageSnippet1```

# Quick usage
```import PackageSnippet1 as pk1```\
```pk1.subpackage1.moduleA.fun_a()```

# Test
```pytest test/test_PackageSnippet1.py -s```

# Reference
[https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)









