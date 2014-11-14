## Python learning materials


### Installing Python/Anaconda

We will use Python 3, installed with Anaconda. To get that on your laptop:

- Download this file: http://repo.continuum.io/anaconda3/Anaconda3-2.1.0-MacOSX-x86_64.sh
   You want the `.sh`, *not* the `.pkg` file. Believe me.
   
- In the shell, switch your working directory to the one containing this file
  (typically `~/Downloads`) and run:

        sh Anaconda3-2.1.0-MacOSX-x86_64.sh

You will be asked to press `ENTER` to continue, which will drop you into a
buffer containing the license. Type `q` to exit that buffer, and then enter
`yes` to continue. The proposed installation location that should then appear
should be something like: `/Users/arokem/anaconda3`. Accept that, and wait for
the installation to complete.

Anaconda should give you the basic tools for scientific computing, including
`ipython`/`numpy`/`scipy`/`matplotlib` and many more. 

### In preparation

- Clone this repo

- Fire up the ipython notebook in the top-level directory of this repo, by
  typing at the shell:

      ipython notebook

  This should open up a browser with a notebook.
      
- Watch the python programming videos on this page
  https://talks.stanford.edu/tutorials/programming-tutorials/
  Feel free to skip and start from the third video, which shows how to open the
  IPython notebook. Follow along in the notebook that is in the `whirlwind`
  directory of this repo. We'll go over that first next time we meet. 

### Topics:

- A whirlwind tour through basic python: we'll review the notebook
  from the video tutorial, and address your questions.

- Testing with [`nosetests`](https://nose.readthedocs.org/en/latest/)

- Modules and packages.

- Object oriented programming in Python.

- Scientific Python: [].

- Useful additional libraries.


