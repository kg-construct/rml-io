## Overriding Targets {#overriding-targets}

In some cases exporting all triples to a target is not desired, 
therefore Targets can be overridden when needed 
by either using a separate Triples Map which isolates certain triples or 
by using FnO functions [[FnO]] as conditions.

### Separate Triples Map {#seperate-triples-map}

Triples can be exported to a specific Target while not to other Targets 
by isolating these triples in a separate Triples Map.

In this example, the same subject and object are used in both Triples Maps,
but with a diffent predicate. The triples with the first predicate `foaf:name`
are exported to the first Target and the triples with the second predicate
`schema:name` to the second Target.

<pre class="ex-input">
# Results of DBPedia SPARQL query
actor,name,nickname
http://dbpedia.org/resource/Kevin_Sussman,Kevin Sussman
http://dbpedia.org/resource/Jim_Parsons,Jim Parsons
http://dbpedia.org/resource/Kaley_Cuoco,Kaley Cuoco
http://dbpedia.org/resource/Sara_Gilbert,Sara Gilbert
http://dbpedia.org/resource/Kunal_Nayyar,Kunal Nayyar
http://dbpedia.org/resource/Laura_Spencer_(actress),Laura Spencer
http://dbpedia.org/resource/Simon_Helberg,Simon Helberg
http://dbpedia.org/resource/Johnny_Galecki,Johnny Galecki
http://dbpedia.org/resource/Mayim_Bialik,Mayim Bialik
http://dbpedia.org/resource/Melissa_Rauch,Melissa Rauch
</pre>

<pre class="ex-access">
&lt;#SDSourceAccess&gt; a sd:Service;
  sd:endpoint <http://dbpedia.org/sparql/>;
  sd:supportedLanguage sd:SPARQL11Query;
  sd:resultFormat formats:SPARQL_Results_CSV;
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap1&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#SDSourceAccess&gt;;
    rml:query """
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      SELECT DISTINCT ?actor ?name WHERE {
        ?tvshow rdf:type dbo:TelevisionShow .
        ?tvshow rdfs:label "The Big Bang Theory"@en .
        ?tvshow dbo:starring ?actor .
        ?actor foaf:name ?name .
      }
    """;
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rml:reference "actor";
    rr:termType rr:IRI;
    rmlt:logicalTarget &lt;TargetDump1&gt;;
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
    ];
  ];

&lt;#TriplesMap2&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#SDSourceAccess&gt;;
    rml:query """
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      SELECT DISTINCT ?actor ?name WHERE {
        ?tvshow rdf:type dbo:TelevisionShow .
        ?tvshow rdfs:label "The Big Bang Theory"@en .
        ?tvshow dbo:starring ?actor .
        ?actor foaf:name ?name .
      }
    """;
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rml:reference "actor";
    rr:termType rr:IRI;
    rmlt:logicalTarget &lt;TargetDump2&gt;;
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant schema:name;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
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
  rmlt:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nt&gt;;
.
&lt;#VoIDDump2&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump2.nq&gt;;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nt
&lt;http://dbpedia.org/resource/Kevin_Sussman&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Kevin Sussman" .
&lt;http://dbpedia.org/resource/Jim_Parsons&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Jim Parsons" .
&lt;http://dbpedia.org/resource/Kaley_Cuoco&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Kaley Cuoco" .
&lt;http://dbpedia.org/resource/Sara_Gilbert&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Sara Gilbert" .
&lt;http://dbpedia.org/resource/Kunal_Nayyar&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Kunal Nayyar" .
&lt;http://dbpedia.org/resource/Laura_Spencer&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Laura Spencer" .
&lt;http://dbpedia.org/resource/Simon_Helberg&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Simon Helberg" .
&lt;http://dbpedia.org/resource/Johnny_Galecki&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Johnny Galecki" .
&lt;http://dbpedia.org/resource/Mayim_Bialik&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Mayim Bialik" .
&lt;http://dbpedia.org/resource/Melissa_Rauch&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Melissa Rauch" .

# file:///data/dump2.nt
&lt;http://dbpedia.org/resource/Kevin_Sussman&gt; &lt;http://schema.org/name&gt; "Kevin Sussman" .
&lt;http://dbpedia.org/resource/Jim_Parsons&gt; &lt;http://schema.org/name&gt; "Jim Parsons" .
&lt;http://dbpedia.org/resource/Kaley_Cuoco&gt; &lt;http://schema.org/name&gt; "Kaley Cuoco" .
&lt;http://dbpedia.org/resource/Sara_Gilbert&gt; &lt;http://schema.org/name&gt; "Sara Gilbert" .
&lt;http://dbpedia.org/resource/Kunal_Nayyar&gt; &lt;http://schema.org/name&gt; "Kunal Nayyar" .
&lt;http://dbpedia.org/resource/Laura_Spencer&gt; &lt;http://schema.org/name&gt; "Laura Spencer" .
&lt;http://dbpedia.org/resource/Simon_Helberg&gt; &lt;http://schema.org/name&gt; "Simon Helberg" .
&lt;http://dbpedia.org/resource/Johnny_Galecki&gt; &lt;http://schema.org/name&gt; "Johnny Galecki" .
&lt;http://dbpedia.org/resource/Mayim_Bialik&gt; &lt;http://schema.org/name&gt; "Mayim Bialik" .
&lt;http://dbpedia.org/resource/Melissa_Rauch&gt; &lt;http://schema.org/name&gt; "Melissa Rauch" .
</pre>

### Conditions {#conditions}

FnO functions MAY be leveraged to export triples 
only under certain conditions. 
Conditions are already integrated in RML+FnO processors, 
thus conditions apply on Targets as well.
Triples are generated and exported based on the FnO condition's evaluation. 
Only if the condition is true, the triples are generated and exported.

In the example, the triples with `Jim Parsons` as object are exported 
to the first Target, triples with `Kaley Cuoco` as object are exported 
to the second Target.

<pre class="ex-input">
# Results of DBPedia SPARQL query
actor,name,nickname
http://dbpedia.org/resource/Kevin_Sussman,Kevin Sussman
http://dbpedia.org/resource/Jim_Parsons,Jim Parsons
http://dbpedia.org/resource/Kaley_Cuoco,Kaley Cuoco
http://dbpedia.org/resource/Sara_Gilbert,Sara Gilbert
http://dbpedia.org/resource/Kunal_Nayyar,Kunal Nayyar
http://dbpedia.org/resource/Laura_Spencer_(actress),Laura Spencer
http://dbpedia.org/resource/Simon_Helberg,Simon Helberg
http://dbpedia.org/resource/Johnny_Galecki,Johnny Galecki
http://dbpedia.org/resource/Mayim_Bialik,Mayim Bialik
http://dbpedia.org/resource/Melissa_Rauch,Melissa Rauch
</pre>

<pre class="ex-access">
&lt;#SDSourceAccess&gt; a sd:Service;
  sd:endpoint <http://dbpedia.org/sparql/>;
  sd:supportedLanguage sd:SPARQL11Query;
  sd:resultFormat formats:SPARQL_Results_CSV;
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#SDSourceAccess&gt;;
    rml:query """
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      SELECT DISTINCT ?actor ?name WHERE {
        ?tvshow rdf:type dbo:TelevisionShow .
        ?tvshow rdfs:label "The Big Bang Theory"@en .
        ?tvshow dbo:starring ?actor .
        ?actor foaf:name ?name .
      }
    """;
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rml:reference "actor";
    rr:termType rr:IRI;
    rmlt:logicalTarget &lt;TargetDump1&gt;;
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
    ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:name ];
    rr:objectMap [
      fnml:functionValue [
        rr:predicateObjectMap [
          rr:predicate fno:executes ;
          rr:objectMap [ rr:constant idlab-fn:decide ]
        ];
        rr:predicateObjectMap [
          rr:predicate idlab-fn:expectedStr ;
          rr:objectMap [ rr:constant "Jim Parsons"]
        ];
        rr:predicateObjectMap [
          rr:predicate idlab-fn:str ;
          rr:objectMap [ 
            rml:reference "name";
            rml:logicalTarget <#TargetDump1>;
          ];
        ];
      ];
    ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:name ];
    rr:objectMap [
      fnml:functionValue [
        rr:predicateObjectMap [
          rr:predicate fno:executes ;
          rr:objectMap [ rr:constant idlab-fn:decide ]
        ];
        rr:predicateObjectMap [
          rr:predicate idlab-fn:expectedStr ;
          rr:objectMap [ rr:constant "Kaley Cuoco"]
        ];
        rr:predicateObjectMap [
          rr:predicate idlab-fn:str ;
          rr:objectMap [ 
            rml:reference "name";
            rml:logicalTarget <#TargetDump2>;
          ];
        ];
      ];
    ];
  ];
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:N-Triples;
.
&lt;#TargetDump2&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump2&gt;;
  rmlt:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nt&gt;;
.
&lt;#VoIDDump2&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump2.nt&gt;;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nt
&lt;http://dbpedia.org/resource/Jim_Parsons&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Jim Parsons" .

# file:///data/dump2.nt
&lt;http://dbpedia.org/resource/Kaley_Cuoco&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Kaley Cuoco" .
</pre>
