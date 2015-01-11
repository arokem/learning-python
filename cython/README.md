# Cython :

Install cython as:

    conda install cython

Start with `add`, just to demonstrate what happens with definition of input
types.

Next is `fib`. We use `cdef` to define local variables 

Fibonacci in ('pure') python:
    
    def fib(n):
    	a, b = 1, 1
    	for i in range(n):
            a, b = a+b, a

	return a


Fibonacci in C/C++:

int fib(int n){
    int tmp, i, a, b;
    a = b = 1;
    for(i=0; i<n; i++){
    	     tmp = a;
	     a += b;
	     b = tmp;
    }	     
    return a;
}


The problem: C/C++ implementation approximately 70x faster than the python
implementation! Solution: Fibonacci in cython is as fast as the C
implementation (!)

    def fib(int n):
    	cdef int i, a, b
    	a, b = 1, 1
    	for i in range(n):
            a, b = a+b, a

	return a

This is *faster* than writing a C python extension (think mex) by hand. 

Cython is a python-like language that:

     - Improves python performance by adding type information (100 - 1000x speedups
        are common).
     - Can be used to wrap external code (C/C++/Fortran).

The `cython` CLI:
    - Generates optimized C/C++ source code from a Cython source file
    - Can then be compiled into an extension module.

 Other features:

       - Built-in support for numpy arrays
       - Integrates well with ipython


To compile the fib.pyx file, you can use the setup_fib.py:

        python setup_fib.py build_ext --inplace [--compiler=mingw32 #only for Windows!]

In ipython, you can then do:

    import fib
    a = fib.fib(10)

Note the error that comes out if you run the function with an input for which
int(foo) would fail. It fails upfront!

An even easier way to use cython is through the pyximport mechanism (see run_fib.py)

In case you are wondering where the pyx file is in this case, it is under a
conventional location: ~/.pyxbld/

We can use `cdef` to define local functions and even types, as

   cdef float distance(float *x, float *y, int n):
       cdef:  # same as using two lines each starting with `cdef`
           int i
	   float d = 0.0
	for i in range(n):
	    d += (x[i]- y[i]) **2
	return d

    cdef class Particle(object):
        cdef float psn[3], vel[3]
	cdef int id

These are unavailable from the python side, but will be available to other
functions within that pyx file/module. They have the advantage that they have
no python overhead when called, so their performance is very good. 
       
## Using `cdef` and `cpdef`

Alternatively, defining it with `cpdef` will create both the cython-available
and the python-available versions of the function. Not as simple, because the
inputs now need to be something that python knows how to produce (array
pointers are not one of those...). This gives you the advantage of 

   cpdef float distance(float[:] x, float[:] y):  # Defined as typed memory views
       cdef int i
       cdef int n = x.shape[0]
       cdef float d = 0.0
       for i in range(n):	
	    d += (x[i] - y[i]) ** 2
       return d

Finally, if you just want to define this in cython (or python, for that matter), this works:

	 def distance(x, y):
	     return np.sum((x-y) **2)

Another example:

	def increment(int num, int offset):
	    return num + offset

	def increment_sequence(seq, offset):
	    result = []
	    for val in seq:
	        res = increment(val, offset)
		result.append(res)
	    return result

And using `cdef`:

	cdef int fast_increment(int num, int offset):
	    return num + offset
	def fast_increment_sequence(seq, offset):
	    result = []
	    for val in seq:
	        res = fast_increment(val, offset)
		result.append(res)
	    return result

The second example will be much faster, because there is less python-related
overhead in that one. Cython can compile the fast_increment function without
needing to do things like python type-checking, etc.

In this case, we may as well use cpdef:

	cpdef int increment_either(int num, int offset):
	    return num + offset
	def fast_increment_sequence(seq, offset):
	    result = []
	    for val in seq:
	        res = increment_either(val, offset)
		result.append(res)
	    return result

The function increment_either is only fast when called by
fast_increment_sequence. However, you can now independently call it from
python (in which case, it will be slow).

## Using `cimport`

Look at the sinc tutorial example, and `cimport clib.math`

## Pure python mode

   import cython
   @cython.locals(n=cython.int)
   def fib(n):
       cython.declare(a=cython.int,
                               b=cython.int,
			       i=cython.int)
	a, b = 1, 1
	for i in range(n):
	    a, b = a+b, a
	return a

This can appear in a python file, and has the advantage that it can be either
compiled, or not compiled, using exactly the same code. If no compilation
occurs, this will just work at the python speed.

## Profiling with annotations

Use:

    cython -a fib.pyx

This generates your c file, but also an html file with information about the
line-by-line cost of the file. The shade of yellow corresponds the number of
lines of c that were generated, which highly correlates with the time of
execution. 


## Compling c extension from c code.

This is useful if you want to use legacy c code. Consider the toy example

     cythonize fact.pyx  
    
     gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/arokem/anaconda3/include -arch x86_64 -I/Users/arokem/anaconda3/include/python3.4m -c fact.c

     gcc -bundle -undefined dynamic_lookup -L/Users/arokem/anaconda3/lib -arch x86_64 fact.o -L/Users/arokem/anaconda3/lib -o fact.so
    

 
cythonize strlen.pyx  
    
     gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/arokem/anaconda3/include -arch x86_64 -I/Users/arokem/anaconda3/include/python3.4m -c strlen.c

     gcc -bundle -undefined dynamic_lookup -L/Users/arokem/anaconda3/lib -arch x86_64 strlen.o -L/Users/arokem/anaconda3/lib -o strlen.so
    
