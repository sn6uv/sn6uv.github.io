The space $BMO$
###############
:date: 2014-02-21 11:31
:category: math
:author: Angus Griffith

Introducing $BMO$
-----------------
The space of functions of bounded mean oscillation or $BMO$ arises when studying the space of functions whos deviation from the mean over cubes is bounded.
In ways $BMO$ is similar to $L^\\infty$, and it is often used as a replacement, however functions in $BMO$ may be unbounded.
The classic example of this is $\\log(x)$.

The space $BMO$ naturally arises in other situations too such as when studying singular integral operators,
\\begin{equation}
f(x) \\mapsto \\int k(x,y) f(y)\\, dy.
\\end{equation}
These operators map $L^\\infty$ to $BMO$.

For a complex-valued locally integrable function on $\\mathbb{R}^n$ we define
$$
||f||_{BMO} = \\sup_Q \\frac{1}{\|Q\|} \\int_Q \|f(x) - \\text{Avg}_Q f\| dx,
$$
where the supremium is taken over all cubes $Q \\subset \\mathbb{R}^n$.
This defines a norm when we take an equivalance class of functions that differ a.e. by a constant.
We denote $BMO = \\Big\\lbrace f : \\mathbb{R}^n \\to \\mathbb{C} \\Big| ||f||_{BMO} < \\infty \\Big\\rbrace$.
In fact, $BMO$ is a Banach space that contains $L^\\infty$.

Our definition for $BMO$ used cubes, but the definition using balls instead is equivalent.
**Question:** What other shapes could we use? How about $L^p$ balls for $1 \\le p \\le \\infty$?
