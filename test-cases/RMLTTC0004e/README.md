## RMLTTC0004e

**Title**: Target RDF/JSON

**Description**: Test export all triples as RDF/JSON

**Error expected?** No

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLTTC0004e/Friends.json](http://w3id.org/rml/resources/rml-io/RMLTTC0004e/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
    dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLTTC0004e/Friends.json>;
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
    dcat:downloadURL <file://./dump1.rdfjson>;
  ];
  rml:serialization formats:RDF_JSON;
.

```

**Output 1**
```

```

**Output 2**
```
{
    "http://example.org/0" : {
        "http://xmlns.com/foaf/0.1/age" : [ { "value" : "33" } ],
        "http://xmlns.com/foaf/0.1/name" : [ { "value" : "Monica Geller" } ]
    },
    "http://example.org/1" : {
        "http://xmlns.com/foaf/0.1/age" : [ { "value" : "34" } ],
        "http://xmlns.com/foaf/0.1/name" : [ { "value" : "Rachel Green" } ]
    },
    "http://example.org/2" : {
        "http://xmlns.com/foaf/0.1/age" : [ { "value" : "35" } ],
        "http://xmlns.com/foaf/0.1/name" : [ { "value" : "Joey Tribbiani" } ]
    },
    "http://example.org/3" : {
        "http://xmlns.com/foaf/0.1/age" : [ { "value" : "36" } ],
        "http://xmlns.com/foaf/0.1/name" : [ { "value" : "Chandler Bing" } ]
    },
    "http://example.org/4" : {
        "http://xmlns.com/foaf/0.1/age" : [ { "value" : "37" } ],
        "http://xmlns.com/foaf/0.1/name" : [ { "value" : "Ross Geller" } ]
    }
}

```

