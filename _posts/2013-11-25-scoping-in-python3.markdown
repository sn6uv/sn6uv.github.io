# Introduction
Recently I was working on porting my Python2 library
[gmpy_cffi](https://github.com/sn6uv/gmpy_cffi) to work under Python3 as well.
I'm using [py.test](http://pytest.org) to organise and run my tests.
Each test module is in it's own class, and so we have code that looks something like this

{% highlight python %}
import sys
import pytest
from gmpy_cffi import mpq


class TestMPQ(object):
    ints = [1, 2, -123, 456, sys.maxsize, -sys.maxsize - 1, 2*sys.maxsize]
    pairs = [(i, j) for i in ints for j in ints]

    @pytest.mark.parametrize(('n', 'd'), pairs)
    def test_int(self, n, d):
        int(mpq(n, d)) == n // d
    import pytest
    import sys
{% endhighlight %}

Under Python2 this code behaves like you might expect, but under Python 3 we get
the following traceback

    Traceback (most recent call last):
      File "tests/test_example.py", line 6, in <module>
        class TestMPQ(object):
      File "tests/test_example.py", line 8, in TestMPQ
        pairs = [(i, j) for i in ints for j in ints]
      File "tests/test_example.py", line 8, in <listcomp>
        pairs = [(i, j) for i in ints for j in ints]
    NameError: global name 'ints' is not defined

But I defined ints just there! Even more strange, I made this minimal example:

{% highlight python %}
class A(object):
    integers = [1, 2, 3]
    singles = [i for i in integers]


class B(object):
    integers = [1, 2, 3]
    pairs = [(i, j) for i in integers for j in integers]
{% endhighlight %}

Under Python2  this works fine, but under Python3 you get the same traceback as above but only for class B and not for class A.
I looked up the Python3 documentation, 
[what's new in Python 3.0](http://docs.python.org/3.0/whatsnew/3.0.html),
but all I found was

> list comprehensions have different semantics: they are closer to syntactic
> sugar for a generator expression inside a list() constructor, and in
> particular the loop control variables are no longer leaked into the surrounding
> scope.

In Python 3 the iteration variables (`i` and `j` in the example) no longer leak out of the list comprehenion.

{% highlight python %}
class C(object):
    ints = [i for i in range(10)]
{% endhighlight %}

Under Python 2 we can access the iteration variable as a class variable

    >>> C().i
    9

but under Python 3:

    >>> C().i
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'C' object has no attribute 'i'

This isn't quite the same issue as we're trying to solve, but's it is related.
I asked on [stack overflow](http://stackoverflow.com/q/20136955/606640) if
someone could explain my example.
The first comments I recieved were "Are you sure?", and that I should submit a bug against the implementation.
I recieved an answer not soon after.
The [answer](http://stackoverflow.com/a/20137069/606640) by user Blckknght is
excellent and worth a read, but to summarise:

- List comprehensions were changed to prevent this leaking of iteration variables into the surrounding scope.
- They are now implemented with a function that is called to produce the lists.

Just as class methods can't access class variables directly (you have to access them through `self`),
these list comprehension functions also can't access the class variables.
If the list comprehension isn't nested (as in class A), then it's okay because the list comprehension function is called with the class variable `ints` as an argument.
When we nest list comprehensions however the body of the outer list comprehension, within which the inner list comprehension is called, doesn't know about the class variable `ints` and hence our NameError.

The answer by Blckknght goes on in detail disasembling the python bytecode to show how exactly how this happens and is well worth a read.
The change to prevent leaking scope make sense, and I think it's a good idea.
You just have to remember that in Python 3 list comprehensions are functions, and in both Python 2 and 3 class scopes can be a little bit strange.
