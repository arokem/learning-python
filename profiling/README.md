
# Profiling python code

 After you have tested it, and are sure that it does what you intended, the
 next step is often to get it to do that quickly and efficiently. Profiling is
 a way to assess the performance of your code, on a function-by-function, or
 even line-by-line basis. You might want to assess different aspects of code
 performance, and the two major ones are how long it takes for your code to run
 and (not unrelated) how much memory the code uses.

 We will look at an assessment of the speed of performing different parts of
 your code and the assessment of memory consumption of different parts of your code. 

 ## Line-by-line timing

We will use the python
[`line_profiler`](https://github.com/rkern/line_profiler) library for this. It
can be installed from the command line using: 

    pip install line_profiler

Fire up the notebook `001-line-profiler` to see how to use it in the context of
an ipython session. 

## Line-by-line memory consumption

Memory profiler can be installed with:

    pip install memory_profiler

Please also install psutil, which makes memory_profiler work faster:

    pip install psutil

Head over to the notebook `002-mem-profiler` to see how it's done. 
    
