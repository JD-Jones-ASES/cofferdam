# **Cofferdam outside audit — Turn 16 proposal**

## **Executive verdict**

**I agree with the mathematical conclusions currently certified through 0019\.** I found no theorem-breaking defect in

\[  
22\\le m(K)\\le456,\\qquad  
X(K)\\ge5,\\qquad  
X(K)=5\\Longrightarrow m(K)\\le26.  
\]

Cofferdam correctly absorbed the previous turn as Certificate 0019, including the new defect-hub and star-collision inequalities. The certificate’s stated claims and dependency split are accurately reflected in its NOTES.

I did, however, find one genuine correction to the turn-15 record:

> **The received proof’s flooring step was not circular.**

That does not weaken 0019\. Its replacement argument, (DH), is valid and stronger. But the repo currently records a nonexistent logical defect in the outside proof.

More importantly, the mathematics pushes substantially farther.

---

# **Proposed new standing**

Let (K) be an edge-critical counterexample core to intersecting Ryser at (r=6), with (m) edges and pair-excess (X). Then:

\[  
\\boxed{X\\ge6\\quad\\text{on every rung of }\[22,456\].}  
\]

Moreover,

\[  
\\boxed{  
\\begin{aligned}  
m\\ge27&\\Longrightarrow X\\ge7,\\  
m\\ge29&\\Longrightarrow X\\ge8,\\  
m\\ge30&\\Longrightarrow X\\ge9,\\  
m\\ge32&\\Longrightarrow X\\ge10.  
\\end{aligned}}  
\]

There is also a new window-wide quadratic growth law. If

\[  
H=\\bigl|{v:d(v)\\ge6}\\bigr|  
\]

and

\[  
\\Sigma\_5=\\sum\_v r\_v(5-r\_v),  
\\qquad r\_v\\equiv d(v)\\pmod 5,\\quad 0\\le r\_v\<5,  
\]

then

\[  
\\boxed{m(m-25)+10H+\\Sigma\_5\\le38X.}  
\]

In particular,

\[  
\\boxed{X\\ge  
\\left\\lceil\\frac{m(m-25)}{38}\\right\\rceil.}  
\]

At the current ceiling (m=456), this gives

\[  
\\boxed{X\\ge5172,}  
\]

against Certificate 0017’s present (X\\ge2259). Certificate 0017 currently records the latter as its ceiling-rung second-moment bound.

These results are not yet GREEN under Cofferdam’s law. I regard the proofs below as complete, but they should enter as statements plus mechanisms, be blindly re-derived, and receive a hostile certificate audit.

---

# **1\. Correction: the alleged (16/3) circularity is not real**

Certificate 0019 says the received proof argued

\[  
\\sum\_{v\\in e}w(d(v))\\le\\frac{16}{3},  
\]

then floored the left side to (5), and that doing so circularly presupposed a degree cap. The repository therefore presents (DH) as a repair of that step.

But

\[  
w(d)=\\Phi(d-1,5)  
\]

is an integer for every integer degree (d), with no degree cap required. The certificate itself defines (\\Phi) by an integer closed form and computes the integral table

\[  
w(2),\\ldots,w(11)=0,0,0,0,0,1,2,3,4,5.  
\]

Therefore

\[  
\\sum\_{v\\in e}w(d(v))\\in\\mathbb Z  
\]

automatically, and

\[  
\\sum\_{v\\in e}w(d(v))\\le\\frac{16}{3}  
\\quad\\Longrightarrow\\quad  
\\sum\_{v\\in e}w(d(v))\\le5  
\]

is valid. Since

\[  
w(11)=5,\\qquad w(12)=7,  
\]

this indeed forces every degree on that edge to be at most (11).

There could have been a **separate scope issue** if a bound proved only on one selected edge was then quoted globally. But the recorded objection—“integrality presupposes the cap being derived”—is false.

## **Recommended correction**

The following should be reworded:

* Certificate 0019 NOTES, “The (\\Delta\\le5+X) repair.”  
* Certificate 0019’s verify.py honesty note.  
* Turn-15 notebook.  
* PLAN’s D-037 lesson.  
* DECISIONS D-037.  
* Any report saying two refuters found a real circularity.

The accurate record is:

> The received flooring step was valid. The in-house (DH) argument independently produced the stronger global bound (\\Delta\\le5+X), eliminating any possible edge-to-global scope concern and materially strengthening the proof.

D-037 remains a good intake protocol. Its motivating example should not falsely describe a valid integer-flooring argument as circular.

---

# **2\. A stronger star-collision inequality**

Certificate 0019 proves

\[  
D:=\\sum\_v(d(v)-5)*\+*  
*\\le*  
*R:=\\sum*{{e,f}}q\_{ef}(q\_{ef}+1),  
\]

where

\[  
q\_{ef}=|e\\cap f|-1.  
\]

Its proof uses the five available cells of an avoiding edge and the collision count among edges through a fixed vertex.

The same argument has a stronger convex form.

## **Definition**

Put

\[  
F(d):=\\Phi(d,5).  
\]

For a vertex (z), define its star-excess

\[  
s(z):=\\sum\_{{e,g}\\subseteq E(z)}q\_{eg}.  
\]

## **Lemma 2.1 — balanced defect-hub inequality**

For every vertex (z),

\[  
\\boxed{F(d(z))\\le s(z).}  
\\tag{BDH}  
\]

### **Proof**

Choose an edge (f) avoiding (z), possible because a core with (\\tau=6) has no universal vertex.

For each (u\\in f), put

\[  
r\_u=\\bigl|{e\\in E(z):u\\in e}\\bigr|.  
\]

Every edge through (z) meets (f), so

\[  
\\sum\_{u\\in f}r\_u\\ge d(z).  
\]

The cell of (f) in (z)’s own part occurs on no (z)-edge. Thus at most five of the six (r\_u) are positive. Balanced convexity gives

\[  
\\sum\_{u\\in f}\\binom{r\_u}{2}  
\\ge \\Phi\!\\left(\\sum r\_u,5\\right)  
\\ge \\Phi(d(z),5).  
\]

On the other hand,

# **\[**

# **\\sum\_{u\\in f}\\binom{r\_u}{2}**

\\sum\_{{e,g}\\subseteq E(z)}|e\\cap g\\cap f|.  
\]

Because (z\\in e\\cap g) but (z\\notin f),

\[  
|e\\cap g\\cap f|  
\\le |e\\cap g|-1  
\=q\_{eg}.  
\]

Hence

\[  
F(d(z))\\le s(z).  
\\qquad\\square  
\]

This is the balanced-split strengthening that the turn-15 notebook had already identified as a promising (S1^+/S1^{++}) direction.

---

# **3\. Strictness from (\\tau=6)**

The previous inequality cannot attain equality at a high-degree vertex.

## **Lemma 3.1 — strict star-collision**

If (d(z)\\ge6), then

\[  
\\boxed{F(d(z))+1\\le s(z).}  
\\tag{SSC}  
\]

More precisely, if

\[  
q\_{\\max}(z)  
:=  
\\max\_{{e,g}\\subseteq E(z)}q\_{eg},  
\]

then

\[  
\\boxed{F(d(z))+q\_{\\max}(z)\\le s(z).}  
\\tag{SSC(^+)}  
\]

### **Proof**

Let

\[  
\\delta=s(z)-F(d(z)).  
\]

Choose an excessive pair (e,g\\in E(z)) with excess (q=q\_{eg}\>0), and let

\[  
U=(e\\cap g)\\setminus{z},  
\\qquad |U|=q.  
\]

For any edge (f) avoiding (z), write

# **\[**

# **C\_f**

\\sum\_{{a,b}\\subseteq E(z)}|a\\cap b\\cap f|.  
\]

The proof of (BDH) gives

\[  
F(d(z))\\le C\_f\\le s(z),  
\]

and therefore

\[  
s(z)-C\_f\\le\\delta.  
\]

Term by term,

\[  
q\_{ab}-|a\\cap b\\cap f|\\ge0.  
\]

Consequently, for the selected pair (e,g),

\[  
q-|U\\cap f|\\le\\delta.  
\]

If (\\delta\<q), then every edge (f) avoiding (z) meets (U). Every edge containing (z) is met by (z). Therefore

\[  
{z}\\cup U  
\]

is a cover of size (q+1\\le5), contradicting (\\tau(K)=6).

Thus (\\delta\\ge q) for every excessive pair through (z), and hence

\[  
s(z)-F(d(z))\\ge q\_{\\max}(z).  
\\qquad\\square  
\]

Since (F(d)\>0) exactly when (d\\ge6), summing the weaker strict form gives:

## **Corollary 3.2 — strict global star-collision**

Define

\[  
P=\\sum\_vF(d(v)),  
\\qquad  
H=\\bigl|{v:d(v)\\ge6}\\bigr|.  
\]

Then

\[  
\\boxed{P+H\\le R.}  
\\tag{SG}  
\]

Indeed,

# **\[**

# **\\sum\_v s(v)**

# **\\sum\_{{e,f}}q\_{ef}|e\\cap f|**

# **\\sum\_{{e,f}}q\_{ef}(q\_{ef}+1)**

R.  
\]

This extra (+H) is the decisive new unit. It kills the entire (X=5) field.

---

# **4\. A five-set cover obstruction: (q\\le3)**

## **Lemma 4.1**

Distinct edges of a critical core satisfy

\[  
|e\\cap f|\\le4,  
\\qquad\\text{equivalently}\\qquad q\_{ef}\\le3.  
\]

### **Proof**

Suppose (|e\\cap f|=5), and put

\[  
S=e\\cap f.  
\]

Any edge (g) avoiding (S) must still meet both (e) and (f). The two vertices in

\[  
e\\setminus S,\\qquad f\\setminus S  
\]

lie in the same part and are distinct. Thus (g) would have to contain both of them, impossible in a partite edge.

Therefore every edge meets (S), making (S) a (5)-cover, contrary to (\\tau=6). ∎

It follows that

\[  
q(q+1)\\le4q  
\]

for every excessive pair, and hence

\[  
\\boxed{R\\le4X.}  
\\tag{R4}  
\]

---

# **5\. The new quadratic growth law**

Write

\[  
d=5a+r,\\qquad 0\\le r\<5.  
\]

The balanced-split value is

\[  
F(d)=5\\binom a2+ra.  
\]

A direct calculation gives the exact identity

\[  
\\boxed{5d+10F(d)-d^2=r(5-r).}  
\\tag{I}  
\]

Let

\[  
\\Sigma\_5=\\sum\_v r\_v(5-r\_v).  
\]

Using the moment identities

\[  
\\sum\_vd(v)=6m,  
\]

\[  
\\sum\_vd(v)^2=m^2+5m+2X,  
\]

identity (I) yields

# **\[**

# **10P**

m^2-25m+2X+\\Sigma\_5.  
\]

Now apply the strict global bound (P+H\\le R\\le4X):

\[  
m^2-25m+2X+\\Sigma\_5+10H  
\\le40X.  
\]

Therefore

\[  
\\boxed{m(m-25)+\\Sigma\_5+10H\\le38X.}  
\\tag{Q}  
\]

In particular,

\[  
\\boxed{  
X\\ge  
\\left\\lceil\\frac{m(m-25)}{38}\\right\\rceil.  
}  
\\tag{Q(\_0)}  
\]

## **Numerical comparison**

| (m) | Current published profile in the repo | New bound (Q\_0) |
| ----- | ----- | ----- |
| 38 | (X\\ge10) | (X\\ge13) |
| 108 | (X\\ge100) | (X\\ge236) |
| 309 | (X\\ge1000) | (X\\ge2310) |
| 456 | (X\\ge2259) | (\\boxed{X\\ge5172}) |

The current public summary records the old (X\\ge2259) ceiling value and its lower-rung milestones.

This new law consumes no field enumeration, no solver, and no private-cover corner inequality. It uses only:

* intersectingness;  
* six-partiteness;  
* (\\tau=6);  
* the two degree moments;  
* balanced convexity.

---

# **6\. The (X=5) layer is empty**

Certificate 0019 currently proves that (X=5) can occur only for

\[  
m\\in{22,23,24,25,26}.  
\]

The current PLAN therefore names those five rungs as the principal frontier.

We can eliminate all five at once.

## **6.1 The possible excess partitions**

Since (q\\le3), the positive (q)-values partitioning (X=5) are:

\[  
(1,1,1,1,1),  
\]

\[  
(2,1,1,1),  
\]

\[  
(2,2,1),  
\]

\[  
(3,1,1),  
\]

\[  
(3,2).  
\]

For each partition define:

* (t): the least possible value of (\\max\_ex\_e);  
* (R=\\sum q(q+1)).

| excess partition | (t) | (R) |
| ----- | ----- | ----- |
| (1+1+1+1+1) | 1 | 10 |
| (2+1+1+1) | 2 | 12 |
| (2+2+1) | 2 | 14 |
| (3+1+1) | 3 | 16 |
| (3+2) | 3 | 18 |

Choosing an edge (f) with (x\_f\\ge t), (DH) gives

\[  
d(z)\\le10-t\\qquad(z\\notin f).  
\]

The certified (4/3) corner at (X=5) gives

\[  
\\sum\_{v\\in f}w(d(v))  
\\le  
\\left\\lfloor\\frac43(5-t)\\right\\rfloor,  
\]

namely budgets (5,4,4,2,2) in the five rows. Certificate 0017 certifies the (4/3) corner at (X=5), while C3 supplies the edge-excess restrictions used throughout 0019\.

The strict local inequality gives

\[  
F(d(v))+1\\le s(v)\\le X=5  
\]

for (d(v)\\ge6). Since

\[  
F(9)=4,\\qquad F(10)=5,  
\]

we obtain the global cap

\[  
\\boxed{\\Delta\\le9.}  
\]

## **6.2 The exact degree census**

For each row and each (m=22,\\ldots,26), minimize

\[  
S:=\\sum\_d\\bigl(F(d)+\\mathbf1\_{d\\ge6}\\bigr)n\_d  
\]

over integer (n\_2,\\ldots,n\_9) satisfying

\[  
\\sum\_dn\_d\\ge36,  
\]

\[  
n\_2\\le\\left\\lfloor\\frac m2\\right\\rfloor,  
\]

\[  
\\sum\_ddn\_d=6m,  
\]

\[  
\\sum\_dd^2n\_d=m^2+5m+10,  
\]

and the relevant off-(f)/on-(f) degree budget above.

This is a tiny exact recursion over degrees (9,8,\\ldots,3), solving for (n\_2) at the leaf. No solver is involved.

The exact minima are:

| partition | (R) | (m=22) | 23 | 24 | 25 | 26 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| (1^5) | 10 | 13 | 14 | 14 | 15 | 15 |
| (2+1^3) | 12 | 15 | 15 | 16 | 17 | 19 |
| (2+2+1) | 14 | 15 | 15 | 16 | 17 | 19 |
| (3+1+1) | 16 | 19 | 21 | 21 | 24 | 25 |
| (3+2) | 18 | 19 | 21 | 21 | 24 | 25 |

Every entry is strictly larger than its row’s (R), contradicting

\[  
S\\le R.  
\]

The thinnest cells close by one unit:

\[  
m=22,\\quad 2+2+1:\\qquad 15\>14,  
\]

\[  
m=22,\\quad 3+2:\\qquad 19\>18.  
\]

Therefore:

# **Theorem A**

\[  
\\boxed{X\\ge6\\text{ for every critical core.}}  
\]

The current X=5 field is empty. The PLAN’s first-ranked campaign is finished before its weighted-graph shape census begins.

This argument does consume the degree-two cap. Removing (n\_2\\le\\lfloor m/2\\rfloor) reopens several low-rung cells, so 0008 remains explicitly load-bearing.

---

# **7\. The first four steps of the new excess staircase**

The same strict inequality gives more.

The certified per-edge linear law is

\[  
2m+5x\_e\\le52+3X.  
\\tag{C3}  
\]

Since (\\sum\_ex\_e=2X\>0), C3 makes each fixed-(X) campaign finite.

## **7.1 Arithmetic elimination above the exceptional rung**

Applying the same exact degree census with the (3/2) corner gives:

| (X) | rungs killed arithmetically | maximum (R) there | minimum (S) at first rung |
| ----- | ----- | ----- | ----- |
| 6 | (m=28,\\ldots,32) | 18 | 21 |
| 7 | (m=30,\\ldots,34) | 20 | 26 |
| 8 | (m=31,\\ldots,35) | 24 | 30 |
| 9 | (m=33,\\ldots,37) | 26 | 38 |

At those rungs C3 forces (\\max x\_e\\le2), hence all (q\\le2), producing the displayed maxima of (R). Every row contradicts (S\\le R).

One exceptional lower rung remains for each (X).

## **7.2 The exceptional weighted matchings**

The exact arithmetic leaves only:

| (X) | rung | only remaining excess partition |
| ----- | ----- | ----- |
| 6 | 27 | (3+3) |
| 7 | 29 | (3+3+1) |
| 8 | 30 | (3+3+2) |
| 9 | 32 | (3+3+3) |

C3 forces the listed weighted pairs to be edge-disjoint. Let their shared vertex sets be (A,B,C), as applicable.

Two different shared sets intersect in at most one vertex: two common vertices would make an unlisted cross-pair excessive.

By (SSC(^+)), a high-degree vertex cannot lie in only one shared set. If it did, then

\[  
s(v)=q\_{\\max}(v),  
\]

forcing (F(d(v))\\le0), contrary to (d(v)\\ge6).

Therefore:

* with two shared sets, at most one high-degree vertex exists;  
* with three shared sets, at most three high-degree vertices exist.

The same local inequality bounds their degrees.

| (X,m) | (H\_{\\max}) | (\\Delta\_{\\max}) |
| ----- | ----- | ----- |
| (6,27) | 1 | 8 |
| (7,29) | 3 | 9 |
| (8,30) | 3 | 10 |
| (9,32) | 3 | 10 |

For (2\\le d\\le5),

\[  
d^2\\le7d-10.  
\]

For (d\\ge6),

\[  
d^2-(7d-10)=(d-2)(d-5).  
\]

Thus the maximum possible second moments under the preceding high-degree caps are:

| (X,m) | required (\\sum d^2=m^2+5m+2X) | maximum allowed |
| ----- | ----- | ----- |
| (6,27) | 876 | (7(162)-360+18=792) |
| (7,29) | 1000 | (7(174)-360+3(28)=942) |
| (8,30) | 1066 | (7(180)-360+3(40)=1020) |
| (9,32) | 1202 | (7(192)-360+3(40)=1104) |

Every exceptional shape is impossible.

Therefore:

# **Theorem B — the new staircase**

\[  
\\boxed{X=6\\Longrightarrow m\\le26,}  
\]

\[  
\\boxed{X=7\\Longrightarrow m\\le28,}  
\]

\[  
\\boxed{X=8\\Longrightarrow m\\le29,}  
\]

\[  
\\boxed{X=9\\Longrightarrow m\\le31.}  
\]

Equivalently,

\[  
\\boxed{  
\\begin{aligned}  
m\\ge27&\\Longrightarrow X\\ge7,\\  
m\\ge29&\\Longrightarrow X\\ge8,\\  
m\\ge30&\\Longrightarrow X\\ge9,\\  
m\\ge32&\\Longrightarrow X\\ge10.  
\\end{aligned}}  
\]

---

# **8\. Minor Certificate 0019 clarification**

Certificate 0019’s prose says

\[  
\\Phi(d-1,5-b)\\ge\\Phi(d-1,5)  
\]

for every (b\\ge0), while its actual check correctly runs only over (b=0,\\ldots,4).

At (b=5), the left side would formally have zero classes. This is not a mathematical gap because the inherited covering branch says:

\[  
b\_i=5\\Longrightarrow d\_i=1,  
\]

and therefore the corresponding weight is zero. But the sentence should say:

> For (0\\le b\_i\\le4), use monotonicity. If (b\_i=5), covering forces (d\_i=1), so the term and its (w)-relaxation are both zero.

This is a minor scope correction only.

---

# **9\. Recommended Certificate 0020**

A natural title is:

> **Certificate 0020 — strict star-collision: (X\\ge6) everywhere, the low-excess staircase, and the (m(m-25)/38) growth law**

## **Suggested claim rows**

| claim | proposed label |
| ----- | ----- |
| (\\lambda(e,f)\\le4), hence (q\\le3) and (R\\le4X) | PROVEN-BY-CERTIFICATE |
| (F(d(v))\\le s(v)) | PROVEN-BY-CERTIFICATE |
| (F(d(v))+q\_{\\max}(v)\\le s(v)) | PROVEN-BY-CERTIFICATE |
| (P+H\\le R) | PROVEN-BY-CERTIFICATE |
| (m(m-25)+\\Sigma\_5+10H\\le38X) | PROVEN-BY-CERTIFICATE |
| (X\\ge6) window-wide | PROVEN-BY-CERTIFICATE |
| (X=6,7,8,9) have ceilings (26,28,29,31) | PROVEN-BY-CERTIFICATE |

## **Suggested finite checks**

1. Exhaust (F(d)=\\Phi(d,5)) and the residue identity.  
2. Enact the balanced defect-hub inequality on a diverse small corpus.  
3. Include a (\\tau=2) control where equality is possible, proving (\\tau\\ge3) is load-bearing for strictness.  
4. Exhaust the five (X=5) partition rows and reproduce the (5\\times5) minimum table.  
5. Exhaust the four staircase arithmetic scans.  
6. Enumerate the four exceptional weighted matchings and verify their shared-set intersection caps.  
7. Recompute every moment upper bound rather than hard-coding it.

## **Mandatory mutants**

* Remove the (+H) term: the (X=5) field must reopen.  
* Replace five fibres by six: balanced defect-hub must weaken.  
* Permit (q=4): the five-cover control must fail.  
* Relax (D2) by one: low-rung (X=5) configurations should revive.  
* Drop the (q\_{\\max}) term: the exceptional matching argument must lose its high-vertex confinement.  
* Replace ceiling by floor in the one-unit (X=5) cells.  
* Mutate (r(5-r)) to (r(4-r)): the quadratic identity must redden.

## **Dependency ledger**

The new certificate should consume:

* 0005: minimum degree and active vertices;  
* 0008: degree-two cap, for the (X=5) elimination;  
* 0013: critical-core scope and (\\tau=6);  
* 0017: C3 and the (4/3)/(3/2) corners;  
* 0019: DH may either be consumed or re-derived in stronger balanced form.

It need not consume:

* 0018;  
* 0017 C2;  
* the old X=3/X=4 shape censuses;  
* a solver.

The quadratic law itself has a considerably smaller ledger than the staircase: it needs neither D2 nor the private-cover corner machinery.

---

# **10\. New frontier**

The current PLAN ranks (X=5) on (m=22,\\ldots,26), followed by measurement of the (X=6) horizon. Both entries are now superseded.

The new low-end frontier is:

\[  
\\boxed{X=6\\text{ on }m\\in{22,23,24,25,26}.}  
\]

A preliminary shape campaign indicates that this field is already highly compressed, but I would not ingest those detailed counts before Certificate 0020 establishes the strict inequality cleanly. The correct order is:

1. certify strict star-collision;  
2. certify (X\\ge6);  
3. certify the staircase and quadratic law;  
4. only then enumerate (X=6) on the five remaining rungs.

---

# **Final assessment**

**Current project state:** sound.

**Major correction:** the turn-15 record falsely calls an integral flooring step circular. Correct the provenance narrative; no theorem changes.

**New principal theorem:**

\[  
\\boxed{X\\ge6\\text{ for every possible critical core}.}  
\]

**New low-end profile:**

\[  
\\boxed{  
m\\ge27\\Rightarrow X\\ge7,\\quad  
m\\ge29\\Rightarrow X\\ge8,\\quad  
m\\ge30\\Rightarrow X\\ge9,\\quad  
m\\ge32\\Rightarrow X\\ge10.  
}  
\]

**New global growth law:**

\[  
\\boxed{m(m-25)+10H+\\Sigma\_5\\le38X.}  
\]

**New ceiling-rung requirement:**

\[  
\\boxed{m=456\\Longrightarrow X\\ge5172.}  
\]

The project’s next turn should not begin with an (X=5) shape census. It should begin by trying to break strict star-collision. If that lemma survives, the whole (X=5) campaign disappears and the existing excess-growth profile is more than doubled at the top.