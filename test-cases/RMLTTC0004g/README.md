# RMLTTC0004g

Test export all triples as Turtle

**Error expected?** Yes

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLTTC0004g/Friends.json](http://w3id.org/rml/resources/rml-io/RMLTTC0004g/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
    dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLTTC0004g/Friends.json>;
.

<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#DCATSourceAccess>;
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$[*]";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{$.id}";
    rml:logicalTarget <#TargetDump1>;
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
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
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.age";
    ];
  ];
.

<#TargetDump1> a rml:LogicalTarget;
  rml:target [ a rml:Target, dcat:Distribution;
    dcat:downloadURL <file://./dump1.ttl>;
  ];
  rml:serialization formats:Turtle;
.

```

**Output 1**
```

```

**Output 2**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.org/> .

<ex:0> <foaf:age> "33" .
<ex:0> <foaf:name> "Monica Geller" .
<ex:1> <foaf:age> "34" .
<ex:1> <foaf:name> "Rachel Green" .
<ex:2> <foaf:age> "35" .
<ex:2> <foaf:name> "Joey Tribbiani" .
<ex:3> <foaf:age> "36" .
<ex:3> <foaf:name> "Chandler Bing" .
<ex:4> <foaf:age> "37" .
<ex:4> <foaf:name> "Ross Geller" .

```

