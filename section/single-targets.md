## Single targets {#single-targets}

### Subject Map {#subject-map}

All triples containing the generated subject are exported 
to the specified targets in the Subject Map [[RML]].

The following example exports all triples containing 
the generated subject `http://example.org/{id}` 
to an RDF dump with N-Quads as serialization format and GZip compression:

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump> a void:Dataset ;
  void:dataDump <file:///data/file.nt.gz>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump>;
  rmlt:serialization formats:N-Quads ;
  rmlt:compression comp:GZip;
.

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ 
    rr:template "http://example.org/{id}";
    rml:logicalTarget <#LogicalTarget1>;
   ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:name ];
    rr:objectMap [ rml:reference "name"; ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [ rml:reference "age" ];
  ];
.
```

### Predicate Map {#predicate-map}

All triples containing the generated predicate are exported 
to the specified targets in the Predicate Map [[RML]].

The following example exports all triples containing 
the generated predicate `foaf:name` to an RDF dump 
with Turtle as serialization format and Zip compression:

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump> a void:Dataset ;
  void:dataDump <file:///data/file.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;
.

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ rr:template "http://example.org/{id}"; ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ 
      rr:constant foaf:name;
      rml:logicalTarget <#LogicalTarget1>; 
    ];
    rr:objectMap [ rml:reference "name" ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [ rml:reference "age" ];
  ];
.
```

### Object Map {#object-map}

All triples containing the generated object are exported 
to the specified targets in the Object Map [[RML]].

The following example exports all triples containing 
the generated object name to an RDF dump 
with N-Triples as serialization format:

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump> a void:Dataset ;
  void:dataDump <file:///data/file.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ rr:template "http://example.org/{id}"; ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:name ];
    rr:objectMap [ 
      rml:reference "name";
      rml:logicalTarget <#LogicalTarget1>;
    ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [ rml:reference "age" ];
  ];
.
```

### Graph Map {#graph-map}

All triples within a named graph are exported to the specified targets 
in the Graph Map [[RML]].
The named graph doesn't influence where the named graph's triples 
are exported to by the Target. 
If a named graph is spread over multiple targets, 
all targets must be combined to access the complete named graph.

The following example exports all triples in the named graph `ex:MyGraph`
to an SPARQL [[SPARQL]] endpoint using `SPARQL UPDATE`:

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump> a void:Dataset ;
  void:dataDump <file:///data/file.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ 
    rr:template "http://example.org/{id}";
   ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:name ];
    rr:objectMap [ rml:reference "name"; ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [ 
      rml:reference "age";
      rr:graphMap [
        rml:logicalTarget <#LogicalTarget1>;
        rr:template "http://www.example.org/{type}" 
      ];
    ];
  ];
.
```

### Language Map {#language-map}

All triples with a language tag are exported to the specified targets 
in the Language Map [[RML]].

The following examples export all triples with a language tag 
to a RDF dump with JSON-LD as serialization format:

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump> a void:Dataset ;
  void:dataDump <file:///data/file.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ 
    rr:template "http://example.org/{id}";
   ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:name ];
    rr:objectMap [ 
      rml:reference "name";
      rml:languageMap [
        rml:logicalTarget <#LogicalTarget1>;
        rml:reference "language";
      ]; 
    ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [ rml:reference "age"; ];
  ];
.
```
