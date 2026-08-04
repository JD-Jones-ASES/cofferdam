# **Cofferdam audit and next theorem candidate**

## **Ryser (r=6), repository state of August 3, 2026**

## **Verdict**

**I agree with the repository’s current mathematical headline through certificate 0023\.** I found no major load-bearing error in the claim that every critical core has

\[  
22\\le m\\le456,\\qquad X\\ge8,  
\]

with the current minimum-excess frontier (X=8) confined to (22\\le m\\le28). That is the state presently advertised by the README and PLAN.

I found **four minor certificate/prose defects**, none of which changes certificate 0023’s conclusion.

More importantly, I found a substantially stronger route:

> ## **Proposed theorem (T)-A24**

> Every critical (6)-partite intersecting (6)-uniform core with (\\tau=6) satisfies  
> \[  
> \\boxed{X\\ge10.}  
> \]

There is also a new staircase:

> ## **Proposed theorem (T)-B24**

> If (X=10), then  
> \[  
> \\boxed{m\\le25.}  
> \]  
> Equivalently,  
> \[  
> \\boxed{m\\ge26\\Longrightarrow X\\ge11.}  
> \]

Thus the proposed new minimum-excess frontier is

\[  
\\boxed{X=10,\\qquad 22\\le m\\le25.}  
\]

This is **not yet Cofferdam-certified**. It should enter the normal derive (\\to) refute (\\to) independently reimplement (\\to) mutate (\\to) certify process. It does not prove Ryser (r=6), nor does it construct a counterexample. A 2025 paper still describes Ryser’s conjecture as open for every (r\\ge4), so no published Holy Grail resolution surfaced in my literature check. ([arXiv](https://arxiv.org/abs/2505.05339))

---

# **1\. Audit of certificate 0023**

## **1.1 The main proof appears sound**

The difficult point is the zero-slack ((X,m)=(7,24)) triangle. I agree with the substantive argument.

At equality, the optimizer uniquely forces the high-degree multiset

\[  
(10,9,6)  
\]

and the census

\[  
(n,n\_2,n\_3,n\_4,n\_5)=(36,12,5,0,16).  
\]

Consequently every edge contains exactly one degree-(2) vertex. The certificate’s high-incidence pigeonhole then gives a complete contradiction:

* An edge with no high vertex has degree sum at most  
  \[  
  2+5\\cdot5=27\<29=m+5.  
  \]  
  Hence every edge contains a high vertex.  
* The three triangle edges consume (3\\cdot3=9) of the (10+9+6=25) high incidences.  
* Every other edge meets the high triple in at most one vertex, leaving only  
  \[  
  25-9=16  
  \]  
  high incidences for (24-3=21) edges.

Thus (16\<21), contradiction. This is a complete proof of that cell, independent of the profile-ledger engine. The source itself identifies this as the primary gate.

I also agree with the residual-pairing lemma ((RG)). If (k) vertices are removed from a (\\tau=6) core, the residual edge family has cover number at least (6-k). Pairing residual edges gives a cover with at most (\\lceil r/2\\rceil) vertices, so (r) residual edges require

\[  
\\left\\lceil\\frac r2\\right\\rceil\\ge6-k,  
\]

hence

\[  
r\\ge2(6-k)-1.  
\]

That is exactly the bound consumed by the certificate.

The incidence ledgers are also used safely. They are relaxations: **infeasibility** proves nonexistence, while feasibility proves nothing. Certificate 0023 explicitly records the two feasible (m=22) double-triple returns and closes them with ((RG)) instead. That is the correct logical direction.

## **1.2 The K4 and double-triple inventories**

I found no missing major posture in the current source.

For the ((1^7)) K4 branch, the seventh pair’s two edges are correctly split according to whether the seventh shared set meets the K4 core in one high vertex or lies on low vertices. The exclusion of two support edges is structural: two K4 supports already share the two-cell core, and adding another shared set would make the seventh pair have (q\\ge2).

For the ((10,8,8)) double-triple case, the two postures are correctly indexed by whether there is an (abc)-edge. The resulting counts of 18 or 19 edges meeting the high triple, followed by the residual-pairing requirement, correctly kill (m=22).

So my audit conclusion is:

> **No major mathematical repair to 0023 is presently required.**

The new argument below nevertheless makes most of 0023 non-load-bearing: it independently removes the entire (X=7) layer without parity, ledgers, or ((RG)).

---

# **2\. Minor corrections to certificate 0023**

## **2.1 Mutation count: “Twelve” should be “Nine”**

The proof header says:

> “(7) MUTATIONS. Twelve, priced.”

But the mutation ledger actually asserts

len(MUT) \== 9

and contains nine priced mutations.

**Fix:** change “Twelve, priced” to “Nine, priced.”

This is purely bookkeeping.

## **2.2 The ((7,24)) cell does not fall by “three independent proofs”**

The strongest accurate description is:

1. **One complete pigeonhole proof**, namely `CK_PIG`.  
2. **One separate apex-plus-parity proof chain**:  
   * apex arithmetic first excludes a seventh-pair edge riding a triangle edge;  
   * parity then kills the resulting plain edges.

The apex arithmetic alone is not a complete proof of the cell, and the parity proof consumes the apex conclusion. The degree-(10) and degree-(6) parity contradictions are two manifestations of the same invariant, not independent full proofs.

**Suggested replacement:**

> “The ((7,24)) tie has one complete high-incidence pigeonhole proof and a separate apex-arithmetic-plus-parity proof.”

This affects README, PLAN, the commit prose, and the certificate narrative, but not the theorem.

## **2.3 Mutation `M-P2` contradicts `CK_PIG`**

`M-P2` says that after withdrawing parity, “no alternative gate stands behind it.” But the certificate has already proved the complete `CK_PIG` contradiction.

**Fix the mutation description to:**

> “With parity withdrawn, the apex-plus-parity proof branch disappears; the independent high-incidence pigeonhole proof still kills the theorem cell.”

Again, theorem unaffected.

## **2.4 A vacuous `or True`**

The ((2,2,1,1,1)) quotient check contains a conjunct of the form

all(... or True for ...)

which is identically true.

A later conjunct enforces the intended (H\_{1010}) property, so the proof does not presently depend on the vacuous line. Nevertheless, this is precisely the kind of construct that can conceal a future false green.

My independent reconstruction gives

\[  
|H\_{1010}|=1,  
\]

with the unique pattern

\[  
(7,7,2,2),\\qquad \\mu\_{01}=3.  
\]

The checker should explicitly assert

len(H\_1010) \== 1

and delete the `or True` conjunct.

---

# **3\. The new lemma: global part-collision**

The banked pointwise ((PC)) inequality has a stronger global form.

Let the six parts be (V\_1,\\dots,V\_6), with

\[  
n\_i=|V\_i|.  
\]

For integers (a,b), write (a=qb+r), (0\\le r\<b), and define the balanced collision number

# **\[**

# **\\Phi(a,b)**

r\\binom{q+1}{2}+(b-r)\\binom q2.  
\]

For (u\\in V\_i), define

\[  
g(u):=\\sum\_{j\\ne i}\\Phi(d(u),n\_j).  
\]

Recall that an excessive edge pair ({e,f}) has

\[  
q(e,f)=|e\\cap f|-1\>0,  
\]

and

\[  
X=\\sum\_{{e,f}}q(e,f),  
\\qquad  
R=\\sum\_{{e,f}}q(e,f)\\bigl(q(e,f)+1\\bigr).  
\]

Also let

\[  
s(u)=\\sum\_{{e,f}:u\\in e\\cap f}q(e,f).  
\]

## **Lemma: global part-collision**

For every vertex (u),

\[  
\\boxed{g(u)\\le s(u)\\le X,}  
\]

and globally,

\[  
\\boxed{\\sum\_u g(u)\\le R.}  
\\tag{GPC}  
\]

## **Proof**

Fix (u\\in V\_i), and consider the (d(u)) edges containing (u). For another part (V\_j), let (a\_x) be the number of those edges using (x\\in V\_j). Then

\[  
\\sum\_{x\\in V\_j}\\binom{a\_x}{2}  
\]

counts pairs of star edges that agree in part (j). By convexity,

\[  
\\sum\_{x\\in V\_j}\\binom{a\_x}{2}  
\\ge \\Phi(d(u),n\_j).  
\]

Now sum over (j\\ne i). A pair (e,f) through (u) is counted once for every additional part in which it agrees. That number is exactly

\[  
|e\\cap f|-1=q(e,f).  
\]

Therefore

\[  
g(u)  
\\le  
\\sum\_{{e,f}\\subseteq E(u)}q(e,f)  
\=s(u).  
\]

Clearly (s(u)\\le X).

Finally,

# **\[**

# **\\sum\_us(u)**

# **\\sum\_{{e,f}}q(e,f),|e\\cap f|**

\\sum\_{{e,f}}q(e,f)\\bigl(q(e,f)+1\\bigr)  
\=R.  
\]

Hence

\[  
\\sum\_ug(u)\\le R.  
\]

(\\square)

This global inequality is the main new instrument. Pointwise ((PC)) caps individual degrees; ((GPC)) limits how many vertices can simultaneously approach those caps.

---

# **4\. Exact degree-and-part sweep**

I used the following necessary conditions only.

For a proposed excess partition

\[  
\\pi=(q\_1,\\dots,q\_t),\\qquad q\_1\\ge\\cdots\\ge q\_t,  
\]

distinct (6)-edges imply (q\_i\\le4). Define

\[  
R(\\pi)=\\sum\_iq\_i(q\_i+1).  
\]

For every sorted six-part size vector

\[  
6\\le n\_i\\le\\left\\lfloor\\frac m2\\right\\rfloor  
\]

and every degree multiset in each part, the sweep requires:

\[  
\\sum\_{v\\in V\_i}d(v)=m  
\\quad\\text{for every }i,  
\]

\[  
d(v)\\ge2,  
\]

\[  
\\sum\_vd(v)^2=m^2+5m+2X,  
\\tag{DM}  
\]

\[  
n\_2\\le\\left\\lfloor\\frac m2\\right\\rfloor,  
\\tag{D2}  
\]

\[  
P:=\\sum\_vF(d(v))  
\\le  
R-q\_1(q\_1+1),  
\\tag{LD}  
\]

\[  
F(d(v))\\le X-q\_1,  
\\tag{KC}  
\]

\[  
g(v)\\le X,  
\\tag{PC}  
\]

and

\[  
\\sum\_vg(v)\\le R.  
\\tag{GPC}  
\]

Here

\[  
F(d)=\\Phi(d,5).  
\]

The state space is finite. The dynamic-programming state is

\[  
\\left(\\sum d^2,\\ n\_2,\\ P,\\ \\sum g\\right).  
\]

No graph realization, SAT solver, ILP solver, or floating-point calculation is used. This is a relaxation: an empty state set proves nonexistence; a surviving state merely proceeds to structural analysis.

The outer sweep contains 407,253 excess-shape/part-size cells over the required (X=7,8,9) ranges. A direct state-set traversal and a Pareto-compressed traversal returned identical tables.

---

# **5\. (X=7): independently empty**

Certificate 0021 confines (X=7) to (22\\le m\\le26). The new sweep gives:

\[  
\\begin{array}{c|ccccc}  
m&22&23&24&25&26\\ \\hline  
\\text{survivors}&0&0&0&0&0  
\\end{array}  
\]

Thus ((GPC)) independently proves

\[  
X\\ne7.  
\]

This re-proves certificate 0023’s global headline without consuming:

* certificate 0022;  
* certificate 0023’s profile ledgers;  
* the parity sieve;  
* residual pairing;  
* the hand-generated quotient posture lists.

That is a meaningful trust-chain improvement. Certificates 0022 and 0023 remain valuable independent belts, but they need no longer carry the global excess floor.

---

# **6\. (X=8): exact survivor table**

Write

\[  
6^6=(6,6,6,6,6,6),  
\\qquad  
6^5 7=(6,6,6,6,6,7).  
\]

The entire (X=8) sweep leaves only:

| (m) | surviving ((\\pi;\\mathbf n)) |
| ----- | ----- |
| 22 | ((4,4);6^6) |
| 23 | ((4,4);6^6), ((3,3,2);6^6) |
| 24 | ((4,4);6^6), ((4,4);6^5 7), ((3,3,2);6^6) |
| 25 | ((4,4);6^6) |
| 26 | ((4,4);6^6) |
| 27–28 | none |

These all die structurally.

## **6.1 Shape ((4,4))**

The two (q=4) support pairs are edge-disjoint. Let their five-cell shared sets be (A,B).

If (|A\\cap B|\\ge2), the four support edges produce all six excessive pairs among themselves, impossible for a shape containing only two excessive pairs. Hence

\[  
|A\\cup B|\\ge9.  
\]

Every vertex of (A\\cup B) contributes at least (4) to (J), so

\[  
J\\ge36.  
\]

But

\[  
R=2\\cdot4\\cdot5=40,  
\]

and (P+J\\le R), so

\[  
P\\le4.  
\]

The relevant cost/value table is

\[  
\\begin{array}{c|rrrrrr}  
d&6&7&8&9&10&11\\ \\hline  
F(d)&1&2&3&4&5&7\\  
\\psi(d)&3&8&15&24&35&48  
\\end{array}  
\]

where

\[  
\\psi(d)=(d-5)*\+\\bigl((d-5)*\++2\\bigr).  
\]

Under (P\\le4),

\[  
\\Psi:=\\sum\_v\\psi(d(v))\\le24.  
\]

But the moment requirement is at least

\[  
\\Lambda\_8(22)=61.  
\]

Contradiction at every rung.

## **6.2 Shape ((3,3,2))**

Outside one exceptional support triangle, the two four-cell (q=3) shared sets have intersection at most one. Therefore

\[  
J\\ge3(4+3)=21.  
\]

Since (R=30),

\[  
P\\le9,  
\]

and the knapsack maximum is

\[  
\\Psi\\le59.  
\]

This is below

\[  
\\Lambda\_8(23)=63,  
\\qquad  
\\Lambda\_8(24)=64.  
\]

At (m=23), the only exceptional posture is a support triangle with pair labels (3,3,2). Every high vertex must lie in the triple intersection (T), with

\[  
|T|\\le3.  
\]

The sweep forces (6^6), and pointwise ((PC)) gives (d\\le7). Therefore

\[  
\\Psi\\le3\\psi(7)=24\<63.  
\]

Thus the (X=8) layer is empty.

---

# **7\. (X=9): exact survivor table**

The complete survivor table is:

| (m) | surviving ((\\pi;\\mathbf n)) |
| ----- | ----- |
| 22 | ((4,4,1);6^6) |
| 23 | ((4,4,1);6^6), ((4,4,1);6^5 7), ((4,3,2);6^6), ((3,3,3);6^6) |
| 24 | the preceding four types where applicable, plus ((3,3,3);6^5 7), ((3,3,2,1);6^6), ((3,3,1,1,1);6^6), ((3,2,2,2);6^6), ((2,2,2,2,1);6^6) |
| 25 | ((4,4,1);6^6,6^5 7), ((3,3,3);6^6,6^5 7), ((3,3,2,1);6^6) |
| 26 | ((4,4,1);6^6,6^5 7), ((3,3,3);6^6,6^5 7\) |
| 27–29 | none |

## **7.1 Shape ((4,4,1))**

As above, the two five-cell sets have union at least nine, so

\[  
J\\ge36.  
\]

Here (R=42), hence

\[  
P\\le6.  
\]

The maximum moment contribution is

\[  
\\Psi\\le38\<\\Lambda\_9(22)=63.  
\]

## **7.2 Shape ((4,3,2))**

The (q=4) and (q=3) support pairs are edge-disjoint, and their shared sets meet in at most one cell. Consequently

\[  
J\\ge4\\cdot5+3\\cdot3=29.  
\]

Since (R=38),

\[  
P\\le9,  
\\qquad  
\\Psi\\le59.  
\]

But

\[  
\\Lambda\_9(23)=65,  
\\qquad  
\\Lambda\_9(24)=66.  
\]

## **7.3 Shape ((3,3,3))**

Unless the support graph is a triangle, the three four-cell sets have pairwise intersections at most one, giving union size at least nine and

\[  
J\\ge27.  
\]

Thus

\[  
P\\le36-27=9,  
\\qquad  
\\Psi\\le59.  
\]

In the triangle posture, every high vertex lies in the common intersection (T), with (|T|\\le4).

At (6^6), pointwise ((PC)) gives (d\\le7), so

\[  
\\Psi\\le4\\psi(7)=32.  
\]

At (6^5 7), pointwise ((PC)) gives (d\\le8), so

\[  
\\Psi\\le4\\psi(8)=60\<66.  
\]

## **7.4 The four remaining shapes**

These are

\[  
(3,3,2,1),\\quad  
(3,3,1,1,1),\\quad  
(3,2,2,2),\\quad  
(2,2,2,2,1).  
\]

They occur only at (6^6).

A high vertex has (F(d)\\ge1). From

\[  
F(d(v))+q\_{\\max}(v)\\le s(v),  
\]

a high vertex cannot belong to only one shared set: that would give (s=q\_{\\max}). Hence every high vertex belongs to at least two shared sets.

The total numbers of shared-set incidences are respectively

\[  
13,\\ 14,\\ 13,\\ 14\.  
\]

Therefore the number (H) of high vertices is at most

\[  
6,\\ 7,\\ 6,\\ 7\.  
\]

At (6^6), pointwise ((PC)) gives (d\\le7), so every high vertex contributes at most (\\psi(7)=8). Thus

\[  
\\Psi\\le48  
\\quad\\text{or}\\quad  
\\Psi\\le56,  
\]

both below the smallest relevant moment requirement (66).

Therefore (X=9) is empty.

---

# **8\. First proposed theorem**

Starting only from certificate 0021’s certified (X\\ge7) floor and its (m)-windows:

* (X=7) has no ((GPC))-feasible degree/part state.  
* Every (X=8) survivor is structurally impossible.  
* Every (X=9) survivor is structurally impossible.

Hence:

\[  
\\boxed{X\\ge10\\text{ for every critical core}.}  
\]

This proposed proof does not consume certificates 0022 or 0023\. That is nearly as important as the two-unit floor increase.

---

# **9\. The (X=10) high-rung staircase**

The same machinery gives more.

## **9.1 Exact high-rung sweep**

For (X=10):

| (m) | ((GPC))-survivors |
| ----- | ----- |
| 28 | only ((4,4,2);6^6) |
| 29–32 | none |

For (m\\ge33), even the older (P/J) knapsack is enough. Across all 23 admissible partitions of (10),

\[  
\\max\\Psi=179,  
\]

attained by ((3,3,3,1)). But

\[  
\\Lambda\_{10}(33)=182.  
\]

Since (\\Lambda\_{10}(m)) is strictly increasing for (m\\ge22), (X=10) is impossible for every (m\\ge33).

The lone (m=28) state ((4,4,2)) dies exactly as before:

\[  
J\\ge36,\\qquad R=46,\\qquad P\\le10,  
\]

so

\[  
\\Psi\\le70\<\\Lambda\_{10}(28)=98.  
\]

## **9.2 The (m=27) row**

The sweep leaves only the shape types

\[  
(4,4,2),\\ (4,4,1,1),\\ (4,3,3),\\ (3,3,3,1),\\ (3,3,2,2).  
\]

All surviving part vectors are (6^6) or (6^5 7), so pointwise ((PC)) gives

\[  
d\\le8.  
\]

At (m=27),

\[  
\\Lambda\_{10}(27)=89.  
\]

With (d\\le8), a budget (P\\le17) yields at most (83), so every realization would require

\[  
P\\ge18.  
\]

The three shapes containing a (q=4) pair die immediately from the preceding union bounds.

For ((3,3,3,1)), a nontriangle support graph gives (J\\ge27), impossible with (P\\ge18) and (R=38). In the triangle case, high vertices are confined to at most four common cells plus the two cells of the (q=1) set, giving

\[  
\\Psi\\le4\\cdot15+2\\cdot3=66\<89.  
\]

For ((3,3,2,2)), the nontriangle case gives (J\\ge21). The only remaining support triangle has a three-cell common core. Its three core vertices contribute at most (45); the remaining (q=2) set can make at most two further vertices degree (7), giving

\[  
\\Psi\\le45+2\\cdot8=61\<89.  
\]

Thus (X=10) is impossible at (m=27).

## **9.3 The (m=26) row**

The exact sweep leaves nine shape types:

\[  
\\begin{aligned}  
&(4,4,2),\\ (4,4,1,1),\\ (4,3,3),\\ (4,3,2,1),\\  
&(3,3,3,1),\\ (3,3,2,2),\\ (3,3,2,1,1),\\  
&(2,2,2,2,2),\\ (2,2,2,2,1,1).  
\\end{aligned}  
\]

All surviving part vectors are among

\[  
6^6,\\qquad6^5 7,\\qquad6^4 7^2,  
\]

and pointwise ((PC)) again gives (d\\le8).

Now

\[  
\\Lambda\_{10}(26)=79.  
\]

For degrees (6,7,8), the cost/value pairs are

\[  
(1,3),\\quad(2,8),\\quad(3,15).  
\]

A budget (P\\le16) gives at most (78), so

\[  
P\\ge17.  
\]

The four shapes containing (q=4) die from their (J)-lower bounds.

For ((3,3,3,1)), the nontriangle branch has (J\\ge27); the triangle branch has

\[  
\\Psi\\le66.  
\]

For ((3,3,2,2)), the nontriangle branch has (J\\ge21). The only triangle branch has a three-cell common core and satisfies

\[  
\\Psi\\le61.  
\]

For ((3,3,2,1,1)), the same triangle analysis and four available (q=1) incidences give

\[  
\\Psi\\le61.  
\]

The two low-(q) shapes die by a pure shared-set-incidence budget.

For ((2^5)), there are 15 shared-set incidences. A degree-(8) vertex requires at least three memberships; degrees (6) and (7) require at least two. Hence the abstract maximum is

\[  
\\max{15a+8b+3c:3a+2b+2c\\le15}=75\<79.  
\]

For ((2^4,1,1)), there are 16 shared-set incidences. The same relaxation gives

\[  
\\max{15a+8b+3c:3a+2b+2c\\le16}=76\<79.  
\]

Therefore (X=10) is impossible at (m=26).

Combining the rows:

\[  
\\boxed{X=10\\Longrightarrow m\\le25.}  
\]

Equivalently,

\[  
\\boxed{m\\ge26\\Longrightarrow X\\ge11.}  
\]

---

# **10\. Recommended certificate architecture**

I would not put everything into one monolithic file.

## **Certificate 0024: global part-collision**

This certificate should contain:

1. The pointwise and global ((PC)/(GPC)) proof.  
2. The exact degree/part dynamic program.  
3. Generated assertions for:  
   * 11 admissible partitions of (7);  
   * 15 admissible partitions of (8);  
   * 18 admissible partitions of (9);  
   * 23 admissible partitions of (10).  
4. The zero-survivor (X=7) table.  
5. The exact (X=8) and (X=9) survivor tables.  
6. Positive controls:  
   * ((8,24),(4,4),6^5 7);  
   * ((9,24),(3,3,3),6^5 7);  
   * ((10,28),(4,4,2),6^6).  
7. Two state engines:  
   * direct state-set DP;  
   * Pareto-compressed DP;  
     with identical output assertions.

Essential mutations should include:

* remove global (\\sum g\\le R);  
* relax pointwise (g(v)\\le X);  
* omit (n\>36) vectors;  
* relax (n\_2\\le\\lfloor m/2\\rfloor);  
* delete one admissible excess partition;  
* delete one degree partition from a part;  
* replace exact (\\sum d^2) by an inequality.

## **Certificate 0025: structural cleanup**

This should contain only the finite survivor kills:

* (X=8): ((4,4)), ((3,3,2)), triangle exception.  
* (X=9): four principal shapes plus the shared-set-incidence bound.  
* (X=10), (m\\ge26): high-(q) union bounds, triangle capacities, and low-(q) incidence knapsacks.

The support-graph triangle/nontriangle alternatives should be generated from small simple graphs rather than listed narratively.

## **New load-bearing chain**

Once those certificates are green, the preferred global chain becomes

\[  
0021  
\\longrightarrow  
0024  
\\longrightarrow  
0025,  
\]

yielding

\[  
X\\ge10  
\\quad\\text{and}\\quad  
m\\ge26\\Rightarrow X\\ge11.  
\]

Certificates 0022 and 0023 become independent belts rather than necessary pillars.

---

# **11\. What the Holy Grail now looks like**

No counterexample has appeared, and this does not prove Ryser. But the search geometry has changed again.

A minimal counterexample must now satisfy

\[  
22\\le m\\le456,  
\\qquad  
X\\ge10.  
\]

More sharply,

\[  
X=10\\Longrightarrow22\\le m\\le25,  
\]

and

\[  
m\\ge26\\Longrightarrow X\\ge11.  
\]

The immediate finite target is therefore no longer (X=8) on seven rungs. It is:

\[  
\\boxed{X=10\\text{ on only }m\\in{22,23,24,25}.}  
\]

That is the correct next campaign.

The best engine for it is not another raw moment inequality. The (m=25) survivors already point toward a small quotient problem involving three- and four-cell shared-set universes. The banked quotient-completeness engine ((EC)), now combined with global part-collision and ((RG2)), is exactly the right machinery.

# **Bottom line**

**Current repository:** agreed; no major error found.

**Minor repairs:** mutation count, independence wording, `M-P2` description, and one vacuous checker conjunct.

**New mathematical advance, pending Cofferdam certification:**

\[  
\\boxed{X\\ge10\\text{ everywhere}}  
\]

and

\[  
\\boxed{m\\ge26\\Longrightarrow X\\ge11.}  
\]

The proposed live minimum-excess frontier is now

\[  
\\boxed{X=10,\\quad 22\\le m\\le25.}  
\]

That is a real compression of the counterexample universe—and, just as importantly, it replaces the most delicate part of the current chain with a short global invariant and an exact finite degree/part calculation.

