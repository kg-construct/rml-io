# RMLTTC0002g

Test exporting all triples to a Target in a Predicate Map and a Target in a Graph Map.

**Error expected?** Yes

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLTTC0002g/Friends.json](http://w3id.org/rml/resources/rml-io/RMLTTC0002g/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix ex: <http://example.org> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
    dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLTTC0002g/Friends.json>;
.

<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#DCATSourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{$.id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:graphMap [ a rml:GraphMap;
      rml:constant ex:PeopleGraph;
      rml:logicalTarget <#TargetDump2>;
    ];
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
      rml:logicalTarget <#TargetDump1>;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.

<#TargetDump1> a rml:LogicalTarget;
  rml:target [ a rml:Target, dcat:Distribution;
    dcat:downloadURL <file://./dump1.nq>;
  ];
  rml:serialization formats:N-Quads;
.

<#TargetDump2> a rml:LogicalTarget;
  rml:target [ a rml:Target, dcat:Distribution;
    dcat:downloadURL <file://./dump2.nq>;
  ];
  rml:serialization formats:N-Quads;
.

```

**Output 1**
```

```

**Output 2**
```
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" <http://example.org/PeopleGraph>.
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" <http://example.org/PeopleGraph> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" <http://example.org/PeopleGraph> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" <http://example.org/PeopleGraph> .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" <http://example.org/PeopleGraph> .

```

**Output 3**
```
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller" <http://example.org/PeopleGraph> .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green" <http://example.org/PeopleGraph> .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani" <http://example.org/PeopleGraph> .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing" <http://example.org/PeopleGraph> .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller" <http://example.org/PeopleGraph> .

```

