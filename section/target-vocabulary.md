## Target vocabulary {#target-vocabulary}

The Target vocabulary namespace is http://semweb.mmlab.be/ns/rml-target# 
and it's prefix is `rmlt`.

The Target vocabulary consists of a single class: `rmlt:LogicalTarget` 
to describe how a knowledge graph must be exported after generation. 

### Defining Targets {#defining-targets}

A Target is any target to where RDF triples are exported to.

A Target (`rmlt:LogicalTarget`) contains the following properties:

- The **target** (`rmlt:target`) locates the output target.
It is a URI [[RFC3986]] 
or Literal [[RDF-Concepts]]
that represents the target's location. 
External vocabulary such as DCAT, VoID, SD is allowed here. 
Each `rmlt:LogicalTarget` MUST have one `rmlt:target` property. 
The target MAY be a Literal 
containing the path the file to where the knowledge graph is exported to, 
this is allowed to stay backwards compatibility 
with existing data access descriptions.
- The **serialization format** (`rmlt:serialization`) MAY specify 
the serialization format for exporting a knowledge graph. 
The serialization format is described using the W3C 
[formats](https://www.w3.org/ns/formats/) namespace. 
By default, the serialization format is N-Quads [[N-Quads]].
- The **compression algorithm** (`rmlt:compression`) MAY describe 
the compression algorithm to apply when exporting a knowledge graph.
The compression format is specified through 
the [comp](http://semweb.mmlab.be/ns/rml-compression#) namespace.
By default, no compression is applied.

The Target definition requires only the target (`rmlt:target`) to be specified, 
all other properties are optional.

| Property             | Domain               | Range              |
| -------------------- | -------------------- | ------------------ |
| `rmlt:target`        | `rmlt:LogicalTarget` | `URI or Literal`   |
| `rmlt:serialization` | `rmlt:LogicalTarget` | `formats:Format`   |
| `rmlt:compression`   | `rmlt:LogicalTarget` | `comp:Compression` |

<figure>
  <img src="./resources/images/structure.png" alt="Target structure"/>
  <figcaption>The structure of Target</figcaption>
</figure>

### Examples {#examples}

The following example show a Target of an RDF dump in Turtle [[Turtle]] 
format with GZip compression:

```turtle "example": " "
<#VoIDDump> a rmlt:LogicalTarget;
     rmlt:target [ a void:Dataset
         void:dataDump <file:///data/dump.ttl>;
     ];
     rmlt:serialization formats:Turtle;
     rmlt:compression comp:GZip;
.
```

The following example shows a Target of a [[SPARQL]] 
endpoint with `SPARQL UPDATE`:

```turtle "example": " "
<#SPARQLEndpoint> a rmlt:LogicalTarget;
     rmlt:target [ a sd:Service;
       sd:endpoint  <http://example.com/sparql-update> ;
       sd:supportedLanguage sd:SPARQL11Update ;
     ];
.
```

The following example shows a Target of a 
DCAT dataset in N-Quads format with Zip compression:

```turtle "example": " "
<#DCATDump> a rmlt:LogicalTarget;
     rmlt:target [ a dcat:Dataset
         dcat:distribution [ a dcat:Distribution;
	        dcat:accessURL <http://example.org/dcat-access-url> ;
         ];
     ];
     rmlt:serialization formats:N-Quads;
     rmlt:compression comp:Zip;
.
```
