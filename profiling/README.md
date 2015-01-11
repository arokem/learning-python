
# Profiling python code

 After you have tested it, and are sure that it does what you intended, the
 next step is often to get it to do that quickly and efficiently. Profiling is
 a way to assess the performance of your code, on a function-by-function, or
 even line-by-line basis. We will look at an assessment of the speed of
 performing different parts of your code and the assessment of memory
 consumption of different parts of your code. 

 ## Line-by-line timing

 The line profiler can be installed: 

    pip install line_profiler


## Line-by-line memory consumption

Memory profiler can be installed with:

    pip install memory_profiler

Please also install psutil, which makes memory_profiler work faster:

    pip install psutil
    

http://nbviewer.ipython.org/gist/arokem/f91d436af3f0d3084af4
