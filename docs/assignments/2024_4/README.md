# Λύση εργασίας 4 

## Python 

```
$ python python_plain_timer.py
input1000.txt - elapsed time 0.003833
input100000.txt - elapsed time 0.358541
input1000000.txt - elapsed time 4.434623
```


## Σε Linux ή MacOS

```
$ time python python_plain.py input100000.txt
python python_plain.py input100000.txt  0.37s user 0.02s system 92% cpu 0.424 total
$ time python python_plain.py input100000.txt
python python_plain.py input100000.txt  0.37s user 0.02s system 92% cpu 0.424 total
$ time python python_plain.py input1000000.txt
python python_plain.py input1000000.txt  4.44s user 0.10s system 97% cpu 4.631 total
```

```
$ ./time_python_plain.sh
real	0m0.045s
user	0m0.015s
sys	0m0.010s

real	0m0.370s
user	0m0.351s
sys	0m0.011s

real	0m4.609s
user	0m4.449s
sys	0m0.089s
```


