## Logical Source in RML {#logical-source-in-rml}

RML is aligned with the Logical Source vocabulary 
by extending `rr:TriplesMap` with the `rml:logicalSource` property 
to describe on Triples Map [[RML]] level where the data must be retrieved
from and where the references refer to.
A Triples Map is a function that generates an RDF triples 
from a Subject Map and Predicate Object Maps [[RML]].

A Triples Map MUST contain exactly one `rml:logicalSource` property
to describe the data source that must be used by the Triples Map to generate
RDF triples.

| Property            | Domain          | Range                |
| ------------------- | ------------    | -------------------- |
| `rml:logicalSource` | `rr:TriplesMap` | `rml:LogicalSource`  |

In the example below, a CSV file is transformed into a knowledge graph.
The CSV file is accessed using the [[CSVW]] vocabulary,
transformed into a knowledge graph using [[RML]] mappings,

<pre class="ex-input">
id;name;nickname
0;Nathan Ford;Mastermind
1;Sophie Devereaux;Grifter
2;Eliot Spender;Hitter
3;Parker;Thief
4;Alec Hardison;Hacker
</pre>

<pre class="ex-access">
&lt;#CSVSourceAccess&gt; a rml:Source, csvw:Table;
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

&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#CSVSourceAccess&gt;;
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.com/{id}";
    rr:class foaf:Person;
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:nickname;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "nickname";
    ];
  ];
.
</pre>

<pre class="ex-output">
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
</pre>

