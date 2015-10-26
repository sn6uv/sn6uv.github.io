Pontryagin duality
##################
:date: 2015-10-26 13:40
:category: math
:author: Angus Griffith

Topological groups
------------------
A topological groups is what one might expect, a group $G$ equipped with a topology.
We ask that the topology is nice with respect to the group structure.
Namely, we require that the binary operation on the group $G \\times G \\to G$, and the inverse $G \\to G$ are continuous.

One simple group is the circle group $\\mathbb{T} = \\{z \\in \\mathbb{C} : \|z\| < 1\\}$ equipped with multiplication.
To make this a topological group this group can be equipped with the standard topology coming from $\\mathbb{C}$.
Complex multiplication and inverses are clearly continuous on $\\mathbb{T}$.
As we will soon see, this group turns out play a central role in Pontryagin duality.

The next step is to define dual groups and state the Pontryagin duality theorem but first we define locally compact (abelian) groups.

Locally compact groups
----------------------
A topological group $G$ is called locally compact if and only if there is a compact neighbourhood containing the identity.
That is, if there exists some open set $U \\ni e$ whose closure is compact in the topology of $G$.

For example, the circle group $\\mathbb{T}$ is locally compact.
Simply take $U = B\_\\epsilon(1) \\cap \\mathbb{T}$ for small $\\epsilon > 0$ such that $\\bar{U}$ is just some closed connected piece of the circle.

There are many more examples such as; $\\mathbb{R}^n$ with addition and standard topology, and any finite abelian group equipped with the discrete topology.

Dual group
----------
The dual of a group is analogous to the dual of a vector space but there are some subtle differences.

If $G$ is a locally compact abelian group then consider the set of continuous group homomorphisms $f : G \\to \\mathbb{T}$.
Such functions are called characters of the group $G$ and collectively form a locally compact abelian group, called the dual group $G^\\wedge$.

For a finite dimensional vector space $V$ over a field $\\mathbb{K}$ we usually define the dual space as $Hom(V, \\mathbb{K})$.
Likewise, for a locally compact abelian group the dual group is $Hom(G, \\mathbb{T})$.

For example, the integers with addition $(\\mathbb{Z}, +)$ is isomorphic to the dual of the circle group $(\\mathbb{T}, \\cdot)$.
Typically one proves this by showing that characters on $\\mathbb{T}$ are of the form $z \\mapsto z^n$ for some $n \\in \\mathbb{Z}$.

Pontryagin duality theorem
--------------------------
The dual of $G^\\wedge$ is canonically isomorphic to $G$.

Canonical means that there is a natural isomorphism from $\\phi: G \\to (G^\\wedge)^\\wedge$.
That is, $\\phi(x) = \\{\\chi \\mapsto \\chi(x)\\}$ for all $x \\in G$, $\\chi \\in G^\\wedge$.
