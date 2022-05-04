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
:::{tip}
Note: If you have questions about this test, please read the [pytest documentation.](https://docs.pytest.org/en/6.2.x/capture.html#accessing-captured-output-from-a-test-function)
:::

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
:::{tip}
Note: Pants has very useful help commands built in. You can access them with the basic `help` or `--help` flags.

```shell
./pants help
```
:::

### Using `pants` to build your `.pex`

#### Tailoring the pants

In order to create your `.pex` file, `pants` needs more information about your local environment and directory structure.  This "tailoring" of the build is done using the `tailor` command below.

```shell
./pants tailor
```

The information `pants` needs is stored in the new file `BUILD`. Your file should look approximately like this.

##### BUILD
```python
pex_binary(
    name="helloworld0",
    entry_point="helloworld.py",
)

python_sources(
    name="root",
)

python_tests(
    name="tests0",
)
```

Check that your project structure now looks like this!

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


### Using `pants` to run your tests on your `.pex`

Here we can show you multiple ways of using `pants` to run your tests.

The first is the most straightforward.

```shell
./pants test test_helloworld.py
```

This runs pytest on the file `test_helloworld.py`.  But what if you had more than one test file?

Then you could use the command below.

```shell
./pants test ::
```

The double colons indicate a directory structure. Plain `::` indicates the current directory.  If you put all the tests into a folder called `tests` then the command would be `./pants test tests::`. For pants, just replace slashes with `::`.



Finally, let's look at that build file again.

```python
...
python_tests(
    name="tests0",
)
```


The build file has a command `python_tests`.  This command has a `name` keyword that is assigned to the value `test0`.  This name can be used by pants to call the tests.

```shell script
./pants test :tests0
```
###  Using `pants` to generate your `.pex`

Now that you understand the `pants` syntax a little better, you can use it to generate the `.pex` file.

```shell script
./pants package ::
```

If the command ran properly, the console should look like this.

```shell
>>> ./pants package ::
20:42:00.28 [INFO] Completed: Building helloworld0.pex
20:42:00.28 [INFO] Wrote dist/helloworld0.pex
```
The `.pex` will be in your `dist` file alongside the `.whl` and `tar.gz` files.

Check that the directory now looks like this.

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
│   │   helloworld0.pex

```

And that the new `.pex` file can be run like this.

```shell
>>> ./dist/helloworld0.pex
hello world
```
