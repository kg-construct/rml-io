## RMLTTC0004a

**Title**: Target JSON-LD

**Description**: Test export all triples as JSON-LD

**Error expected?** No

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLTTC0004a/Friends.json](http://w3id.org/rml/resources/rml-io/RMLTTC0004a/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
    dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLTTC0004a/Friends.json>;
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
    dcat:downloadURL <file://./dump1.jsonld>;
  ];
  rml:serialization formats:JSON-LD;
.

```

**Output 1**
```

```

**Output 2**
```
{
  "@context": { 
    "foaf": "http://xmlns.com/foaf/0.1/"
  },
  "@graph": [
    {                                                                                

      "@id": "http://example.org/0",
      "foaf:name": "Monica Geller",
      "foaf:age": "33"
    },
    {                                                                                
      "@id": "http://example.org/1",
      "foaf:name": "Rachel Green",
      "foaf:age": "34"
    },
    {                                                                                
      "@id": "http://example.org/2",
      "foaf:name": "Joey Tribbiani",
      "foaf:age": "35"
    },
    {                                                                                
      "@id": "http://example.org/3",
      "foaf:name": "Chandler Bing",
      "foaf:age": "36"
    },
      {                                                                                
      "@id": "http://example.org/4",
      "foaf:name": "Ross Geller",
      "foaf:age": "37"
    }
  ]
}

```

