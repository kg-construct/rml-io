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
# DBPedia Friends actors as CSV
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
&lt;#SourceAccess&gt; a rml:Source, rml:FilePath;
  rml:path "FriendsDBPedia.csv";
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap1&gt; a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#SourceAccess&gt;;
    rml:referenceFormulation rml:CSV;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:reference "actor";
    rml:termType rml:IRI;
    rml:logicalTarget &lt;TargetDump1&gt;;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];

&lt;#TriplesMap2&gt; a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#SourceAccess&gt;;
    rml:referenceFormulation rml:CSV;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:reference "actor";
    rml:termType rml:IRI;
    rml:logicalTarget &lt;TargetDump2&gt;;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant schema:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#Dump1&gt;;
  rml:serialization formats:N-Triples;
.
&lt;#TargetDump2&gt; a rml:LogicalTarget;
  rml:target &lt;#Dump2&gt;;
  rml:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#Dump1&gt; a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
&lt;#Dump2&gt; a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
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
# DBPedia Friends actors as CSV
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
&lt;#SourceAccess&gt; a rml:Source, rml:FilePath;
  rml:path "FriendsDBPedia.csv";
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap&gt; a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;SourceAccess&gt;;
    rml:referenceFormulation rml:CSV;
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:reference "actor";
    rml:termType rml:IRI;
    rml:logicalTarget &lt;TargetDump1&gt;;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name";
    ];
  ];
  rml:predicateObjectMap [
    rml:predicateMap [ rml:constant foaf:name ];
    rml:objectMap [
      fnml:functionValue [
        rml:predicateObjectMap [
          rml:predicate fno:executes ;
          rml:objectMap [ rml:constant idlab-fn:decide ]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:expectedStr ;
          rml:objectMap [ rml:constant "Jim Parsons"]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:str ;
          rml:objectMap [
            rml:reference "name";
            rml:logicalTarget <#TargetDump1>;
          ];
        ];
      ];
    ];
  ];
  rml:predicateObjectMap [
    rml:predicateMap [ rml:constant foaf:name ];
    rml:objectMap [
      fnml:functionValue [
        rml:predicateObjectMap [
          rml:predicate fno:executes ;
          rml:objectMap [ rml:constant idlab-fn:decide ]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:expectedStr ;
          rml:objectMap [ rml:constant "Kaley Cuoco"]
        ];
        rml:predicateObjectMap [
          rml:predicate idlab-fn:str ;
          rml:objectMap [
            rml:reference "name";
            rml:logicalTarget <#TargetDump2>;
          ];
        ];
      ];
    ];
  ];
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#Dump1&gt;;
  rml:serialization formats:N-Triples;
.
&lt;#TargetDump2&gt; a rml:LogicalTarget;
  rml:target &lt;#Dump2&gt;;
  rml:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#Dump1&gt; a rml:Target, rml:FilePath;
  rml:path "/data/dump1.nt";
.
&lt;#Dump2&gt; a rml:Target, rml:FilePath;
  rml:path "/data/dump2.nt";
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nt
&lt;http://dbpedia.org/resource/Jim_Parsons&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Jim Parsons" .

# file:///data/dump2.nt
&lt;http://dbpedia.org/resource/Kaley_Cuoco&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Kaley Cuoco" .
</pre>
