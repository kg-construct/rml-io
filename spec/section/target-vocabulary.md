## Logical Target vocabulary {#target-vocabulary}

The LogicalTarget vocabulary namespace is http://w3id.org/rml/
and it's prefix is `rml`.

The LogicalTarget vocabulary consists of `rml:LogicalTarget` and `rml:Target` 
classes to describe how a knowledge graph must be exported after generation. 
 
### Defining Logical Targets {#defining-targets}

A Logical Target is any target to where RDF triples are exported to.

| Property                    | Domain               | Range               |
| --------------------------- | -------------------- | ------------------- |
| `rml:target`                | `rml:LogicalTarget`  | `Target`            |

- The target access description (`rml:target`) MUST specify how to access
the target through an `rml:Target`.
The Target definition requires only the target (`rml:target`) to be specified, 
all other properties are optional.

### Target 

A Target describes how a target must be accessed when exporting RDF triples.
An external vocabulary such as DCAT, VoID, SD is allowed here. 
If a target cannot be accessed with existing vocabulary, a custom vocabulary 
can be used, for example: handling an authentication flow may be specific 
for that specific target. A custom ontology can be used here to describe 
this authentication flow.

A Target (`rml:Target`) MAY contain the following properties:
 
- The **serialization format** (`rml:serialization`) MAY specify 
the serialization format for exporting a knowledge graph. 
The serialization format is described using the W3C 
[formats](https://www.w3.org/ns/formats/) namespace. 
By default, the serialization format is N-Quads [[N-Quads]].
- The **compression algorithm** (`rml:compression`) MAY describe 
the compression algorithm to apply when exporting a knowledge graph.
By default, no compression is applied.
- The **encoding** (`rml:encoding`) MAY specify which encoding must be used
when exporting a knowledge graph.
By default, UTF-8 is used.

| Property             | Domain               | Range             |
| -------------------- | -------------------- | ----------------- |
| `rml:serialization`  | `rml:LogicalTarget`  | `formats:Format`  |
| `rml:compression`    | `rml:LogicalTarget`  | `rml:Compression` |
| `rml:encoding`       | `rml:LogicalTarget`  | `rml:Encoding`    |

<figure>
  <img src="./resources/images/target-structure.png" alt="Logical Target structure"/>
  <figcaption>The structure of Logical Target</figcaption>
</figure>

#### Serialization formats

Each Target MAY describe the serialization format 
with `rml:serialization` to use when exporting RDF triples to a Target.
The possible formats are defined in the W3C 
[formats](https://www.w3.org/ns/formats/) namespace 
such as N-Quads, N-Triples, JSON-LD, Turtle, etc.
If unspecified, the default format is N-Quads [[N-Quads]].

#### Compression formats

Each Target MAY specify the compression with `rml:compression`
to apply when exporting RDF triples to a Target for saving storage space.
Several compression formats are specified by the `comp` namespace:

- `rml:none`: No compression is applied
- `rml:gzip`: GZip compression
- `rml:zip`: Zip archive with Zip compression
- `rml:tarXz`: Tar archive with Xz compression
- `rml:tarGz`: Tar archive with GZip compression

If unspecified, the default value is no compression.
This namespace is NOT limited to the listed compression formats 
and MAY be extended in the future.

#### Encoding formats

Each Target MAY describe the encoding format to use when exporting
RDF triples to a Target. Several encoding formats are defined by the `enc`
namesapce:

- `rml:UTF-8`: UTF-8 encoding
- `rml:UTF-16`: UTF-16 encoding

If unspecified, the default value is UTF-8.
This namespace is NOT limited to the listed compression formats 
and MAY be extended in the future.

#### Examples {#target-examples}

The following example show a Target of an RDF dump in Turtle [[Turtle]] 
format with GZip compression and UTF-8 encoding:

<pre class="ex-target">
&lt;#VoIDDump&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, void:Dataset;
        void:dataDump &lt;file:///data/dump.ttl&gt;;
        rml:compression rml:gzip;
        rml:encoding rml:UTF-8;
    ];
    rml:serialization formats:Turtle;
.
</pre>

The following example shows a Target of a [[SPARQL]] 
endpoint with `SPARQL UPDATE`:

<pre class="ex-target">
&lt;#SPARQLEndpoint&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, sd:Service;
        sd:endpoint  &lt;http://example.com/sparql-update&gt;;
        sd:supportedLanguage sd:SPARQL11Update ;
    ];
.
</pre>

The following example shows a Target of a 
DCAT dataset in N-Quads format with Zip compression:

<pre class="ex-target">
&lt;#DCATDump&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, dcat:Distribution;
        dcat:accessURL &lt;http://example.org/dcat-access-url&gt;;
        rml:compression rml:zip;
    ];
    rml:serialization formats:N-Quads;
.
</pre>

The following example shows a Target of a
MQTT stream in N-Quads format without compression:

<pre class="ex-target">
&lt;#MQTTStream&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "mqtt://localhost/topic";
                hctl:forContentType "application/n-quads";
                # Set MQTT parameters through W3C WoT Binding Template for MQTT
                mqv:controlPacketValue "SUBSCRIBE";
                mqv:options ([ mqv:optionName "qos"; mqv:optionValue "1" ] [ mqv:optionName "dup" ]);
            ];
        ];
    ];
    rml:serialization formats:N-Quads;
.
</pre>

The following example shows a Target of a
TCP stream in N-Quads format without compression:

<pre class="ex-target">
&lt;#TCPStream&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "tcp://localhost:1234/topic";
                hctl:forContentType "application/n-quads";
            ];
        ];
    ];
    rml:serialization formats:N-Quads;
.
</pre>

The following example shows a Target of a
Kafka stream in N-Quads format without compression:

<pre class="ex-target">
&lt;#KafkaStream&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "kafka://localhost:8089/topic";
                hctl:forContentType "application/n-quads";
                # Kafka parameters through W3C WoT Binding Template for Kafka
                kafka:groupId "MyAwesomeGroup";
            ];
        ];
    ];
    rml:serialization formats:N-Quads;
.
</pre>

The following example shows a Target of a
HTTP Web API in N-Quads format without compression and
the User Agent HTTP header set to 'Processor':

<pre class="ex-target">
&lt;#HTTPWebAPI&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "http://localhost:4242/";
                hctl:forContentType "application/n-quads";
                # Set HTTP method and headers through W3C WoT Binding Template for HTTP
                htv:methodName "POST";
                htv:headers ([
                    htv:fieldName "User-Agent";
                    htv:fieldValue "Processor";
                ]);
            ];
        ];
    ];
    rml:serialization formats:N-Quads;
.
</pre>

The following example shows a Target of a
HTTP Server Sent Events stream in N-Quads format without compression:

<pre class="ex-target">
&lt;#HTTPSSEStream&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "http://localhost:4242/";
                hctl:forContentType "text/event-stream";
            ];
        ];
    ];
    rml:serialization formats:N-Quads;
.
</pre>

The following example shows a Target of a
WebSocket in N-Quads format without compression:

<pre class="ex-target">
&lt;#HTTPSSEStream&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "ws://localhost:5555/";
                hctl:forContentType "application/n-quads";
            ];
        ];
    ];
    rml:serialization formats:N-Quads;
.
</pre>
