# Super Simple Tutorial

#### First: Where to get help if you need help

Even simple things can take time and perspective to understand, the pants community is here to help you!

[Meet us on our friendly slack channel!]()


### Setup

Let's build a project to say hello to the world!

:::{tip}
Note: It is best practice to use a virtual environment.  If you want to setup a virtual environment, but don't know how - I find [this tutorial useful](https://realpython.com/lessons/creating-virtual-environment/).
:::

Start by making a project directory and adding the `helloworld.py` file into that directory. Your project should look like this.


```
myproject
│   helloworld.py

```

The code of a helloworld program is below.

```python
def main():
	print("hello world")

if __name__ == '__main__':
	main()
```

You should be able to run this program from the command line with the command below.

```shell
python helloworld.py
```

Hopefully... you are seeing `hello world`! 

:::{tip}
Note: If you are not, please reach out to the [slack channel](https://join.slack.com/t/pantsbuild/shared_invite/zt-d0uh0mok-RLvVosDiX6JDpvStH~bFBA), we would love to help!
:::

### Creating a python package

Next, let's turn the helloworld module into a python package. We will use setuptools to create a wheel - `.whl` - and tar - `.tar.gz` - which can be installed into a virtual environment by pip.

Add a `setup.py` file into the project directory.

```
mypexproject
│   helloworld.py
│   setup.py

```

The file - `setup.py` - should contain the text below.


```python
from setuptools import setup

setup(
    name='helloworld',   # this is the name of the .whl or .tar.gz file
    version='0.0.1',
    py_modules=['helloworld'],  # this is the location of the helloworld.py module
    install_requires=[
        'importlib-metadata; python_version >= "3.7"', # sets the version of python
    ],
    entry_points = {
    # the console_script is in the form `command_line_arg=python_function_called` 
    # and is used to set the command argument to invoke the python program
        'console_scripts': ['helloworld=helloworld:main'],  
    }
)
```

Python has a package called `build` which can run this `setup.py` file and generate distributions in the `dist` folder.  But first, be sure to have `build` installed.

```shell
pip3 install build
```

Next you can run this command to build your package.

```shell
python3 -m build 
```

Now your project structure should look like this.

```
mypexproject
│   helloworld.py
│   setup.py  
│
└───dist
│   │   helloworld-0.0.1-py3-none-any.whl
│   │   helloworld-0.0.1-py3-none-any.tar.gz

```

Great work! On to the next part, creating the python executable file.

### Creating a python executable - `.pex`

Just like you need the `build` package to build a python package, you need the `pex` project to build a python executable - `.pex` .

Start by installing the pex package using the command below.

```shell
pip3 install pex
```

More information about pex is available in the [documentation](https://pex.readthedocs.io/en/v2.1.84/index.html)

Once pex is installed, all you need to do to create a .pex file is to run the command below

```shell
pex . -c helloworld --output=helloworld.pex
```
Pex looks for the `setup.py` in the directory and creates the output file `helloworld.pex`.

Finally your project structure should look like this.

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


First, make sure it worked by running `helloworld.pex` using this command.

```shell
./helloworld.pex
```

Now you can run `helloworld.pex`. The only file you need to give to another person to run your `helloworld` program is the `helloworld.pex`. The magic of an executable file is that it can easily be shared!

You can run it, but can your friend run `helloworld.pex`?
Send it to your friend and let them try to run it today!




