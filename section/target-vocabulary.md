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
- The **encoding** (`rmlt:encoding`) MAY specify which encoding must be used
when exporting a knowledge graph.
The encoding is specified through 
[enc](http://semweb.mmlab.be/ns/rml-compression#) namespace.

The Target definition requires only the target (`rmlt:target`) to be specified, 
all other properties are optional.

| Property             | Domain               | Range              |
| -------------------- | -------------------- | ------------------ |
| `rmlt:target`        | `rmlt:LogicalTarget` | `URI or Literal`   |
| `rmlt:serialization` | `rmlt:LogicalTarget` | `formats:Format`   |
| `rmlt:compression`   | `rmlt:LogicalTarget` | `comp:Compression` |
| `rmlt:encoding`      | `rmlt:LogicalTarget` | `enc:Encoding`     |

<figure>
  <img src="./resources/images/structure.png" alt="Target structure"/>
  <figcaption>The structure of Target</figcaption>
</figure>

### Examples {#examples}

The following example show a Target of an RDF dump in Turtle [[Turtle]] 
format with GZip compression and UTF-8 encoding:

<pre class="ex-target">
&lt;#VoIDDump&gt; a rmlt:LogicalTarget;
     rmlt:target [ a void:Dataset;
         void:dataDump &lt;file:///data/dump.ttl&gt;;
     ];
     rmlt:serialization formats:Turtle;
     rmlt:compression comp:gzip;
     rmlt:encoding enc:UTF-8;
.
</pre>

The following example shows a Target of a [[SPARQL]] 
endpoint with `SPARQL UPDATE`:

<pre class="ex-target">
&lt;#SPARQLEndpoint&gt; a rmlt:LogicalTarget;
     rmlt:target [ a sd:Service;
       sd:endpoint  &lt;http://example.com/sparql-update&gt;;
       sd:supportedLanguage sd:SPARQL11Update ;
     ];
.
</pre>

The following example shows a Target of a 
DCAT dataset in N-Quads format with Zip compression:

<pre class="ex-target">
&lt;#DCATDump&gt; a rmlt:LogicalTarget;
     rmlt:target [ a dcat:Dataset;
         dcat:distribution [ a dcat:Distribution;
	        dcat:accessURL &lt;http://example.org/dcat-access-url&gt;;
         ];
     ];
     rmlt:serialization formats:N-Quads;
     rmlt:compression comp:zip;
.
</pre>
