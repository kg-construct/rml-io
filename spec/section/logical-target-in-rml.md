## Logical Target in RML {#logical-target-in-rml}

RML is aligned with the Logical Target vocabulary
by extending `rml:TermMap` with the `rml:logicalTarget` property
to describe on Term Map [[RML]] level where each triple must be directed to.
A Term Map is a function that generates an RDF term
from a logical reference [[RML]].
The result of that function is known as the term map's generated
RDF term [[RDF-Concepts]]
such as subjects, predicates, objects, named graphs and language tags.

Each RML processor has a default target where generated triples are exported.
Logical Targets provide a mechanism to override this default target for some
of the triples to be exported.

Logical Targets are defined in Term Maps. A Term Map MAY contain
one or more `rml:logicalTarget` properties to export all triples containing
the generated term to different targets. Specifically, when generating a
triple `t`, if any of the term maps involved in the generation of `t`
contains a Logical Target `LT`, then triple `t` exported to target `LT`.
If none of those Term Maps contains a Logical Target,
then the triple `t` is sent to the default target of the RML processor.

Multiple Logical Targets MAY be combined by specifying multiple Logical Targets
in the same Term Map or multiple Term Maps of the same RDF triple
(Section [[[#multiple-targets]]]).
Logical Targets MAY be overriden by using a separate Triples Map
or conditions [[FnO]] (Section [[[#overriding-targets]]]).

If the mapping document contains no Targets,
the processor falls back to the default target,
as it is specified through the processor's
specific configuration file or command line parameters.
If a mapping document contains at least one Target,
the processor will export the triples to these Targets,
triples which do not have one or more Target(s) assigned,
are exported to the default target of the processor.

| Property            | Domain       | Range                |
| ------------------- | ------------ | -------------------- |
| `rml:logicalTarget` | `rml:TermMap` | `rml:LogicalTarget` |

In the example below, a CSV file is transformed into a knowledge graph.
The CSV file is accessed using the [[CSVW]] vocabulary,
transformed into a knowledge graph using [[RML]] mappings,
and exported to two Logical Targets, which are accessed through the [[DCAT]]
vocabulary.
The knowledge graph is exported as N-Quads to the first Target,
and as Turtle to the second Target.
The Turtle file of the second Target is also compressed using the Zip
compression algorithm.

<pre class="ex-input">
id;name;nickname
0;Nathan Ford;Mastermind
1;Sophie Devereaux;Grifter
2;Eliot Spender;Hitter
3;Parker;Thief
4;Alec Hardison;Hacker
</pre>

<pre class="ex-access">
&lt;#CSVSourceAccess&gt; a csvw:Table;
  csvw:url "https://rml.io/specs/rml-target/Leverage.csv";
  csvw:dialect [ a csvw:Dialect;
    csvw:delimiter ";";
    csvw:encoding "UTF-8";
    csvw:header "1"^^xsd:boolean;
  ];
.
</pre>

<pre class="ex-mapping">
@base &lt;http://example.com/ns#&gt; .

&lt;#TriplesMap&gt; a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#CSVSourceAccess&gt;;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.com/{id}";
    rml:logicalTarget &lt;#TargetDump1&gt;;
    rml:class foaf:Person;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
      rml:logicalTarget &lt;#TargetDump2&gt;;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:nickname;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "nickname";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#DCATDump1&gt;;
  rml:serialization formats:N-Triples;
.

&lt;#TargetDump2&gt; a rml:LogicalTarget;
  rml:target &lt;#DCATDump2&gt;;
  rml:serialization formats:Turtle;
.
</pre>

<pre class="ex-access">
&lt;#DCATDump1&gt; a dcat:Distribution;
  dcat:downloadURL &ltfile:///data/dump1.nt&gt;;
.

&lt;#DCATDump2&gt; a dcat:Distribution;
  dcat:downloadURL &ltfile:///data/dump2.ttl.zip&gt;;
  rml:compression rml:zip;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nq
&lt;http://example.org/0&gt; &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#type&gt; &lt;http://xmlns.com/foaf/0.1/Person&gt; _b0 .
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Nathan Ford" _b0 .
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/nickname&gt; "Mastermind" _b0 .
&lt;http://example.org/1&gt; &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#type&gt; &lt;http://xmlns.com/foaf/0.1/Person&gt; _b0 .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Sophie Devereaux" _b0 .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/nickname&gt; "Grifter" _b0 .
&lt;http://example.org/2&gt; &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#type&gt; &lt;http://xmlns.com/foaf/0.1/Person&gt; _b0 .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Eliot Spencer" _b0 .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/nickname&gt; "Hitter" _b0 .
&lt;http://example.org/3&gt; &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#type&gt; &lt;http://xmlns.com/foaf/0.1/Person&gt; _b0 .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Parker" _b0 .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/nickname&gt; "Thief" _b0 .
&lt;http://example.org/4&gt; &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#type&gt; &lt;http://xmlns.com/foaf/0.1/Person&gt; _b0 .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Alec Hardison" _b0 .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/nickname&gt; "Hacker" _b0 .

# file:///data/dump2.ttl.zip
@prefix foaf: &lt;http://xmlns.com/foaf/0.1/&gt; .

&lt;http://example.org/0&gt;
  foaf:name "Nathan Ford";
.
&lt;http://example.org/1&gt;
  foaf:name "Sophie Devereaux";
.
&lt;http://example.org/2&gt;
  foaf:name "Eliot Spencer";
.
&lt;http://example.org/3&gt;
  foaf:name "Parker";
.
&lt;http://example.org/4&gt;
  foaf:name "Alec Hardison";
.
</pre>

