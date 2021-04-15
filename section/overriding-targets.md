## Overriding Targets {#overriding-targets}

In some cases exporting all triples to a target is not desired, 
therefore Targets can be overridden when needed 
by either using a separate Triples Map which isolates certain triples or 
by using FnO functions [[FnO]] as conditions.

### Separate Triples Map {#seperate-triples-map}

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

### Conditions {#conditions}

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
