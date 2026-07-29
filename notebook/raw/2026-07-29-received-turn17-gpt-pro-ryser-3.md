# **Cofferdam audit — post-certificate 0020**

> **Scope.** This audit is pinned to the post-0020 state of `main`, including the documentation sweep at commit `2a09954`. That sweep correctly retired several frontiers already closed by later certificates.

## **Executive verdict**

**I agree with the repository’s certified state through 0020\.** I found no fatal error in:

* the critical-core reduction and finite window (22\\le m\\le456);  
* the part-confinement refinement (462\\to456);  
* the strict star-collision inequalities;  
* (X\\ge6) throughout the window;  
* the existing four-step staircase;  
* the quadratic law  
  \[  
  m(m-25)+\\Sigma\_5+10H\\le38X.  
  \]

The finite-window argument correctly distinguishes arbitrary counterexamples from edge-critical cores, and the 456 refinement uses exactly the additional partite structure it says it uses.

Certificate 0020’s analytic heart also survives scrutiny: the (\\lambda\\le4) cover argument, five-fibre collision count, sharp ((\\mathrm{SSC}+)) guard, summation to (P+H\\le R), residue identity, and global degree cap all have the correct direction and hypotheses.

The exceptional ((X,m,\\pi)=(8,30,(3,3,1,1))) argument is valid. In particular, its proof of (|S\_i\\cap S\_j|\\le1), the (|T\_v|\\ge2) consequence, and the linear-profile maximum are logically sufficient; I do not see the defect that would be needed to reopen that cell.

There is, however, a **large underclaim**:

> ## **New theorem candidate**

> \[  
> \\boxed{X\\ge7\\quad\\text{for every critical core in }22\\le m\\le456.}  
> \]

> More strongly,  
> \[  
> \\boxed{  
> \\begin{aligned}  
> X=7&\\Longrightarrow m\\le26,\\  
> X=8&\\Longrightarrow m\\le28,\\  
> X=9&\\Longrightarrow m\\le29.  
> \\end{aligned}}  
> \]

Consequently, subject to house certification, the low-(m) staircase becomes

\[  
\\boxed{  
X\\ge  
\\begin{cases}  
7,&22\\le m\\le26,\\  
8,&27\\le m\\le28,\\  
9,\&m=29,\\  
10,&30\\le m\\le456.  
\\end{cases}}  
\]

This does **not** prove Ryser (r=6), nor construct a counterexample. It does replace the current (X=6) frontier by an (X=7) frontier and improves every step of the existing staircase. The repository presently describes (X=6) on (m=22,\\ldots,26) as its next field, and labels the (m=26) exclusion only “measured”; both would be superseded.

The proof below is a complete hand proof, but it has not yet passed Cofferdam’s independent-lane and certificate process.

---

# **1\. The unused strength inside 0020**

Let

\[  
J:=\\sum\_v q\_{\\max}(v).  
\]

Certificate 0020 proves, before weakening (J) to (H),

\[  
\\boxed{P+J\\le R,}  
\\qquad  
P=\\sum\_v F(d(v)),  
\\qquad  
R=\\sum\_{{e,f}}q\_{ef}(q\_{ef}+1).  
\\tag{SJ}  
\]

The published claim row records only the weaker (P+H\\le R), but the proof explicitly establishes the stronger line.

Let (q\_1) be the largest pair excess and (S\_1) its shared set. Since

\[  
|S\_1|=q\_1+1  
\]

and every (v\\in S\_1) has (q\_{\\max}(v)\\ge q\_1),

\[  
J\\ge q\_1(q\_1+1).  
\]

Therefore

\[  
\\boxed{P\\le R-q\_1(q\_1+1).}  
\\tag{D}  
\]

This is the **largest-pair debit**. It is substantially stronger than charging only (+1) for each high vertex.

We also retain 0020’s global cap

\[  
\\boxed{F(d(v))\\le X-q\_1}  
\\tag{K}  
\]

at every vertex.

The other ingredients are already certified:

\[  
\\sum\_v d(v)=6m,\\qquad  
\\sum\_v d(v)^2=m^2+5m+2X,  
\\tag{M}  
\]

\[  
n\\ge36,\\qquad n\_2\\le\\left\\lfloor\\frac m2\\right\\rfloor.  
\\tag{N/D2}  
\]

The moments are exact double counts; (n\\ge36) comes from six active cells per part, and the degree-two cap is certificate 0008\.

---

# **2\. A new moment inequality**

For (2\\le d\\le10), put

\[  
f(d):=(d-5)\_+=F(d).  
\]

For every such (d),

\[  
d^2\\le  
8d-15+3,\\mathbf 1\_{{d=2}}+f(d)(f(d)+2).  
\\tag{1}  
\]

It is equality except at (d=4), where the right side is larger by one.

Summing (1), then using (M), (N/D2), gives

\[  
m^2+5m+2X  
\\le  
48m-540+3\\left\\lfloor\\frac m2\\right\\rfloor  
\+\\sum\_v f(v)(f(v)+2).  
\]

Thus every candidate must satisfy

\[  
\\boxed{  
\\Psi:=\\sum\_v f(v)(f(v)+2)  
\\ge  
\\Lambda\_X(m):=  
m^2-43m+2X+540  
\-3\\left\\lfloor\\frac m2\\right\\rfloor.}  
\\tag{2}  
\]

For (X=6),

| (m) | (22) | (23) | (24) | (25) | (26) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| (\\Lambda\_6(m)) | (57) | (59) | (60) | (66) | (71) |

At (X=6), (K) gives (F(d)\\le5), hence (d\\le10), so (1) covers every vertex.

For a partition (\\pi) of the excess, let

\[  
B(\\pi)=R(\\pi)-q\_1(q\_1+1),\\qquad C=6-q\_1.  
\]

By (D) and (K),

\[  
\\sum f\_v\\le B(\\pi),\\qquad 0\\le f\_v\\le C.  
\]

Since (f(f+2)) is convex, its maximum is obtained by filling (f=C) repeatedly and then using the remainder.

---

# **3\. Five of the seven (X=6) partitions die immediately**

The seven partitions of six with parts at most three are:

| (\\pi) | (R(\\pi)) | (B(\\pi)) | cap on (f) | maximum possible (\\Psi) |
| ----- | ----- | ----- | ----- | ----- |
| ((3,3)) | 24 | 12 | 3 | 60 before geometry |
| ((3,2,1)) | 20 | 8 | 3 | **38** |
| ((3,1,1,1)) | 18 | 6 | 3 | **30** |
| ((2,2,2)) | 18 | 12 | 4 | 72 before geometry |
| ((2,2,1,1)) | 16 | 10 | 4 | **56** |
| ((2,1,1,1,1)) | 14 | 8 | 4 | **48** |
| ((1,1,1,1,1,1)) | 12 | 10 | 5 | 70 before geometry |

Since the smallest required value is (57), four rows die immediately.

The ((3,3)) row also dies easily. The C3 bound gives (x\_e\\le5) throughout (m=22,\\ldots,26), so the two (q=3) pairs cannot share a hyperedge. C3 is the same per-edge inequality already used to form 0020’s staircase.

If their two four-element shared sets met in two vertices, all six pairs among their four endpoint hyperedges would be excessive, forcing total excess at least

\[  
3+3+4=10.  
\]

Hence their intersection has size at most one. Their union has at least seven vertices, each contributing (3) to (J), so

\[  
J\\ge21,\\qquad P\\le24-21=3.  
\]

Thus (\\Psi\\le15\<57).

Only

\[  
(2,2,2)\\quad\\text{and}\\quad(1^6)  
\]

remain.

---

# **4\. The ((2,2,2)) case**

Form the **excess graph** (G) whose vertices are hyperedges of (K), and whose three edges are the three excessive pairs. Each edge of (G) has weight (2).

For a cell (v), the set of positive pairs containing (v) is the edge set induced by the hyperedges through (v). This induced-subgraph condition is stronger than treating an arbitrary subset of the three excess pairs as a possible (T\_v).

## **4.1 Nontriangle excess graph**

If (G) is not a triangle, any two shared sets (S\_i,S\_j) meet in at most one cell:

* for edge-disjoint excess pairs, two common cells would force all six pairs on four endpoints to be excessive;  
* for adjacent excess pairs, two common cells would force the closing edge and hence a triangle.

Three 3-sets with pairwise intersections at most one have union size at least six. Therefore

\[  
J\\ge2\\cdot6=12,\\qquad P\\le18-12=6.  
\]

With (f\\le4),

\[  
\\Psi\\le 4(4+2)+2(2+2)=32\<57.  
\]

## **4.2 Triangle excess graph**

Let the three excess pairs be the triangle on hyperedges (a,b,c). A cell lying in two of the three shared sets automatically lies in the third. Thus every high cell belongs to

\[  
T:=S\_{ab}\\cap S\_{ac}\\cap S\_{bc}.  
\]

If (|T|\\le2), there are at most two high cells and

\[  
\\Psi\\le2\\cdot24=48.  
\]

Suppose (|T|=3) and all three cells are high. Write their degrees as

\[  
d\_i=5+f\_i,\\qquad 1\\le f\_i\\le4.  
\]

No hyperedge outside ({a,b,c}) can contain two of these cells: such an edge would create three additional excessive pairs. Hence their three stars have pairwise and triple intersection exactly ({a,b,c}), and their union has size

\[  
\\sum\_i d\_i-6=9+\\sum\_i f\_i.  
\]

### **Residual-pairing lemma**

For any set (U) of (k\\le5) cells, let (K\_U) be the hyperedges avoiding (U). Then

\[  
\\tau(K\_U)\\ge6-k;  
\]

otherwise a cover of (K\_U), together with (U), would give a 5-cover of (K).

An intersecting family with (r) edges has a cover of size at most (\\lceil r/2\\rceil): pair its edges and choose one intersection cell from every pair. Therefore

\[  
|K\_U|\\ge2(6-k)-1.  
\\tag{R}  
\]

For the three cells above, (k=3), so at least five hyperedges avoid them. Consequently

\[  
9+\\sum\_i f\_i\\le m-5,  
\\qquad  
\\sum\_i f\_i\\le m-14.  
\]

The largest possible values of (\\Psi) are therefore:

| (m) | cap on (\\sum f\_i) | maximizing (f)-profile | maximum (\\Psi) | required |
| ----- | ----- | ----- | ----- | ----- |
| 22 | 8 | (4,3,1) | 42 | 57 |
| 23 | 9 | (4,4,1) | 51 | 59 |
| 24 | 10 | (4,4,2) | 56 | 60 |
| 25 | 11 | (4,4,3) | 63 | 66 |

At (m=26), only (f=(4,4,4)) could survive (2). Then the three high degrees are (9,9,9). But the exact identity

# **\[**

# **\\sum\_v d(v)^2**

42m-10n+\\sum\_v(d(v)-2)(d(v)-5)  
\]

and (n\\ge36) give

\[  
\\sum\_vd(v)^2  
\\le  
42\\cdot26-360+3\\cdot28  
\=816,  
\]

whereas the required second moment is

\[  
26^2+5\\cdot26+12=818.  
\]

So ((2,2,2)) is empty for every (m=22,\\ldots,26).

---

# **5\. The ((1^6)) case**

Here (R=12), (q\_1=1), and

\[  
P\\le10,\\qquad f\\le5.  
\]

Without an (f=5) vertex, convexity gives

\[  
\\Psi\\le56\<57.  
\]

Let (u) have (f(u)=5), so (d(u)=10). Since ((\\mathrm{SSC}+)) gives

\[  
F(d(u))+q\_{\\max}(u)\\le s(u),  
\]

we have (s(u)\\ge6). But all excess totals only six, so (u) belongs to **all six** shared sets.

Thus every endpoint of the excess graph (G) contains (u).

If another high cell (w) lies on a set (B) of support hyperedges, any two hyperedges in (B) share both (u) and (w). Hence (B) induces a clique of (G). With six edges total, the only possible clique sizes are:

* two support vertices: one excess edge, forcing (f(w)=0);  
* three support vertices: a triangle, forcing (f(w)\\le2);  
* four support vertices: (K\_4), allowing (f(w)\\le5).

If (G\\ne K\_4), the remaining (P)-budget is at most five and every other high cell has (f\\le2). Therefore

\[  
\\Psi\\le35+8+8+3=54\<57.  
\]

So a survivor forces (G=K\_4) and a second cell (v) common to all four support hyperedges. Since every excessive pair has intersection size two,

\[  
S\_i={u,v}  
\]

for all six pairs. These are the only high cells.

Put

\[  
p=f(u)+f(v).  
\]

Their stars intersect in exactly the four support hyperedges, so their union has size

\[  
(5+f(u))+(5+f(v))-4=6+p.  
\]

The residual avoiding (u,v) has covering number at least four. Applying the residual-pairing lemma with (k=2), it has at least seven edges. Hence

\[  
6+p\\le m-7,\\qquad p\\le m-13.  
\\tag{3}  
\]

Combining (2), (3), and (P\\le10), only the following cases survive numerically:

| (m) | possible high degrees |
| ----- | ----- |
| 22 | (10,9) |
| 23 | (10,9) or (10,10) |
| 24 | (10,10) |
| 25 | (10,10) |
| 26 | none |

In each surviving case, (n=36); if (n\\ge37), the (-15n) term in (1) already drops the maximum below the required second moment. The two high cells occupy different parts, leaving four **ordinary parts**.

For every hyperedge (e),

# **\[**

# **\\sum\_{z\\in e}(d(z)-1)**

# **\\sum\_{f\\ne e}|e\\cap f|**

(m-1)+x\_e.  
\]

Thus

\[  
\\boxed{\\sum\_{z\\in e}d(z)=m+5+x\_e.}  
\\tag{4}  
\]

Each of the four (K\_4) support hyperedges has (x\_e=3). Moreover, no ordinary cell can contain two support hyperedges, since those two hyperedges already share (u,v) and have (q=1).

The moment equations give the following possible low-degree counts:

| (m) | high degrees | possible ((n\_2,n\_3,n\_4,n\_5)) |
| ----- | ----- | ----- |
| 22 | (10,9) | ((11,11,2,10)) |
| 23 | (10,9) | ((11,9,0,14)) |
| 23 | (10,10) | ((11,4,11,8)), ((10,7,8,9)), ((9,10,5,10)), ((8,13,2,11)) |
| 24 | (10,10) | ((12,0,10,12)), ((11,3,7,13)), ((10,6,4,14)), ((9,9,1,15)) |
| 25 | (10,10) | ((12,0,4,18)), ((11,3,1,19)) |

Now use (4) on each support hyperedge.

### **(m=22)**

The four ordinary cell degrees sum to

\[  
22+5+3-10-9=11.  
\]

Because an edge contains at most one degree-two cell, the only possibility is

\[  
(2,3,3,3).  
\]

The four support edges therefore require twelve **distinct** degree-three cells in the ordinary parts. But the whole family has only (n\_3=11). Contradiction.

### **(m=23), high degrees (10,9)**

The ordinary degrees sum to (12). Since (n\_4=0) and an edge cannot hold two degree-two cells, every support edge must have

\[  
(3,3,3,3)  
\]

in the ordinary parts. That requires sixteen distinct degree-three cells, against (n\_3=9).

### **(m=23), high degrees (10,10)**

The ordinary degrees sum to (11), so every support edge again needs

\[  
(2,3,3,3).  
\]

Thus the ordinary parts need at least twelve degree-three cells and four degree-two cells.

The first three candidate degree vectors have (n\_3\<12). In the last vector,

\[  
(n\_2,n\_3,n\_4,n\_5)=(8,13,2,11).  
\]

Each special part consists of its degree-ten cell and five low cells summing thirteen. The possible low profiles are

\[  
(5,2,2,2,2),\\qquad  
(4,3,2,2,2),\\qquad  
(3,3,3,2,2).  
\]

To leave twelve of the thirteen degree-three cells for the ordinary parts, the two special parts together may contain at most one degree-three cell. They must therefore consume at least seven of the eight degree-two cells, leaving at most one for the ordinary parts—against the four required.

### **(m=24)**

The ordinary degrees sum to (12). Every support edge has one of

\[  
(3,3,3,3),\\qquad (2,3,3,4).  
\]

Let (t) be the number of support edges of the second type. Then the support edges require

\[  
16-2t  
\]

distinct degree-three cells and (t) distinct degree-four cells.

The first three global degree vectors have (n\_3=0,3,6), below the minimum (8). The last has

\[  
(n\_3,n\_4)=(9,1).  
\]

To reduce the degree-three demand to at most nine requires (t=4), which in turn requires four degree-four cells. Only one exists.

### **(m=25)**

The ordinary degrees sum to (13). The possibilities are

\[  
(3,3,3,4),\\qquad  
(2,3,4,4),\\qquad  
(2,3,3,5).  
\]

Every support edge therefore needs at least one degree-three cell, and no ordinary block can serve two support edges. At least four degree-three cells are required. The two global vectors have (n\_3=0) and (n\_3=3).

Thus ((1^6)) is empty throughout (m=22,\\ldots,26).

Combining all seven partitions proves:

\[  
\\boxed{X\\ne6\\quad\\text{for }22\\le m\\le26.}  
\]

Since 0020 already confines (X=6) to that band, we obtain

\[  
\\boxed{X\\ge7\\text{ window-wide}.}  
\]

---

# **6\. The same engine strengthens the staircase**

For (d=6,\\ldots,11), the cost (F(d)) and moment value

\[  
\\psi(d):=d^2-8d+15  
\]

are

| (d) | 6 | 7 | 8 | 9 | 10 | 11 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| (F(d)) | 1 | 2 | 3 | 4 | 5 | 7 |
| (\\psi(d)) | 3 | 8 | 15 | 24 | 35 | 48 |

The same inequalities apply:

\[  
\\Psi:=\\sum\_{d(v)\\ge6}\\psi(d(v))  
\\ge  
\\Lambda\_X(m),  
\]

\[  
P\\le R-q\_1(q\_1+1),\\qquad F(d)\\le X-q\_1.  
\]

## **6.1 (X=7) at (m=27,28)**

The required values are

\[  
\\Lambda\_7(27)=83,\\qquad  
\\Lambda\_7(28)=92.  
\]

The cost-value knapsack kills every partition of seven except

\[  
\\pi=(2,2,2,1).  
\]

On both rungs, C3 gives (x\_e\\le3). Hence the three (q=2) excess pairs are edge-disjoint. Their three 3-element shared sets meet pairwise in at most one cell; otherwise four endpoint hyperedges would generate six excessive pairs, while this partition has only four.

Their union has at least six cells, so

\[  
J\\ge12,\\qquad P\\le20-12=8.  
\]

The maximum moment value purchasable with (P\\le8) is

\[  
35+15=50,  
\]

far below both required values. Therefore

\[  
\\boxed{X=7\\Longrightarrow m\\le26.}  
\]

## **6.2 (X=8) at (m=29)**

Here

\[  
\\Lambda\_8(29)=108,\\qquad x\_e\\le3.  
\]

Only four partitions survive the initial knapsack:

\[  
(3,3,2),\\quad  
(3,3,1,1),\\quad  
(2,2,2,2),\\quad  
(2,2,2,1,1).  
\]

The C3 cap forces every (q=3) pair to be isolated from every other positive pair, and forces the (q=2) pairs to be mutually edge-disjoint.

The resulting shared-set union bounds give:

| partition | lower bound on (J) | upper bound on (P) | maximum (\\Psi) |
| ----- | ----- | ----- | ----- |
| ((3,3,2)) | 23 | 7 | 43 |
| ((3,3,1,1)) | 21 | 7 | 43 |
| ((2,2,2,2)) | 12 | 12 | 78 |
| ((2,2,2,1,1)) | 12 | 10 | 70 |

For the four weight-two pairs, the union of their four 3-sets has size at least six: otherwise twelve incidences on at most five cells would force more than six pairwise block intersections, contradicting pairwise intersection at most one.

All four maxima are below 108\. Hence

\[  
\\boxed{X=8\\Longrightarrow m\\le28.}  
\]

## **6.3 (X=9) at (m=30,31)**

The required values are

\[  
\\Lambda\_9(30)=123,\\qquad  
\\Lambda\_9(31)=141,  
\]

and C3 again gives (x\_e\\le3).

At (m=31), only ((3,3,3)) survives the initial knapsack. Its three (q=3) pairs are edge-disjoint; their three 4-sets have union at least nine. Thus

\[  
J\\ge27,\\qquad P\\le36-27=9,\\qquad \\Psi\\le59\<141.  
\]

At (m=30), only

\[  
(3,3,3),\\qquad (3,3,2,1),\\qquad (2,2,2,2,1)  
\]

survive initially. The same geometry gives:

| partition | upper bound on (P) | maximum (\\Psi) |
| ----- | ----- | ----- |
| ((3,3,3)) | 9 | 59 |
| ((3,3,2,1)) | 9 | 59 |
| ((2,2,2,2,1)) | 14 | 96 |

All are below 123\. Therefore

\[  
\\boxed{X=9\\Longrightarrow m\\le29.}  
\]

---

# **7\. Proposed new certified state**

If the argument survives Cofferdam’s normal hostile intake and independent implementation, the README/PLAN state should become:

> Every critical core has (22\\le m\\le456), and

> \[  
> X\\ge  
> \\begin{cases}  
> 7,&22\\le m\\le26,\\  
> 8,&27\\le m\\le28,\\  
> 9,\&m=29,\\  
> 10,&30\\le m\\le456,  
> \\end{cases}  
> \]

> together with the existing quadratic law  
> \[  
> X\\ge\\left\\lceil\\frac{m(m-25)}{38}\\right\\rceil  
> \]  
> and its (H)-refinement.

The current repository correctly warns that floors do not assert existence of a counterexample. That warning remains essential.

---

# **8\. The new live frontier**

The minimum-excess band becomes

\[  
\\boxed{X=7,\\qquad m\\in{22,23,24,25,26}.}  
\]

At its top rung (m=26), the same moment/debit calculation reduces the seven-partition field to only two excess shapes:

\[  
\\boxed{(2,2,2,1)\\quad\\text{and}\\quad(1^7).}  
\]

The other partitions die as follows:

* ((3,2,2)) misses the moment requirement by one;  
* ((3,2,1,1)), ((3,1^4)), and ((2,1^5)) die by the basic knapsack;  
* ((3,3,1)) dies after debiting the union of its two (q=3) shared sets;  
* ((2,2,1,1,1)) dies after observing that the two 3-element (q=2) shared sets cannot coincide and yield too much (J).

So the immediate next hand-kill is not a seven-shape campaign. It is a **two-shape campaign at ((X,m)=(7,26))**.

---

# **9\. Certificate 0021 blueprint**

I would package this as:

certificates/0021-qmax-debit-x7/

Suggested claim rows:

1. **(SJ)** (P+\\sum\_vq\_{\\max}(v)\\le R).  
2. **(LD)** (P\\le R-q\_1(q\_1+1)).  
3. **(DM)** the D2–moment inequality (2).  
4. **(RG)** the residual-pairing lemma.  
5. **(T-A21)** (X\\ge7) window-wide.  
6. **(T-B21)** (X=7\\Rightarrow m\\le26), (X=8\\Rightarrow m\\le28), (X=9\\Rightarrow m\\le29).

The verifier should independently check:

* the pointwise inequality for every permitted degree;  
* every integer partition of (X=6,7,8,9);  
* the cost-value knapsack by exhaustive integer recursion;  
* completeness of the small excess-graph classes;  
* the K4 degree-count table;  
* the local identity (4);  
* all support-edge profile lists;  
* the four-set union lower bound used for weight-two matchings.

Useful mutants:

* remove the (q\_1(q\_1+1)) debit;  
* replace (n\_2\\le\\lfloor m/2\\rfloor) by (n\_2\\le\\lfloor m/2\\rfloor+1);  
* permit (n=35);  
* raise the C3 cap from (3) to (4) on the top-rung checks;  
* permit two support hyperedges in one ordinary block;  
* weaken the residual-pairing bounds (7\\to6) and (5\\to4);  
* omit the induced-subgraph requirement in the ((2,2,2)) triangle.

The debit and D2 are genuinely load-bearing; this certificate should not inherit 0020’s statement that the staircase is D2-free.

---

# **10\. Minor issues and corrections**

I found **no current mathematical statement that needs retraction**.

The necessary changes are supersessions rather than corrections:

1. README and PLAN currently call (X=6) on (m=22,\\ldots,26) the live frontier. That becomes stale if 0021 certifies.  
2. The (m=26) structural exclusion in 0020 is deliberately labeled “measured, not claimed.” It is correct but much weaker than the argument above, which eliminates every (X=6) partition on every remaining rung.  
3. The stronger summation  
   \[  
   P+\\sum q\_{\\max}\\le R  
   \]  
   should receive its own name and claim row. Burying it inside the proof of (P+H\\le R) hid the strongest available resource.  
4. The new theorem shifts risk back toward 0008’s D2 cap. That dependency should be prominent in the new risk table rather than described as incidental.

## **Bottom line**

**No major mistake found. The project’s current mathematics stands.**

But the current state is apparently not maximal:

\[  
\\boxed{\\text{The }X=6\\text{ frontier can be closed completely.}}  
\]

And the same mechanism appears to move the staircase to

\[  
\\boxed{7,\\ 8,\\ 9,\\ 10\\text{ at }m=22,\\ 27,\\ 29,\\ 30.}  
\]

That leaves a sharply reduced next target:

\[  
\\boxed{X=7,\\ m\\le26,\\quad\\text{with only two shapes at }m=26.}  
\]

This is the strongest realistic push I see from the present machinery without pretending that the Holy Grail itself has already fallen