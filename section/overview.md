## Overview {#overview}

*This section is non-normative.*

This document describes the alignment of Target specification with RML 
to define how a generated RDF knowledge graph must be exported 
in the RML mapping rules.
Target and RML are self-standing specifications 
which are aligned through this specification.

In this document, examples assume 
the following namespace prefix bindings unless otherwise stated:

| Prefix     | Namespace                                        |
| ---------  | ------------------------------------------------ |
| `rml`      | http://semweb.mmlab.be/ns/rml#                   |
| `rmlt`     | http://semweb.mmlab.be/ns/rml-target#            |
| `rr`       | http://www.w3.org/ns/r2rml#                      |
| `formats`  | https://www.w3.org/ns/formats/                   |
| `comp`     | http://semweb.mmlab.be/ns/rml-compression#       |
| `csvw`     | http://www.w3.org/ns/csvw#                       |
| `foaf`     | http://xmlns.com/foaf/0.1/                       |
| `fnml`     | http://semweb.mmlab.be/ns/fnml#                  |
| `idlab-fn` | http://example.com/idlab/function/               |
| `void`     | http://rdfs.org/ns/void#                         |

Examples are divided in several boxes, each box has its own color.
Blue boxes contain the input RDF data of the example:

<pre class="ex-input">
# This box contains the example's input RDF data.
</pre>

The Target description is contained in a pink box:

<pre class="ex-target">
# This box contains the example's Target description.
</pre>

The data access description is contained in a grey box:

<pre class="ex-access">
# This box contains the data access description of the example.
</pre>

The RML mapping is contained in a yellow box:

<pre class="ex-mapping">
# This box contains the example's RML mapping.
</pre>

The generated output RDF is contained in a green box:

<pre class="ex-output">
# This box contains the example's generated output RDF.
</pre>
