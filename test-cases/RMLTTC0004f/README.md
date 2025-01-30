## RMLTTC0004f

**Title**: Target RDF/XML

**Description**: Test export all triples as RDF/XML

**Error expected?** Yes

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLTTC0004f/Friends.json](http://w3id.org/rml/resources/rml-io/RMLTTC0004f/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
    dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLTTC0004f/Friends.json>;
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
    dcat:downloadURL <file://./dump1.rdfxml>;
  ];
  rml:serialization formats:RDF_XML;
.

```

**Output 1**
```

```

**Output 2**
```
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/">
  <rdf:Description rdf:about="http://example.org/0">
    <foaf:age>33</foaf:age>
    <foaf:name>Monica Geller</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/1">
    <foaf:age>34</foaf:age>
    <foaf:name>Rachel Green</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/2">
    <foaf:age>35</foaf:age>
    <foaf:name>Joey Tribbiani</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/3">
    <foaf:age>36</foaf:age>
    <foaf:name>Chandler Bing</foaf:name>
  </rdf:Description>
  <rdf:Description rdf:about="http://example.org/4">
    <foaf:age>37</foaf:age>
    <foaf:name>Ross Geller</foaf:name>
  </rdf:Description>
</rdf:RDF>

```

