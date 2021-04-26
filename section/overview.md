## Overview {#overview}

*This section is non-normative.*

This document specifies *Target*, 
a description for defining how a generated 
RDF [[RDF-Concepts]]
knowledge graph must be exported. 
A Target description is not tailored towards a specific Target 
which allows to export the generated RDF triples to any type of Target. 
Target leverages the access descriptions of data access 
such as DCAT [[DCAT]], VoID [[VoID]], SD [[SD]], etc. 
and allows fine grained control over where each RDF triple is exported to.

In this document, examples assume 
the following namespace prefix bindings unless otherwise stated:

| Prefix    | Namespace                                        |
| --------- | ------------------------------------------------ |
| `rmlt`    | http://semweb.mmlab.be/ns/rml-target#            |
| `formats` | https://www.w3.org/ns/formats/                   |
| `comp`    | http://semweb.mmlab.be/ns/rml-compression#       |
| `void`    | http://rdfs.org/ns/void#                         |
| `sd`      | http://www.w3.org/ns/sparql-service-description# |
| `dcat`    | http://www.w3.org/ns/dcat#                       |

The examples are contained in pink colored boxes:

<pre class="ex-target">
# This box contains the example's Target description.
</pre>
