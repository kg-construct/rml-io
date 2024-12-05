## Input Logical Source in RML {#logical-source-in-rml}

[[RML-Core]] introduces a <a data-cite="RML-Core#dfn-logical-source">logical source</a>
as an abstract construct to describe how a <a data-cite="RML-Core#dfn-data-source">data source</a>
 can be accessed to be used in a <a data-cite="RML-Core#dfn-triples-map">Triples Map</a>.

In this specification we introduce the [=Input Logical Source=] to describe how an input
<a data-cite="RML-Core#dfn-data-source">data source</a> can be accessed.

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

&lt;#TriplesMap&gt; a rml:TriplesMap;
  rml:logicalSource [ a rml:InputLogicalSource;
    rml:source &lt;#CSVSourceAccess&gt;;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.com/{id}";
    rml:class foaf:Person;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
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

