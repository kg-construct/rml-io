# RMLSTC0007c

Test source with XPath reference formulation

**Error expected?** Yes

**Input**
```
<Friends>
  <Character id="0">
    <name>Monica Geller</name>
    <age>33</age>
  </Character>
  <Character id="1">
    <name>Rachel Green</name>
    <age>34</age>
  </Character>
  <Character id="2">
    <name>Joey Tribbiani</name>
    <age>35</age>
  </Character>
  <Character id="3">
    <name>Chandler Bing</name>
    <age>36</age>
  </Character>
  <Character id="4">
    <name>Ross Geller</name>
    <age>37</age>
  </Character>
</Friends>

```

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@base <http://example.com/rules/> .

<#DCATSourceAccess> a rml:Source, dcat:Distribution;
  dcat:downloadURL <http://w3id.org/rml/resources/rml-io/RMLSTC0007c/Friends.xml>;
.

<#TriplesMap> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source <#DCATSourceAccess>;
    rml:referenceFormulation rml:XPath;
    rml:iterator "//Friends/Character";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{@id}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:name;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "name/text()";
    ];
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant foaf:age;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "age/text()";
    ];
  ];
.

```

**Output**
```
<http://example.org/0> <http://xmlns.com/foaf/0.1/age> "33" .
<http://example.org/0> <http://xmlns.com/foaf/0.1/name> "Monica Geller" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/age> "34" .
<http://example.org/1> <http://xmlns.com/foaf/0.1/name> "Rachel Green" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/age> "35" .
<http://example.org/2> <http://xmlns.com/foaf/0.1/name> "Joey Tribbiani" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/age> "36" .
<http://example.org/3> <http://xmlns.com/foaf/0.1/name> "Chandler Bing" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/age> "37" .
<http://example.org/4> <http://xmlns.com/foaf/0.1/name> "Ross Geller" .

```

