GMPY_CFFI mpz speed
###################
:date: 2014-01-01 17:08
:category: programming
:author: Angus Griffith

gmpy_cffi is slow
-----------------
Today I released version 0.1 of `gmpy_cffi`_, a PyPy compatible implementation of `gmpy`_.
The problem is that my implementation is quite a bit slower.

.. image:: /images/gmpy_mpz.png
   :width: 100 %
   :alt: gmpy_mpz.png

As you can see, the time taken to initialize an mpz instance is about 10x slower under gmpy_cffi when compared to gmpy.

Explanation
-----------
The gmpy mpz initialisation code uses the CPython internals to access the raw bits storing the value of a python integer (or long).
In comparison, gmpy_cffi converts the number to a hex string and then uses `mpz_set_str` with base 16 to set the GMP mpz value

.. code-block:: python

    def _pyint_to_mpz(n, a):
        """
        Set `a` from `n`.
        :type n: int,long
        :type a: mpz_t
        """
        if -sys.maxsize - 1 <= n <= sys.maxsize:
            gmp.mpz_set_si(a, n)
        elif sys.maxsize < n <= MAX_UI:
            gmp.mpz_set_ui(a, n)
        else:
            gmp.mpz_set_str(a, hex(n).rstrip('L').encode('UTF-8'), 0)

I've tried other methods such as using bit twiddling to break the python int into an array of C ints and then using mpz_import, but it was slower than using hex

.. code-block:: python

    def _pyint_to_mpz(n, a):
        """
        Set `a` from `n`.
        :type n: int,long
        :type a: mpz_t
        """
        neg = n < 0
        n = abs(n)
        tmp = array.array('L')
        size = tmp.itemsize
        numb = (8 * size)
        mask = ~(~0 << numb)
        while n:
            v = n & mask
            n = n >> numb
            tmp.append(v)
        addr, count = tmp.buffer_info()
        gmp.mpz_import(a, count, -1, size, 0, 0, ffi.cast('void *', addr))
        if neg:
            gmp.mpz_neg(a, a)

Conclusion
----------
The conversion from python long to gmp mpz is by far the main reason why initializing mpzs in gmpy_cffi is so slow, but there isn't really an obvious way to improve on this.

Perhaps cffi could provide a fast method for converting python longs to an array of C ints, but I doubt there's a huge demand for that right now.

We're within a factor of 10 of evil low level C hackery. For now that will have to do.

.. _`gmpy_cffi` : https://github.com/sn6uv/gmpy_cffi
.. _`gmpy` : https://github.com/sn6uv/gmpy_cffi
