# Adding `pants` to the super simple tutorial


## Starting place

At the end of the last tutorial, you created a `.pex` file for your helloworld project. 

Your project should now look like this.


```
mypexproject
│   helloworld.py
│   setup.py  
│   helloworld.pex 
│
└───dist
│   │   helloworld-0.0.1-py3-none-any.whl
│   │   helloworld-0.0.1-py3-none-any.tar.gz

```

## What is `pants`? Why add `pants`?

Pants is a suite of tools for creating and evaluating your new executable files.

If the `pex` package is a knife, then `pants` is the kitchen.

Imagine someone sent you only a `.pex` file. You would want to know, is the python code formatted properly? Are there tests? Do the tests pass? Will this executable do the thing that you want it to do?  Pants lets you run linters like black, run testers like pytest, and many more things.

### Let's add a test to `helloworld`

It's not that complicated, but we still want to know if our `helloworld` project actually works. First, let's install pytest.

```shell
pip3 install pytest

```

Now we can add a test file - `test_helloworld.py` - which contains our test.

##### test_helloworld.py
```python
from helloworld import main
def test_main(capsys):
	main()
	captured = capsys.readouterr()
    assert "hello world" in captured.out

```

Note: If you have questions about this test, please read the [pytest documentation.](https://docs.pytest.org/en/6.2.x/capture.html#accessing-captured-output-from-a-test-function)


Finally, we can run our test using pytest.

```shell
pytest .
```


Your project should now look like this.


```
mypexproject
│   helloworld.py
│   test_helloworld.py
│   setup.py  
│   helloworld.pex 
│
└───dist
│   │   helloworld-0.0.1-py3-none-any.whl
│   │   helloworld-0.0.1-py3-none-any.tar.gz

```



## Adding `pants` 

### Setup installing `pants` by adding `.gitignore` and `pants.toml`

Because `pants` is a program and not a python package, the installation requires a curl command. From `mypexproject` add two files - `.gitignore` and `pants.toml`

##### .gitignore
```text
# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).


# Python files
__pycache__/
*.pyc
.venv/
venv/

# Editors
.idea/
*.iml

# Pants workspace files
/.pants.d/
/dist/
/.pids
/.pants.workdir.file_lock*
/.pants.rc
```
##### pants.toml
```text
[GLOBAL]
pants_version = "2.10.0"
backend_packages = [
"pants.backend.python",
"pants.backend.python.lint.black",
]

```


Your project should now look like this.

```
mypexproject
│   .gitignore
│   helloworld.py
│   test_helloworld.py
│   setup.py  
│   helloworld.pex 
│   pants.toml
│
└───dist
│   │   helloworld-0.0.1-py3-none-any.whl
│   │   helloworld-0.0.1-py3-none-any.tar.gz

```

### Install `pants`

Then you can run this command to install `pants`.

```shell
curl -L -O https://static.pantsbuild.org/setup/pants && chmod +x ./pants
```

Check that your project now looks like this!

```
mypexproject
│   .gitignore
│   helloworld.py
│   test_helloworld.py
│   setup.py  
│   helloworld.pex 
│   pants.toml
│   pants
│
└───dist
│   │   helloworld-0.0.1-py3-none-any.whl
│   │   helloworld-0.0.1-py3-none-any.tar.gz

```

### Using `pants` to build your `.pex`

#### Tailoring the pants

In order to create your `.pex` file, `pants` needs more information about your local environment and directory structure.  This "tailoring" of the build is done using the `tailor` command below.

```shell
./pants tailor
```

The information `pants` needs is stored in the new file `BUILD`.

Check that your project now looks like this!

```
mypexproject
│   .gitignore
│   BUILD
│   helloworld.py
│   test_helloworld.py
│   setup.py  
│   helloworld.pex 
│   pants.toml
│   pants
│
└───dist
│   │   helloworld-0.0.1-py3-none-any.whl
│   │   helloworld-0.0.1-py3-none-any.tar.gz

```


### Using `pants` to run you tests on your `.pex`


```shell
./pants test helloword::
```
