## RMLSTC0012e

**Title**: Complex XML source

**Description**: Tests the generation of triples from complex XML sources

**Error expected?** No

**Input**
 [http://w3id.org/rml/resources/rml-io/RMLSTC0012e/Friends.json](http://w3id.org/rml/resources/rml-io/RMLSTC0012e/Friends.json)

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <http://example.com/> .
@base <http://example.com/rules/> .

<#TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source [ a rml:FilePath;
      rml:root rml:MappingDirectory;
      rml:path "companies.xml";
    ];
    rml:referenceFormulation rml:XPath;
    rml:iterator "/companies/company/departments/department/employees/employee";
  ];
  rml:subjectMap [ a rml:SubjectMap;
    rml:template "http://example.org/{name}";
  ];
  rml:predicateObjectMap [ a rml:PredicateObjectMap;
    rml:predicateMap [ a rml:PredicateMap;
      rml:constant ex:skill;
    ];
    rml:objectMap [ a rml:ObjectMap;
      rml:reference "skills/skill";
    ];
  ].

```

**Output**
```
<http://example.org/Bob%20Smith> <http://example.com/employee> "AWS" .
<http://example.org/Bob%20Smith> <http://example.com/employee> "JavaScript" .
<http://example.org/Bob%20Smith> <http://example.com/employee> "Python" .
<http://example.org/Eve%20Davis> <http://example.com/employee> "Docker" .
<http://example.org/Eve%20Davis> <http://example.com/employee> "Kubernetes" .
<http://example.org/Eve%20Davis> <http://example.com/employee> "Terraform" .
<http://example.org/Liam%20Brown> <http://example.com/employee> "Deep Learning" .
<http://example.org/Liam%20Brown> <http://example.com/employee> "Machine Learning" .
<http://example.org/Liam%20Brown> <http://example.com/employee> "Python" .
<http://example.org/Olivia%20Martinez> <http://example.com/employee> "CRM" .
<http://example.org/Olivia%20Martinez> <http://example.com/employee> "Lead Generation" .
<http://example.org/Olivia%20Martinez> <http://example.com/employee> "Negotiation" .
<http://example.org/Sarah%20Lee> <http://example.com/employee> "Copywriting" .
<http://example.org/Sarah%20Lee> <http://example.com/employee> "Google Ads" .
<http://example.org/Sarah%20Lee> <http://example.com/employee> "SEO" .
<http://example.org/Sophia%20White> <http://example.com/employee> "Data Analysis" .
<http://example.org/Sophia%20White> <http://example.com/employee> "R" .
<http://example.org/Sophia%20White> <http://example.com/employee> "SQL" .

```

