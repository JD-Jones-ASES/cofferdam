# **Cofferdam audit — 1 August 2026**

## **Verdict**

**I agree with the project’s current claimed state through certificate 0021\.** I found no major mathematical error in the load-bearing chain establishing

\[  
22\\le m\\le456,\\qquad X\\ge7,  
\]

together with

\[  
m\\ge27\\Rightarrow X\\ge8,\\qquad  
m\\ge29\\Rightarrow X\\ge9,\\qquad  
m\\ge30\\Rightarrow X\\ge10,  
\]

and the window-wide quadratic bound

\[  
X\\ge \\left\\lceil \\frac{m(m-25)}{38}\\right\\rceil.  
\]

That is accurately represented in the current README and PLAN.

I separately checked the logic behind the newest ingredients:

\[  
P+J\\le R,\\qquad  
P\\le R-q\_1(q\_1+1),  
\]

\[  
\\Psi=m^2-43m+2X+15n-3n\_2+n\_4,  
\]

the residual-pairing lemma, and the cost-(F)/value-(\\psi) knapsack convention. Those are the right formulas and are used in the right directions. The two particularly fragile imported ingredients—the degree-two cap and the per-edge (C3) law—also remain sound under this audit.

This still does **not** prove Ryser at (r=6) or produce a counterexample. Recent sources continue to describe the intersecting case as open beginning at (r=6).

The important new result from this turn is:

> ## **Proposed certificate 0022**

> \[  
> \\boxed{X=7\\Longrightarrow m\\le24.}  
> \]

> Equivalently,

> \[  
> \\boxed{m\\ge25\\Longrightarrow X\\ge8.}  
> \]

I believe the proof below is complete. I independently recomputed all the small integer optimizations and degree censuses, but it has not yet gone through Cofferdam’s green-certificate and hostile-mutation process.

---

# **1\. One real but non-load-bearing mistake in 0021**

There is one incorrect sentence in the triangle treatment underlying the (m=26) frontier preview:

> “Every high cell lies in (T),” where (T=e\_1\\cap e\_2\\cap e\_3) is the common intersection of the three hyperedges supporting a (q=2) triangle.

That is not literally true when the fourth excessive pair has (q=1).

Let (S\_4) be the two-cell shared set of that (q=1) pair, and let

\[  
U=S\_{12}\\cup S\_{13}\\cup S\_{23}  
\]

be the union of the three (q=2) shared sets. A cell

\[  
v\\in S\_4\\cap(U\\setminus T)  
\]

lies in one (q=2) shared set and in the (q=1) shared set. Therefore

\[  
s(v)=2+1=3,\\qquad q\_{\\max}(v)=2,  
\]

so strict star-collision gives only

\[  
F(d(v))\\le s(v)-q\_{\\max}(v)=1.  
\]

Thus (d(v)=6) is possible: a high cell can occur outside (T).

## **Repair**

The repair is inexpensive.

First,

\[  
|S\_4\\cap U|\\le1.  
\]

Indeed, if (S\_4) contained two cells of (U), each of those cells would belong to at least two of the three triangle hyperedges. Any two two-element subsets of a three-element set intersect, so one triangle hyperedge would contain both cells. Each edge supporting (S\_4) would then meet that triangle edge twice, producing additional excessive pairs.

The corrected triangle optimizer therefore allows:

* the old high cells in (T);  
* at most one additional outside cell with (F(d)\\le1).

After adding that missing possibility, the relevant maxima remain unchanged:

\[  
\\begin{array}{c|ccc}  
m&25&26&27\\ \\hline  
\\text{corrected triangle maximum}&67&74&83.  
\\end{array}  
\]

So this defect does **not** invalidate any theorem in 0021:

* the (X=6) triangle has no (S\_4), so the original statement is true there;  
* at the claimed (X=7) staircase rungs (m\\ge27), (C3) excludes the (q=2) triangle altogether;  
* the (m=26) calculation is a frontier preview, not a claim row.

It should nevertheless be corrected before the triangle routine is reused. The current numerical answer survives; the stated reason needs repair.

A smaller engineering note: the finite search for the largest degree at a given collision cost uses a hard-coded degree ceiling. It is harmless at the current tiny budgets but should be replaced by a monotone loop so the checker does not acquire a silent future range assumption.

---

# **2\. Setup for the new theorem**

For each excessive pair (p={e,f}), write

\[  
q(p)=|e\\cap f|-1,\\qquad S(p)=e\\cap f.  
\]

Let the positive (q)-values form the excess partition

\[  
\\pi=(q\_1,\\ldots,q\_k),\\qquad \\sum\_iq\_i=X.  
\]

Use the established quantities

\[  
R=\\sum\_iq\_i(q\_i+1),  
\]

\[  
P=\\sum\_vF(d(v)),\\qquad  
J=\\sum\_vq\_{\\max}(v),  
\]

and

\[  
\\Psi=\\sum\_v\\psi(d(v)),  
\\qquad  
f(d)=(d-5)\_+,\\qquad  
\\psi(d)=f(d)(f(d)+2).  
\]

Certificate 0021 gives

\[  
P+J\\le R  
\\tag{SJ}  
\]

and the key cap

\[  
F(d(v))\\le X-q\_1.  
\\tag{KC}  
\]

For (d=6,\\dots ,10),

\[  
\\begin{array}{c|ccccc}  
d&6&7&8&9&10\\ \\hline  
F(d)&1&2&3&4&5\\  
\\psi(d)&3&8&15&24&35.  
\\end{array}  
\\tag{1}  
\]

At both ((X,m)=(7,25)) and ((7,26)), (C3) gives

\[  
x\_e\\le  
\\left\\lfloor\\frac{52+3X-2m}{5}\\right\\rfloor=4.  
\\tag{2}  
\]

The moment floor is

\[  
\\Lambda\_7(m)=m^2-43m+14+540-3\\left\\lfloor\\frac m2\\right\\rfloor,  
\]

so

\[  
\\Lambda\_7(25)=68,\\qquad  
\\Lambda\_7(26)=73.  
\\tag{3}  
\]

Two tiny knapsacks will recur:

\[  
P\\le10,\\quad F(d)\\le5\\text{ or }6  
\\quad\\Longrightarrow\\quad  
\\Psi\\le70,  
\\tag{4}  
\]

with equality uniquely at high degrees

\[  
(10,10),  
\]

and

\[  
P\\le11,\\quad F(d)\\le6  
\\quad\\Longrightarrow\\quad  
\\Psi\\le73,  
\\tag{5}  
\]

with the value (73) uniquely at

\[  
(10,10,6).  
\]

These are immediate from (1): the value function (c\\mapsto c(c+2)) is convex for collision costs (c=1,\\ldots ,5).

---

# **3\. Eliminate (m=26,\\ X=7)**

Certificate 0021’s complete partition sweep leaves three conservative shapes:

\[  
(2,2,2,1),\\qquad  
(2,2,1,1,1),\\qquad  
(1^7).  
\]

We kill all three.

---

## **3.1 The shape ((2,2,1,1,1))**

Let (A,B) be the two three-cell shared sets belonging to the (q=2) pairs.

If their supporting edge-pairs are disjoint, then

\[  
|A\\cap B|\\le1.  
\]

Otherwise four distinct hyperedges would share two cells, making all six pairs among them excessive, while this partition contains only five excessive pairs.

If the two (q=2) pairs are adjacent, then

\[  
|A\\cap B|\\le2.  
\]

An intersection of size at least three would force the closing pair to have (q\\ge2), producing a third (q=2) pair.

Consequently,

\[  
|A\\cup B|\\ge4.  
\]

Every cell of (A\\cup B) contributes at least (2) to (J), so

\[  
J\\ge8.  
\]

Here

\[  
R=2\\cdot6+3\\cdot2=18,  
\]

and therefore

\[  
P\\le R-J\\le10.  
\]

By (4),

\[  
\\Psi\\le70\<73=\\Lambda\_7(26).  
\]

So ((2,2,1,1,1)) is impossible.

---

## **3.2 The shape ((1^7))**

Let

\[  
U=\\bigcup\_{i=1}^7S\_i.  
\]

Every shared set has size two, and every cell of (U) contributes one to (J).

### **First, (|U|\\ne2)**

If (U={u,v}), all seven excessive pairs have shared set ({u,v}). If (t) hyperedges contain (u,v), then every pair of those hyperedges is excessive, so

\[  
\\binom t2=7,  
\]

which has no integer solution.

Hence

\[  
|U|\\ge3.  
\]

If (|U|\\ge4), then (J\\ge4), so (P\\le10), and (4) gives

\[  
\\Psi\\le70\<73.  
\]

It remains to consider (|U|=3). Then (J=3) and (P\\le11). To meet the moment floor, equality in (5) is necessary:

\[  
\\Psi=73,\\qquad \\text{high degrees }(10,10,6).  
\]

At (m=26,X=7), the exact moment identity may be written as

# **\[**

# **\\Psi-73**

15(n-36)+3(13-n\_2)+n\_4.  
\\tag{6}  
\]

All terms on the right are nonnegative. Thus (\\Psi=73) forces

\[  
n=36,\\qquad n\_2=13,\\qquad n\_4=0.  
\]

The three high cells have degree sum

\[  
10+10+6=26,  
\]

so the remaining (33) cells must have total degree

\[  
6m-26=156-26=130.  
\]

But thirteen of them have degree (2), none has degree (4), and the other twenty have degree at most (5). Their maximum possible total is

\[  
13\\cdot2+20\\cdot5=126\<130,  
\]

a contradiction.

Therefore ((1^7)) is impossible.

---

## **3.3 The shape ((2,2,2,1))**

Let (G\_2) be the graph whose vertices are hyperedges and whose three edges are the three (q=2) excessive pairs.

Because (x\_e\\le4), no hyperedge can lie in three (q=2) pairs. Thus

\[  
\\Delta(G\_2)\\le2.  
\]

We split into nontriangle and triangle cases.

### **Nontriangle case**

Let (A,B,C) be the three three-cell shared sets.

For edge-disjoint excessive pairs, the corresponding shared sets intersect in at most one cell.

For adjacent (q=2) pairs in a nontriangle, the corresponding shared sets intersect in at most two cells. An intersection of size three would make the closing pair another (q=2) edge.

Moreover, at most one pair among (A,B,C) can have intersection size two. Every such two-cell intersection forces its closing pair to be the unique (q=1) pair, and two distinct wedges have distinct closing pairs.

Therefore

\[  
|A\\cup B\\cup C|  
\\ge 9-(2+1+1)=5.  
\]

Every cell in this union contributes at least (2) to (J), so

\[  
J\\ge10.  
\]

Since (R=20),

\[  
P\\le10,  
\]

and hence

\[  
\\Psi\\le70\<73.  
\]

### **Triangle case**

Let the supporting hyperedges be (e\_1,e\_2,e\_3), and put

\[  
T=e\_1\\cap e\_2\\cap e\_3,\\qquad t=|T|.  
\]

The union of the three (q=2) shared sets has size

\[  
|U|=9-2t.  
\]

Let (S\_4) be the shared set of the (q=1) pair. As established in the correction above,

\[  
|S\_4\\cap U|\\le1.  
\]

The possible high cells and their collision caps are:

* (v\\in T\\setminus S\_4): (F(d(v))\\le4);  
* (v\\in T\\cap S\_4): (F(d(v))\\le5);  
* (v\\in S\_4\\cap(U\\setminus T)): (F(d(v))\\le1);  
* every other cell: (F(d(v))=0).

There is one further constraint. No edge outside (e\_1,e\_2,e\_3) can contain two cells of (T), since it would create additional excessive pairs with all three triangle edges. Hence the outside portions of the stars of the (T)-cells are disjoint.

Residual pairing applied to (T) gives at least

\[  
2(6-t)-1=11-2t  
\]

edges avoiding (T). Therefore

\[  
3+\\sum\_{v\\in T}(d(v)-3)  
\\le 26-(11-2t),  
\]

which simplifies to

\[  
\\sum\_{v\\in T} f(d(v))\\le12.  
\\tag{7}  
\]

The corrected finite optimization is now:

\[  
\\begin{array}{c|c|c}  
t&\\text{largest possible }\\Psi&\\text{maximizing }f\\text{-values}\\ \\hline  
0&3&(1)\\  
1&35&(5)\\  
2&59&(5,4)\\  
3&74&(5,4,3).  
\\end{array}  
\\tag{8}  
\]

Thus the only way to reach the required (73) is

\[  
\\Psi=74,\\qquad \\text{high degrees }(10,9,8).  
\]

From (6),

# **\[**

# **74-73**

15(n-36)+3(13-n\_2)+n\_4.  
\]

Hence

\[  
n=36,\\qquad n\_2=13,\\qquad n\_4=1.  
\]

The three high cells have total degree (27), so the remaining (33) cells must have degree sum

\[  
156-27=129.  
\]

But their maximum possible degree sum is

# **\[**

# **13\\cdot2+1\\cdot4+19\\cdot5**

125\<129.  
\]

Contradiction.

Therefore no (m=26,X=7) core exists.

---

# **4\. Eliminate (m=25,\\ X=7)**

Now

\[  
\\Lambda\_7(25)=68.  
\]

The (C3) cap remains (x\_e\\le4).

All partitions not discussed below have raw largest-pair-debit maximum at most (60), so they are already dead. The only shapes needing work are

\[  
(3,3,1),\\quad  
(3,2,2),\\quad  
(2,2,2,1),\\quad  
(2,2,1,1,1),\\quad  
(2,1^5),\\quad  
(1^7).  
\]

---

## **4.1 Dispose of the (q=3) shapes**

### **((3,3,1))**

The two (q=3) pairs cannot share a hyperedge because that edge would have

\[  
x\_e\\ge3+3=6\>4.  
\]

Their four-cell shared sets intersect in at most one cell; otherwise the four supporting hyperedges would generate six excessive pairs.

Their union therefore has at least seven cells, each contributing at least (3) to (J):

\[  
J\\ge21.  
\]

Since

\[  
R=12+12+2=26,  
\]

we get (P\\le5), and hence

\[  
\\Psi\\le24+3=27\<68.  
\]

### **((3,2,2))**

Let (A) be the four-cell (q=3) shared set and (B,C) the two three-cell (q=2) shared sets.

The (q=3) pair is edge-disjoint from each (q=2) pair because (3+2\>4). Consequently,

\[  
|A\\cap B|\\le1,\\qquad |A\\cap C|\\le1.  
\]

Also,

\[  
|B\\cap C|\\le2.  
\]

Each of (B,C) therefore contributes at least two cells outside (A), and their outside portions have union of size at least two. Thus

\[  
J\\ge4\\cdot3+2\\cdot2=16.  
\]

Here (R=24), so (P\\le8), and the cap is (F(d)\\le4). Therefore

\[  
\\Psi\\le2\\cdot24=48\<68.  
\]

Both (q=3) shapes die.

---

## **4.2 The exact (m=25) top census**

For every remaining shape except one (1^7) subcase, the largest possible value at or above (68) is

\[  
\\Psi=70,  
\]

uniquely with high degrees

\[  
(10,10).  
\\tag{9}  
\]

At (m=25,X=7),

# **\[**

# **\\Psi-68**

15(n-36)+3(12-n\_2)+n\_4.  
\\tag{10}  
\]

Substituting (\\Psi=70) gives

\[  
n=36,\\qquad n\_2=12,\\qquad n\_4=2.  
\]

There are two high cells, so (34) low cells remain. From their count and their total degree,

\[  
n\_3+n\_5=20,  
\]

\[  
2\\cdot12+4\\cdot2+3n\_3+5n\_5=130.  
\]

Therefore

\[  
\\boxed{(n\_2,n\_3,n\_4,n\_5)=(12,1,2,19).}  
\\tag{11}  
\]

In particular, the entire core contains **exactly one degree-three cell**.

We will repeatedly use this elementary profile fact:

> Four cells of degrees in ({2,3,4,5}), with at most one degree-two cell, whose degree sum is (13), must include a degree-three cell.

Indeed, without a (3), their smallest possible sum is

\[  
2+4+4+4=14.  
\]

---

## **4.3 The shape ((2,2,2,1))**

The triangle branch has corrected maximum

\[  
67\<68,  
\]

so only a nontriangle can survive.

The nontriangle union argument from (m=26) gives (J\\ge10). Thus the only numerical candidate is (9).

Equality forces:

* (J=10);  
* the union (U) of the three (q=2) shared sets has exactly five cells;  
* the (q=1) shared set lies inside (U);  
* the local (s)-values on (U) are

\[  
(7,7,2,2,2).  
\]

The two odd values (7) must be the two cells of the (q=1) shared set. Each such cell receives one unit from that pair and six units from the (q=2) pairs, so each lies in **all three** (q=2) shared sets.

But a nontriangle with three graph edges uses at least four supporting hyperedges. Those two cells would lie in every supporting hyperedge, so all six pairs among four of them would be excessive. The partition has only four excessive pairs.

Contradiction.

---

## **4.4 The shape ((2,2,1,1,1))**

We have (J\\ge8), so again the only candidate is (9). Equality requires (J=8).

The two (q=2) shared sets must therefore:

* be adjacent;  
* intersect in exactly two cells, say (T={u,v});  
* have union of size four.

Before the three (q=1) pairs are included, the weighted (s)-values on these four cells are

\[  
(4,4,2,2).  
\]

To support two degree-ten cells while exhausting exactly ten units of (P), the final values must be

\[  
(7,7,2,2).  
\]

Hence all three (q=1) shared sets must equal (T).

Write the adjacent (q=2) pairs as

\[  
{e,g},\\qquad{e,h}.  
\]

Then (e,g,h) all contain (T), and ({g,h}) is already one of the three (q=1) pairs. To obtain two additional (q=1) pairs with shared set (T), another hyperedge containing (T) is needed. But such an edge forms excessive pairs with **all three** of (e,g,h), producing three new pairs rather than two.

Contradiction.

---

## **4.5 The shape ((2,1,1,1,1,1))**

The three-cell (q=2) shared set contributes (6) to (J), so (J\\ge6). Again, (9) is the only numerical candidate, forcing (J=6).

Therefore every one of the five (q=1) shared sets lies inside the three-cell (q=2) shared set.

The base (s)-values are

\[  
(2,2,2).  
\]

Equality in (P+J\\le R) and the two degree-ten cells force the five (q=1) shared sets all to equal the same two-cell set

\[  
T={u,v}.  
\]

Every pair of hyperedges containing (T) is excessive. There is exactly one (q=2) pair and five (q=1) pairs, so if (r) hyperedges contain (T),

\[  
\\binom r2=6,  
\]

and therefore (r=4).

Call the four support edges (e,g,h,k), with ({e,g}) the unique (q=2) pair. Then

\[  
x\_h=x\_k=3.  
\]

The two high cells (u,v) have total degree (20). By the established edge-sum identity

\[  
\\sum\_{z\\in h}d(z)=m+5+x\_h,  
\]

the other four cells of (h) have degree sum

\[  
25+5+3-20=13.  
\]

The same holds for (k).

Those two four-cell sets are disjoint: (h\\cap k=T), and each meets (e,g) only in (T). By the profile fact, both (h) and (k) require a degree-three ordinary cell. That requires at least two degree-three cells, contradicting (11), which allows exactly one.

So this shape dies.

---

## **4.6 The shape ((1^7))**

Again let (U) be the union of the seven two-cell shared sets. We already know (|U|\\ge3).

The only knapsack possibilities with (\\Psi\\ge68) are

\[  
(10,10,6)\\quad(\\Psi=73)  
\]

and

\[  
(10,10)\\quad(\\Psi=70).  
\]

### **Candidate ((10,10,6))**

Its collision cost is (11), so (J\\le3). Hence (|U|=3).

For each cell-pair ({a,b}\\subseteq U), the hyperedges containing (a,b) form a clique of excessive pairs. Therefore the number of excessive pairs having shared set ({a,b}) is a triangular number

\[  
\\binom{r\_{ab}}2.  
\]

The positive triangular numbers at most seven are

\[  
1,\\ 3,\\ 6\.  
\]

With three possible cell-pairs and total seven, the only decompositions are

\[  
6+1+0  
\\quad\\text{or}\\quad  
3+3+1.  
\]

Their cell-incidence (s)-sequences are respectively

\[  
(7,6,1)  
\\quad\\text{and}\\quad  
(6,4,4).  
\]

After subtracting (q\_{\\max}=1), the available local capacities are

\[  
(6,5,0)  
\\quad\\text{or}\\quad  
(5,3,3).  
\]

Neither can support collision costs

\[  
(5,5,1)  
\]

for degrees ((10,10,6)).

So (\\Psi=73) is impossible.

### **Candidate ((10,10))**

Now (J\\le4), so (|U|=3) or (4).

For (|U|=3), the only triangular pattern supporting two cells of local capacity at least five is (6+1).

For (|U|=4), equality requires the (s)-sequence

\[  
(6,6,1,1).  
\]

The two incidence-one cells must be paired with one another; otherwise, after their two incidences are removed, the remaining multiplicity on the pair of high cells would have to be (5), which is not triangular. Thus this case is also a disjoint (6+1) pattern.

In either case, six of the seven excessive pairs form a (K\_4) on four hyperedges all sharing the two high cells (T={u,v}).

Every support edge has (x\_e=3), except possibly one edge that participates in the seventh excessive pair. Thus at least three support edges have (x\_e=3).

For each such edge, its four ordinary cells have degree sum

\[  
25+5+3-20=13.  
\]

Ordinary cells belonging to distinct support edges are disjoint, because every pair of support edges intersects exactly in (T). Each of the at least three support edges therefore needs a distinct degree-three cell.

That contradicts the exact census (n\_3=1).

Thus ((1^7)) is impossible.

---

# **5\. New conclusion**

Both top rungs of the old (X=7) frontier are empty:

\[  
m=25,\\ X=7\\quad\\text{impossible},  
\]

\[  
m=26,\\ X=7\\quad\\text{impossible}.  
\]

Hence:

\[  
\\boxed{X=7\\Longrightarrow m\\le24.}  
\]

Once certified, the clean staircase becomes

\[  
\\boxed{  
\\begin{aligned}  
22\\le m\\le24&\\Longrightarrow X\\ge7,\\  
25\\le m\\le28&\\Longrightarrow X\\ge8,\\  
m=29&\\Longrightarrow X\\ge9,\\  
m\\ge30&\\Longrightarrow X\\ge10.  
\\end{aligned}}  
\]

The live minimum-excess frontier shrinks from five edge counts to three:

\[  
\\boxed{X=7,\\qquad m\\in{22,23,24}.}  
\]

---

# **6\. Is the OpenAI attachment useful?**

Yes—but as a **proof-design document**, not as a source to cite for a theorem.

Its abstract explicitly says that it is an AI reconstruction of how arguments emerged from original chains of thought and resulting papers, emphasizing changes of perspective and failed approaches rather than reproducing full proofs.

The most transferable idea is actually in **Chapter 11**, not the large-scale extremal estimates themselves:

> When two local witnesses may overlap, do not assume them disjoint. Include all admissible quotients of the combined template.

That is almost exactly what the Cofferdam frontier now needs. The new arguments above treat:

* adjacent versus edge-disjoint excessive pairs;  
* forced closing pairs;  
* shared-set unions;  
* support cliques;  
* all overlap patterns that could lower (J).

The (m=25) proof is essentially a tiny admissible-quotient argument carried out by hand.

Chapter 10 also contains a useful strategic analogy. Its Ramsey construction succeeds only after strengthening “triangle-free” to a richer invariant that survives recursive gluing. Cofferdam’s corresponding strengthening was retaining

\[  
J=\\sum\_v q\_{\\max}(v)  
\]

over **all** vertices rather than throwing it away or restricting it to high cells. That stronger invariant is what made 0021 and the new eliminations possible.

Chapter 12’s entropy/Hamming machinery is much less relevant at the present frontier. We are dealing with seven units of excess and tiny quotient types; entropy is likely the wrong scale.

I would not import any of the attachment’s claimed new extremal theorems into Cofferdam’s trust chain. The attachment is a secondary discovery narrative, and it does not itself provide an unambiguous bibliographic pointer to the new full-paper proofs. Its local methodological ideas are useful independently of whether those very recent results survive review.

---

# **7\. Certificate design and the next target**

The natural certificate title is:

> **0022 — shared-set quotients: (X=7\\Rightarrow m\\le24)**

It should contain four independent layers:

1. **Repair `tri_max`.** Permit one possible degree-six cell in (S\_4\\cap(U\\setminus T)); assert (|S\_4\\cap U|\\le1); reproduce corrected maxima (67,74,83).  
2. **Re-enumerate every partition of seven.** Do not merely import the three (m=26) survivors. Print every raw, (J)-debit, quotient, census, and profile maximum at (m=25,26).  
3. **Encode shared-set quotients explicitly.** Each state should record:  
   * the excess graph on supporting hyperedges;  
   * shared-cell membership signatures;  
   * forced closing excessive pairs;  
   * (J);  
   * local (s-q\_{\\max}) capacities.  
4. **Add teeth.**  
   * Allow two degree-two cells on a support edge: the sum-(13) profile obstruction should reopen.  
   * Permit an arbitrary multiplicity (5) for one shared cell-pair: the ((1^7)), ((10,10,6)) obstruction should reopen.  
   * Raise the (C3) edge cap from (4) to (5): the (q=3) edge-disjointness arguments should reopen.  
   * Delete the optional outside triangle high cell: a dedicated structural test should fail even though the final numerical maximum happens not to move.

After that, the first (m=24) target is exceptionally concrete. In the (q=2) triangle branch of ((2,2,2,1)), the corrected optimizer ties the moment floor exactly:

\[  
\\Psi=\\Lambda\_7(24)=62  
\]

with high degrees

\[  
(10,9,6).  
\]

The exact moment identity then forces the unique census

\[  
n=36,\\qquad  
(n\_2,n\_3,n\_4,n\_5)=(12,5,0,16).  
\]

That is the next zero-margin template to attack with the quotient/profile engine.

## **Bottom line**

* **Current certified project:** sound as far as this audit found.  
* **Major errors:** none found in the claim chain.  
* **Minor error:** the (X=7) triangle preview omits a possible outside degree-six cell; repaired maxima are unchanged.  
* **New progress:** a certificate-ready argument should improve

\[  
X=7\\Rightarrow m\\le26  
\]

to

\[  
\\boxed{X=7\\Rightarrow m\\le24}.  
\]

* **Next live battlefield:** (X=7) on (m=22,23,24), beginning with the exact ((m,\\pi,\\mathbf d)=(24,(2,2,2,1),(10,9,6))) triangle tie.

