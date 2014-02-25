Equivalent definitions for $BMO$
################################
:date: 2014-02-25 11:15
:category: math
:author: Angus Griffith

The space of functions of bounded mean oscillation $BMO$ is defined by the BMO norm
\\begin{equation}
\\label{norm}
||f||_{BMO} = \\sup_{\\text{cubes }Q} \\frac{1}{\|Q\|} \\int_Q \|u(y) - u_Q\| dy
\\end{equation}

But an equivalent definition is to take the sup over balls instead of cubes.
Previously I wondered what other shapes gave an equivalent norm.

**Proposition:** *Suppose $D \\subset \R^n$ is a open set such that there exists $0 < r_1 < r_2 < \\infty$ such that
$$
B(0, r_1) \\subset D \\subset B(0, r_2)
$$
then the norm given by
$$
||f||_D := \\sup_{E \\in A_D}  \\frac{1}{|E|} \\int_E \|f(y) - f_E\| dy
$$
is equivalent to the BMO norm. 
The set $A_D$ is $D$ under any uniform scaling, rotations transtions  or composition thereof.*

I have not yet proven this, but I think it should be possible by adapting ideas from Stein's Harmonic Analysis.
