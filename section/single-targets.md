## Single targets {#single-targets}

In the following examples, the RDF triples are exported to a single Target.
In some examples, not all RDF triples have a dedicated Target assigned,
therefore, they will be exported to the default Target of the processor.

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
&lt;#DCATSourceAccess&gt; a rml:Source, dcat:Distribution;
  dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
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
    rml:logicalTarget &lt;#TargetDump1&gt;;
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
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#VoIDDump1&gt;;
  rml:serialization formats:N-Quads;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a rml:Target, void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nq.gz&gt;;
  rml:compression comp:gzip;
.
</pre>

<pre class="ex-output">
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Monica Geller" .
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Rachel Green" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Joey Tribbiani" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Chandler Bing" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Ross Geller" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" .
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
&lt;#DCATSourceAccess&gt; a rml:Source, dcat:Distribution;
  dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
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
      rml:logicalTarget &lt;#TargetDump1&gt;;
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
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#VoIDDump1&gt;;
  rml:serialization formats:Turtle;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a rml:Target, void:Dataset;
  void:dataDump &lt;file:///data/dump1.ttl.zip&gt;;
  rml:compression comp:zip;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.ttl.zip
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

# default target of the processor
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" .

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
&lt;#DCATSourceAccess&gt; a rml:Source, dcat:Distribution;
  dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
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
      rml:logicalTarget &lt;#TargetDump1&gt;;
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
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#VoIDDump1&gt;;
  rml:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a rml:Target, void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nt&gt;;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nt
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Monica Geller" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Rachel Green" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Joey Tribbiani" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Chandler Bing" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Ross Geller" .

# default target of the processor
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" .

</pre>

### Graph Map {#graph-map}

All triples within a named graph are exported to the specified targets 
in the Graph Map [[RML]].
The named graph influences to where the named graph's triples 
may be exported to as the Target's serialization format must 
support named graphs such as N-Quads, JSON-LD or TriG.
When a Target contains a serialization format 
which does not support named graphs and a Graph Map is used,
the mapping is considered invalid.
If a named graph is spread over multiple targets, 
all targets must be combined to access the complete named graph.
In case RDF triples are not within a specific named graph,
they are added to the default graph as specified 
by the [[R2RML]] specification.

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
&lt;#DCATSourceAccess&gt; a rml:Source, dcat:Distribution;
  dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
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
    rr:graphMap [
      rml:logicalTarget &lt;#TargetDump1&gt;;
      rr:constant ex:Friends;
    ];
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
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#VoIDDump1&gt;;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a rml:Target, void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nq&gt;;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nq
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" &lt;http://example.org/Friends&gt; .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" &lt;http://example.org/Friends&gt; .
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
&lt;#DCATSourceAccess&gt; a rml:Source, dcat:Dataset;
  dcat:downloadURL "https://rml.io/specs/rml-target/Friends.json";
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
      rml:languageMap [
        rml:logicalTarget &lt;#TargetDump1&gt;;
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
&lt;#TargetDump1&gt; a rml:LogicalTarget;
  rml:target &lt;#VoIDDump1&gt;;
  rml:serialization formats:N-Triples;
.
</pre>

<pre class="ex-access">
&lt;#VoIDDump1&gt; a rml:Target, void:Dataset ;
  void:dataDump &lt;file:///data/dump1.nt&gt;;
.
</pre>

<pre class="ex-output">
# file:///data/dump1.nt
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Monica Geller"@en .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Rachel Green"@en .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Joey Tribbiani"@en .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Chandler Bing"@en .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/name&gt; "Ross Geller"@en .

# default target of the processor
&lt;http://example.org/0&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "33" .
&lt;http://example.org/1&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "34" .
&lt;http://example.org/2&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "35" .
&lt;http://example.org/3&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "36" .
&lt;http://example.org/4&gt; &lt;http://xmlns.com/foaf/0.1/age&gt; "37" .
</pre>
