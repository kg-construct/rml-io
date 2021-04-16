## Single targets {#single-targets}

### Subject Map {#subject-map}

All triples containing the generated subject are exported 
to the specified targets in the Subject Map [[RML]].

The following example exports all triples containing 
the generated subject `http://example.org/{id}` 
to an RDF dump with N-Quads as serialization format and GZip compression:

<pre class="ex-input">
[
  { 
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  { 
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  { 
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  { 
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  { 
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
</pre>

<pre class="ex-access">
&lt;#DCATSourceAccess&gt; a dcat:Dataset;
  dcat:distribution [ a dcat:Distribution;
    dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
  ];
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#DCATSourceAccess&gt;;
    rml:referenceFormulation ql:JSONPath;
    rml:iterator "$.[*]";
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.org/{id}";
    rml:logicalTarget &lt;#TargetDump1;&gt;
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
      rr:constant foaf:age;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "age";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:N-Quads;
  rmlt:compression comp:GZip;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nq.gz&gt;;
.
</pre>

<pre class="ex-output">
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Monica Geller" _b0 .
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" _b0 .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Rachel Green" _b0 .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" _b0 .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Joey Tribbiani" _b0 .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" _b0 .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Chandler Bing" _b0 .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" _b0 .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Ross Geller" _b0 .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" _b0 .
</pre>

### Predicate Map {#predicate-map}

All triples containing the generated predicate are exported 
to the specified targets in the Predicate Map [[RML]].

The following example exports all triples containing 
the generated predicate `foaf:name` to an RDF dump 
with Turtle as serialization format and Zip compression:

<pre class="ex-input">
[
  { 
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  { 
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  { 
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  { 
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  { 
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
</pre>

<pre class="ex-access">
&lt;#DCATSourceAccess&gt; a dcat:Dataset;
  dcat:distribution [ a dcat:Distribution;
    dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
  ];
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#DCATSourceAccess&gt;;
    rml:referenceFormulation ql:JSONPath;
    rml:iterator "$.[*]";
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.org/{id}";
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
      rml:logicalTarget &lt;#TargetDump1;&gt;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:age;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "age";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:Turtle;
  rmlt:compression comp:Zip;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nq.gz&gt;;
.
</pre>

<pre class="ex-output">
@prefix foaf: &lt;http://xmlns.com/foaf/0.1/&gt; .
@base &lt;http://example.com/ns#&gt; .

&lt;http://example.org/0&gt;
  foaf:name "Monica Geller";
.
&lt;http://example.org/1&gt;
  foaf:name "Rachel Green";
.
&lt;http://example.org/2&gt;
  foaf:name "Joey Tribbiani";
.
&lt;http://example.org/3&gt;
  foaf:name "Chandler Bing";
.
&lt;http://example.org/4&gt;
  foaf:name "Ross Geller";
.
</pre>

### Object Map {#object-map}

All triples containing the generated object are exported 
to the specified targets in the Object Map [[RML]].

The following example exports all triples containing 
the generated object from the reference `name` to an RDF dump 
with N-Triples as serialization format:

<pre class="ex-input">
[
  { 
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  { 
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  { 
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  { 
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  { 
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
</pre>

<pre class="ex-access">
&lt;#DCATSourceAccess&gt; a dcat:Dataset;
  dcat:distribution [ a dcat:Distribution;
    dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
  ];
.
</pre>

<pre class="ex-mapping">
&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#DCATSourceAccess&gt;;
    rml:referenceFormulation ql:JSONPath;
    rml:iterator "$.[*]";
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.org/{id}";
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
      rml:logicalTarget &lt;#TargetDump1;&gt;
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:age;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "age";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nt&gt;;
.
</pre>

<pre class="ex-output">
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Monica Geller" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Rachel Green" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Joey Tribbiani" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Chandler Bing" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Ross Geller" .
</pre>

### Graph Map {#graph-map}

All triples within a named graph are exported to the specified targets 
in the Graph Map [[RML]].
The named graph doesn't influence where the named graph's triples 
are exported to by the Target. 
If a named graph is spread over multiple targets, 
all targets must be combined to access the complete named graph.

The following example exports all triples in the named graph `ex:Friends`
to an RDF dump with N-Quads as serialization format:

<pre class="ex-input">
[
  { 
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  { 
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  { 
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  { 
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  { 
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
</pre>

<pre class="ex-access">
&lt;#DCATSourceAccess&gt; a dcat:Dataset;
  dcat:distribution [ a dcat:Distribution;
    dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
  ];
.
</pre>

<pre class="ex-mapping">
&lt;#Target&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
.

&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#DCATSourceAccess&gt;;
    rml:referenceFormulation ql:JSONPath;
    rml:iterator "$.[*]";
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.org/{id}";
    rml:logicalTarget &lt;#TargetDump1;&gt;
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
      rr:constant foaf:age;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "age";
      rr:graphMap [
        rml:logicalTarget &lt;#TargetDump1&gt;;
        rr:constant ex:Friends;
      ];
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nq&gt;;
.
</pre>

<pre class="ex-output">
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" &lt;http://example.org/Friends&gt; .
</pre>

### Language Map {#language-map}

All triples with a language tag are exported to the specified targets 
in the Language Map [[RML]].

The following examples export all triples with a language tag 
to a RDF dump with N-Triples as serialization format:

<pre class="ex-input">
[
  { 
    "id": 0,
    "name": "Monica Geller",
    "age": 33
  },
  { 
    "id": 1,
    "name": "Rachel Green",
    "age": 34
  },
  { 
    "id": 2,
    "name": "Joey Tribbiani",
    "age": 35
  },
  { 
    "id": 3,
    "name": "Chandler Bing",
    "age": 36
  },
  { 
    "id": 4,
    "name": "Ross Geller",
    "age": 37
  }
]
</pre>

<pre class="ex-access">
&lt;#DCATSourceAccess&gt; a dcat:Dataset;
  dcat:distribution [ a dcat:Distribution;
    dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
  ];
.
</pre>

<pre class="ex-mapping">
&lt;#Target&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:compression comp:GZip;
.

&lt;#TriplesMap&gt; a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source &lt;#DCATSourceAccess&gt;;
    rml:referenceFormulation ql:JSONPath;
    rml:iterator "$.[*]";
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.org/{id}";
   ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
      rml:languageMap [
        rml:logicalTarget &lt;#TargetDump1;&gt;
        rr:constant "en";
      ];
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:age;
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "age";
    ];
  ];
.
</pre>

<pre class="ex-target">
&lt;#TargetDump1&gt; a rmlt:LogicalTarget;
  rmlt:target &lt;#VoIDDump1&gt;;
  rmlt:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nt&gt;;
.
</pre>

<pre class="ex-output">
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Monica Geller"@en .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Rachel Green"@en .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Joey Tribbiani"@en .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Chandler Bing"@en .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Ross Geller"@en .
</pre>
