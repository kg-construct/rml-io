## Overview {#overview}

*This section is non-normative.*

This document specifies *Input Logical Source* and *Logical Target*,
Input Logical Source is a description
for specifying how a data source should be accessed.
An Input Logical Source description is not limited to a specific Source
which allows to access any type of Source and provides a reference formulation
to refer to data inside the Source.

Logical Target is
a description for defining how a generated
RDF [[RDF-Concepts]]
knowledge graph must be exported.
A Logical Target description is not tailored towards a specific Target
which allows to export the generated RDF triples to any type of Target
and provides fine-grained control over where each RDF triple is exported to.

Input Logical Source and Logical Target leverage
the access descriptions of data access
such as DCAT [[DCAT]], SD [[SD]], etc.

In this document, examples assume
the following namespace prefix bindings unless otherwise stated:

| Prefix    | Namespace                                           |
| --------- | --------------------------------------------------- |
| `rml`     | http://w3id.org/rml/                                |
| `formats` | http://www.w3.org/ns/formats/                       |
| `sd`      | http://www.w3.org/ns/sparql-service-description#    |
| `dcat`    | http://www.w3.org/ns/dcat#                          |
| `td`      | https://www.w3.org/2019/wot/td#                     |
| `hctl`    | https://www.w3.org/2019/wot/hypermedia#             |
| `htv`     | http://www.w3.org/2011/http#                        |
| `d2rq`    | http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1# |
| `wotsec`  | https://www.w3.org/2019/wot/security#               |
| `idsa`    | https://w3id.org/idsa/core/                         |

The examples are contained in pink colored boxes:

<pre class="ex-source">
# This box contains the example's Input Logical Source description.
</pre>

<pre class="ex-target">
# This box contains the example's Logical Target description.
</pre>
