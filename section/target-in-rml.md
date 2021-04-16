## Target in RML {#target-in-rml}

RML does not specify where generated triples are exported to, 
each RML processor has its own way to describe this information 
through configuration files or command line parameters. 
To incorporate this information in the RML mapping rules, 
RML is aligned with the 
[Target vocabulary](http://semweb.mmlab.be/ns/rml-target#)
which describes how the generated triples are exported. 
RML is aligned with the Target vocabulary 
by extending `rr:TermMap` with the `rml:logicalTarget` property 
to describe on Term Map [[RML]] level where each triple must be directed to. 
A Term Map is a function that generates an RDF term 
from a logical reference [[RML]].
The result of that function is known as the term map's generated 
RDF term [[RDF-Concepts]] 
such as subjects, predicates, objects, named graphs and language tags.

A Term Map MAY also contain zero or more `rml:logicalTarget` properties 
to export all triples containing the generated term to different targets. 
The same Term Map can have multiple targets by specifying 
multiple `rml:logicalTarget` properties in the Term Map. 

Multiple Targets MAY be combined by specifying multiple Targets 
in the same Term Map or multiple Term Maps of the same RDF triple 
(Section [[[#multiple-targets]]]). 
Targets MAY be overriden by using a separate Triples Map 
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
| `rml:logicalTarget` | `rr:TermMap` | `rmlt:LogicalTarget` |

In the example below, a CSV file is transformed into a knowledge graph.
The CSV file is accessed using the [[CSVW]] vocabulary,
transformed into a knowledge graph using [[RML]] mappings,
and exported to two Targets, which are accessed through the [[VoID]] vocabulary.
The knowledge graph is exported as N-Quads to the first Target,
and as Turtle to the second Target.
The Turtle file of the second Target is also compressed using the Zip 
compression algorithm.

<pre class="ex-input">
id;city;bus;latitude;longitude
6523;Brussels;25;50.901389;4.484444
6524;Athens;78;37.936388;23.947222
</pre>

<pre class="ex-access">
&lt;#CSVSourceAccess&gt; a csvw:Table;
  csvw:url "https://rml.io/specs/rml-target/Airport.csv";
  csvw:dialect [ a csvw:Dialect;
    csvw:delimiter ";";
    csvw:encoding "UTF-8";
    csvw:header "1"^^xsd:boolean;
  ];
.
</pre>

<pre class="ex-mapping">
@prefix transit: &lt;http://vocab.org/transit/terms/&gt; .
@prefix wgs84_pos: &lt;http://www.w3.org/2003/01/geo/wgs84_pos#&gt; .
@base &lt;http://example.com/ns#&gt; .

&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#CSVSourceAccess&gt;;
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://airport.example.com/{id}";
    rml:logicalTarget &lt;#TargetDump1&gt;;
    rr:class transit:Stop;
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant transit:route;
      rml:logicalTarget &lt;#TargetDump2&gt;;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "stop";
      rr:datatype xsd:int;
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant wgs84_pos:lat;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "latitude";
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant wgs84_pos:long;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "longitude";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:N-Triples;
.

&lt;#TargetDump2&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump2&gt;;
  rmlt:serialization formats:Turtle;
  rmlt:compression comp:Zip;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset;
    void:dataDump &ltfile:///data/dump1.nt&gt;;
.

&lt;#VoIDDump2&gt; a void:Dataset;
    void:dataDump &ltfile:///data/dump2.ttl.zip&gt;;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nq
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix transit: &lt;http://vocab.org/transit/terms/&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .
@prefix wgs84_pos: &lt;http://www.w3.org/2003/01/geo/wgs84_pos#&gt; .

&lt;http://airport.example.com/6523&gt; rdf:type transit:Stop .
&lt;http://airport.example.com/6523&gt; transit:route "25"^^xsd:int .
&lt;http://airport.example.com/6523&gt; wgs84_pos:lat "50.901389" .
&lt;http://airport.example.com/6523&gt; wgs84_pos:long "4.484444" .

# file:///data/dump2.ttl.zip
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix transit: &lt;http://vocab.org/transit/terms/&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .
@prefix wgs84_pos: &lt;http://www.w3.org/2003/01/geo/wgs84_pos#&gt; .

&lt;http://airport.example.com/6523&gt;
    transit:route "25"^^xsd:int;
.
</pre>

