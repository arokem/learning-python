# Python modules and packages

As you start writing more complex code in Python, you will want to arrange your project with dependencies and tests organized in a manner

- A 'module' is a set of Python code (imports, functions, classes, etc) that together form a coherent set of ideas. These will usually be saved together in a single file and tested using the same `test_module.py` function.

- A 'package' is a set of modules organized together in a directory. To be a python package (i.e. to be importable),  the directory has to contain a `__init__.py` file. 

## Importing your modules and packages.

When `import foo` is interpreted by the python interpreter, it seeks this name in (according to this order):

- The current directory
- The 'PYTHONPATH'
- A system-set default location

You can put your files in the PYTHONPATH by editing this environment variable, or by symlinking. Another way to get your modules into the PYTHONPATH is to add a `setup.py` file to your project and use `python setup.py install` every time you change something in the code.

The most basic `setup.py` file would look something like this: 

    from distutils.core import setup
    setup(name='foo',
              py_modules=['foo'])

This takes advantage of the built-in machinery in the distutils library (a stdlib fixture), and allows you to install the code not only on your machine, but eventually also to distribute the code to others, facilitating the reproducibility of your software.

If your code contains packages, you could write a `setup.py` that looks like this:

    from distutils.core import setup
    setup(name='foo',
          packages = ['foo', 'foo.bar'],
          package_dir = {'foo':'.', 'foo.bar': './bar'},
          package_data={'foo': ['./*.py'],
                                   'foo.bar':[ './bar/*.py']})

This tells distutils about the structure of your directories, and how you would like to organize them into modules and packages. 

These setup files can do many things. We will see this return when we will want to add `cython` code to our packages.

## Adding a `main`:

A module can also become a script that you can run (through the python interpreter, or in IPython), by adding a `main` block.

When the module is imported, this block will be ignored, but when you run it in interpreter/ipython, this block will also be evaluated. It looks like this:

    if __name__ == "__main__":
        # Do something; presumably using the functions defined above


	
