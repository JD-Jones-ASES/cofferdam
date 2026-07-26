# raw run data

Scripts and logs exactly as run, kept so a result can be traced back to the run
that produced it. Nothing here is a certificate; nothing here is load-bearing.

**`cache.pkl` files are deliberately not tracked.** They are regenerable memo
caches (the chain2 run rebuilds its own), they are large, and a pickle executes
arbitrary code when loaded — so handing one to another reader is both unverifiable
and unsafe. The scripts and logs that produced them are here; the conclusions are
in `notebook/` and the certificates.
