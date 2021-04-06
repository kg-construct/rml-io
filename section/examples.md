## Examples {#examples}

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

### Combining multiple Targets {#combining-targets}

Multiple Targets MAY be specified for the same triple 
in the same or multiple Term Maps.
Each triple is exported to all the Targets 
specified in the triple's Term Maps.

#### Subject Map and Predicate Map {#subject-and-predicate-map}

All triples containing the subject `http://example.org/{id}`
are exported to `LogicalTarget1` 
and all triples containing the predicate `foaf:name`
are exported to `LogicalTarget2`.

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump1> a void:Dataset ;
  void:dataDump <file:///data/file1.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump1>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#VoIDDump2> a void:Dataset ;
  void:dataDump <file:///data/file2.nt>;
.

<#LogicalTarget2> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump2>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;
.

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ 
    rr:template "http://example.org/{id}";
    rml:logicalTarget <#LogicalTarget1>;
   ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ 
      rml:logicalTarget <#LogicalTarget2>;
      rr:constant foaf:name 
    ];
    rr:objectMap [ rml:reference "name"; ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [ rml:reference "age" ];
  ];
.
```

#### Subject Map, Predicate Map and Object Map {#subject-predicate-and-object-map}

All triples containing the subject `http://example.org/{id}` are exported 
to `LogicalTarget1`, all triples containing the predicate `foaf:name` 
are exported to `LogicalTarget2` and all triples containing the object `"age"`
are exported to `LogicalTarget3`.

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump1> a void:Dataset ;
  void:dataDump <file:///data/file1.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump1>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#VoIDDump2> a void:Dataset ;
  void:dataDump <file:///data/file2.nt>;
.

<#LogicalTarget2> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump2>;
  rmlt:serialization formats:N-Quads ;
.

<#SPARQLUPDATE_target> a sd:Service ;
  sd:endpoint  <http://example.org/sparql-update> ;
  sd:supportedLanguage sd:SPARQL11Update ;
.

<#LogicalTarget3> a rml:logicalTarget;
  rmlt:target <#SPARQLEndpoint>;
.

<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ 
    rr:template "http://example.org/{id}";
    rml:logicalTarget <#LogicalTarget1>;
   ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ 
      rml:logicalTarget <#LogicalTarget2>;
      rr:constant foaf:name;
    ];
    rr:objectMap [ 
      rml:reference "name"; 
    ];
  ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:age ];
    rr:objectMap [
      rml:logicalTarget <#LogicalTarget3>;
      rml:reference "age";
    ];
  ];
.
```

#### Language Map and Object Map {#language-and-object-map}

All triples containing the language tag `language` 
are exported to `LogicalTarget1` 
and all triples containing the object `"age"` 
are exported to `LogicalTarget2`.

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump1> a void:Dataset ;
  void:dataDump <file:///data/file1.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump1>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#VoIDDump2> a void:Dataset ;
  void:dataDump <file:///data/file2.nt>;
.

<#LogicalTarget2> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump2>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;
.

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
    rr:objectMap [ 
      rml:reference "age";
      rml:logicalTarget <#LogicalTarget2>;
    ];
  ];
.
```

### Overriding Targets {#overriding-targets}

In some cases exporting all triples to a target is not desired, 
therefore Targets can be overridden when needed 
by either using a separate Triples Map which isolates certain triples or 
by using FnO functions [[FnO]] as conditions.

#### Separate Triples Map {#seperate-triples-map}

Triples can be exported to a specific Target while not to other Targets 
by isolating these triples in a separate Triples Map.

In this example, all triples containing the subject `http://example.org/{id}`
are exported to `LogicalTarget1` 
and all triples containing the subject `http://newtarget.org/{id}` 
are exported to LogicalTarget2.

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump1> a void:Dataset ;
  void:dataDump <file:///data/file1.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump1>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;

<#VoIDDump2> a void:Dataset ;
  void:dataDump <file:///data/file2.nt>;
.

<#LogicalTarget2> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump2>;
  rmlt:serialization formats:N-Triples ;
  rmlt:compression comp:GZip;
.

<#TriplesMap1> a rr:TriplesMap;
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
    rr:objectMap [ 
      rml:reference "age";
    ];
  ];
.

<#TriplesMap2> a rr:TriplesMap;
  rml:logicalSource <#LogicalSource1>;
  rr:subjectMap [ 
    rr:template "http://newtarget.org/{id}";
    rml:logicalTarget <#LogicalTarget2>;
   ];
  rr:predicateObjectMap [ 
    rr:predicateMap [ rr:constant foaf:interest ];
    rr:objectMap [ rml:reference "interest"; ];
  ];
.
```

#### Conditions {#conditions}

FnO functions MAY be leveraged to export triples 
only under certain conditions. 
Conditions are already integrated in RML+FnO processors, 
thus conditions apply on Targets as well.
Triples are generated and exported based on the FnO condition's evaluation. 
Only if the condition is true, the triples are generated and exported.

```turtle "example": " "
<#LogicalSource1> a rml:LogicalSource;
  rml:source "/data/people.json";
  rml:referenceFormulation ql:JSONPath;
  rml:iterator "$.[*]";
.

<#VoIDDump1> a void:Dataset ;
  void:dataDump <file:///data/file1.nt>;
.

<#LogicalTarget1> a rmlt:LogicalTarget;
  rmlt:target <#VoIDDump1>;
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
      fnml:functionValue [
        rr:predicateObjectMap [
          rr:predicate fno:executes ;
          rr:objectMap [ rr:constant idlab-fn:trueCondition ]
        ];
        rr:predicateObjectMap [
          rr:predicate idlab-fn:strBoolean ;
          rr:objectMap [ rr:constant "true"]
        ];
        rr:predicateObjectMap [
          rr:predicate idlab-fn:str ;
          rr:objectMap [ 
            rml:reference "age";
            rml:logicalTarget <#LogicalTarget1>;
          ];
        ];
      ];
    ];
  ];
.
```
