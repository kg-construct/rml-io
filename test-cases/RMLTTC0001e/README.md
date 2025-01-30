## RMLTTC0001e

**Title**: Single Target: Language Map

**Description**: Test exporting all triples with a given language tag to a single Target.

**Error expected?** No

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLTTC0001e/Friends.json](http://w3id.org/rml/resources/rml-io/RMLTTC0001e/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
    dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLTTC0001e/Friends.json>;
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
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "$.name";
      rml:languageMap [ a rml:LanguageMap;
        rml:constant "en";
        rml:logicalTarget <#TargetDump1>;
      ];
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
    dcat:downloadURL <file://./dump1.nq>;
  ];
  rml:serialization formats:N-Quads;
.

```

**Output 1**
```
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33".
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34".
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35".
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36".
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37".

```

**Output 2**
```
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller"@en .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green"@en .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani"@en .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing"@en .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller"@en .

```

