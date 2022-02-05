# Python package template
package template for quick start

# Install from Pypi
```pip install PackageSnippet1```

# Local install
```git clone https://github.com/jerinka/PackageSnippet1```\
```pip3 install -e PackageSnippet1```

# build
```python setup.py sdist bdist_wheel```

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
```cd PackageSnippet1/test```\
```pytest test.py -s```

# Reference
[https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)









