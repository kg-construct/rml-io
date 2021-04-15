## Combining multiple Targets {#multi-targets}

Multiple Targets MAY be specified for the same triple 
in the same or multiple Term Maps.
If multiple Targets are defined in the same Term Map, 
all triples containing the generated Term are exported 
to all the specified Targets. 
In case multiple Term Maps of the same RDF triple contain more than one Target, 
the generated triples are exported to all the specified Targets.

### Subject Map and Predicate Map {#subject-and-predicate-map}

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

### Subject Map, Predicate Map and Object Map {#subject-predicate-and-object-map}

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

### Language Map and Object Map {#language-and-object-map}

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
