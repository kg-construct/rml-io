## Target in RML {#target-in-rml}

RML does not specify where generated triples are exported to, 
each RML processor has its own way to describe this information 
through configuration files or command line parameters. 
To incorporate this information in the RML mapping rules, 
RML is aligned with the 
[Target vocabulary](http://semweb.mmlab.be/ns/rml-target#)
which describes how the generated triples are exported. 
RML is aligned with the Target vocabulary 
by extending `rr:TermMap` with the `rml:logicalTarget` property 
to describe on Term Map [[RML]] level where each triple must be directed to. 
A Term Map is a function that generates an RDF term 
from a logical reference [[RML]].
The result of that function is known as the term map's generated 
RDF term [[RDF-Concepts]] 
such as subjects, predicates, objects, named graphs and language tags.

A Term Map MAY also contain zero or more `rml:logicalTarget` properties 
to export all triples containing the generated term to different targets. 
The same Term Map can have multiple targets by specifying 
multiple `rml:logicalTarget` properties in the Term Map. 

Multiple Targets MAY be combined by specifying multiple Targets 
in the same Term Map or multiple Term Maps of the same RDF triple (see [[[!#multiple-targets]]]). 

```turtle "example": " "
<#TriplesMap> a rr:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
    rml:source [ a csvw:Table;
      csvw:url "http://rml.io/data/csvw/Airport.csv";
      csvw:dialect [ a csvw:Dialect;
        csvw:delimiter ";”;
        csvw:encoding "UTF-8";
        csvw:header "1"^^xsd:boolean;
      ];
    ];
  ];
  rr:subjectMap [ a rr:SubjectMap;
    rr:template "http://example.com/{id}";
    rml:logicalTarget [ a rmlt:LogicalTarget;
      rmlt:target [ a void:Dataset
        void:dataDump <file:///data/dump1.nq>;
      ];
      rmlt:serialization formats:N-Quads;
    ];
  ];
  rr:predicateObjectMap [ a rr:PredicateObjectMap;
    rr:predicateMap [ a rr:PredicateMap;
      rr:constant foaf:name;
      rml:logicalTarget [ a rmlt:LogicalTarget;
         rmlt:target [ a void:Dataset
           void:dataDump <file:///data/dump2.ttl>;
         ];
         rmlt:serialization formats:Turtle;
         rmlt:compression comp:Zip;
      ];
    ];
    rr:objectMap [ a rr:ObjectMap;
      rml:reference "name";
    ];
  ];
.
```

If the mapping document contains no Targets, 
the processor falls back to the default target, 
as it is specified through the processor's 
specific configuration file or command line parameters. 
If a mapping document contains at least one Target, 
the processor will export the triples to these Targets,
triples which do not have one or more Target(s) assigned,
are exported to the default target of the processor.

| Property            | Domain       | Range                |
| ------------------- | ------------ | -------------------- |
| `rml:logicalTarget` | `rr:TermMap` | `rmlt:LogicalTarget` |
