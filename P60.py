from infgeoax import primes_million, is_prime
from itertools import product

primes_set = set(primes_million(1000000))

print len(primes_set)

def parts(n):
    nstr = "%d" % n
    r = []
    for i in range(1, len(nstr)):
        p1 = int(nstr[:i])
        p2 = int(nstr[i:])
        if p1 in primes_set and p2 in primes_set and int("%d%d"%(p1,p2))==n and int("%d%d"%(p2,p1)) in primes_set:
            # a valid partition, p1, p2 are both primes and they "fit" back together, and the inversed concatenation yields a prime too.
            r.append((n, p1, p2))
    return r

nodes = {}
def add_edge(p1, p2):
    if not p1 in nodes:
        nodes[p1] = set([ p2 ])
    elif not p2 in nodes[p1]:
        nodes[p1].add(p2)

for p in primes_set:
    for p,p1,p2 in parts(p):
        add_edge(p1, p2)

eid = 0
xedges = []
xnodes = []
for k, v in nodes.items():
    xnodes.append("<node id=\"%d\" label=\"%d\"/>" % (k, k))
    for n in v:
        xedges.append("<edge id=\"%d\" source=\"%d\" target=\"%d\"/>" % (eid, k, n))
        eid += 1

gexf = ["""<?xml version="1.0" encoding="UTF-8"?>
<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">
    <meta lastmodifieddate="2009-03-20">
        <creator>Gexf.net</creator>
        <description>A hello world! file</description>
    </meta>
    <graph mode="static" defaultedgetype="directed">
    <nodes>"""]
for node in xnodes:
    gexf.append(node)
gexf.append("</nodes><edges>")
for edge in xedges:
    gexf.append(edge)
gexf.append("</edges></graph></gexf>")
with open('C:/primes.gexf', 'w') as f:
    f.write("\n".join(gexf))
