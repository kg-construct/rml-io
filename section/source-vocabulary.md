## Logical Source vocabulary {#source-vocabulary}

The LogicalSource vocabulary namespace is http://semweb.mmlab.be/ns/rml-source# 
and it's prefix is `rml`.

The Logical Source vocabulary consists of 2 classes: 

1. `rml:LogicalSource` describes how data of a source can be referenced.
2. `rml:Source` describes how a source can be accessed, it is part of a `rml:LogicalSource`.

### Defining Logical Sources {#defining-logical-sources}

A Logical Source is any data source providing data to be mapped to RDF triples.

A Logical Source (`rml:LogicalSource`) MUST contains the following properties:

- The **source** (`rml:source`) specifies how a source is accessed through a `rml:Source`.
- The **reference formulation** (`rml:referenceFormulation`)
defines the reference formulation used to refer to the elements
of a data source.
The reference formulation must be specified in the case of databases,
CSV, TSV, XML, and JSON data sources.
By default `rr:SQL2008` for databases, `ql:CSV` for CSV and TSV data sources.
XPath for XML and JSONPath for JSON and JSONL data sources.

The following properties MAY be specified in a Logical Source:

- The **logical iterator** (`rml:iterator`)
defines the iteration loop used to map the data of the input source. 
The iterator defines how to refer to any of the following:
    - a row in the case of databases, CSV or TSV data sources
    - a repetition pattern expressed as an element in the case of XML documents,
    - a repetition pattern expressed as an object in the case
    of a JSON data sources. 
    - etc...

By default, the iterator is considered a row, if not specified:
  - In the case of databases, CSV or TSV data sources,
  the value of the `rml:iterator`, if not specified, is a "row". 
  - In the case of XML and JSON data sources,
  it is a valid reference to an element or an object respectively
  considering the reference formulation specified. 

The Logical Source definition requires only the source (`rml:source`)
to be specified, all other properties are optional.
If a property is specified, it MUST NOT be specified multiple times.

| Property                    | Domain               | Range                     |
| --------------------------- | -------------------- | ------------------------- |
| `rml:source`                | `rml:LogicalSource`  | `Source`                  |
| `rml:referenceFormulation`  | `rml:LogicalSource`  | `ql:ReferenceFormulation` |
| `rml:iterator`              | `rml:LogicalSource`  | `Literal`                 |

<figure>
  <img src="./resources/images/source-structure.png" alt="Logical Source structure"/>
  <figcaption>The structure of Logical Source</figcaption>
</figure>

#### Reference formulations

Each Logical Source has a reference formulation to define how to reference
to elements of the data of the input source.
Several reference formulations (`rml:ReferenceFormulation`)
are defined in this specification:

- `rr:SQL2008`: SQL 2008 standard for relational databases
- `ql:CSV`: CSV or TSV data sources
- `ql:JSONPath`: JSON documents
- `ql:XPath`: XML documents, a shortcut for `ql:XPathReferenceFormulation`
with default parameters
- `ql:XPathReferenceFormulation`: XML documents with optionally
the definition of XML namespaces used in references.
By default, no namespaces are defined.

`ql:XPathReferenceFormulation` may specify zero or more 
`ql:namespace` properties with a `ql:Namespace`.
A `ql:Namespace` contains the following required properties:
 - `ql:namespacePrefix`: A Literal with the prefix used for the XML namespace.
 - `ql:namespaceURL`: A Literal with the URL identifying the XML namespace.

<pre class="ex-source">
&lt;#XMLNamespace&gt; a rml:LogicalSource;
     rml:source [ a rml:Source
       rml:access [ a dcat:Dataset;
         dcat:distribution [ a dcat:Distribution;
           dcat:accessURL &lt;file:///path/to/data.xml&gt;;
         ];
       ];
     ];
     rml:referenceFormulation [ a ql:XPathReferenceFormulation;
       ql:namespace [ a ql:Namespace;
         ql:namespacePrefix "ex";
         ql:namespaceURL "http://example.org";
       ];
     ];
     rml:iterator "/xpath/ex:namespace/expression";
.
</pre>

### Source

A Source (`rml:Source`) defines how a data source should be accessed.
It MUST contain the follow properties:

- **rml:access** describes where a source is located.
It is a URI [[RFC3986]] 
or Literal [[RDF-Concepts]]
that represents the input data source's location. 
External vocabulary such as DCAT, VoID, SD is allowed here. 
If a source cannot be accessed with existing vocabulary, a custom vocabulary 
can be used, for example: handling pagination in a Web API may be specific 
for that Web API. A custom ontology can be used here to describe 
that specific pagination behavior.

Optionally, the following properties MAY be specified:

- **rml:encoding** specifies the encoding of the data inside the source.
Defaults to `enc:UTF-8` if not specified.
- **rml:null** describes which data values inside the source
should be considered as NULL.
Defaults to the default NULL character if available.
If none is available such as CSV, no values are considered NULL,
unless specified.
Example: CSV does not have a default NULL character,
so no value is considered NULL.
However, JSON has a NULL character specified: `null`,
this one is used together with the ones specified through `rml:null`.
- **rml:compression** specifies if the source is compressed
and the used compression algorithm. Defaults to no compression.
- **rml:query** defines which query should be applied on the source 
during access. Example: SPARQL query for a SPARQL endpoint or a SQL query
for a relational database. Defaults to an empty string.
This property is a broader version of `rr:sqlQuery`.
A whole table or view of a relational database can be specified
through a `SELECT * FROM {table}` query (`rr:tableName` compatibility).

<pre class="ex-source">
&lt;#JSON&gt; a rml:LogicalSource;
     rml:source [ a rml:Source
       rml:access [ a dcat:Dataset;
         dcat:distribution [ a dcat:Distribution;
           dcat:accessURL &lt;file:///path/to/data.json.gz&gt;;
         ];
       ];
       rml:null ""; # empty string as NULL besides default null character
       rml:compression comp:gzip; # GZip compression
       rml:encoding enc:UTF-16; # UTF-16 encoding
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
</pre>

| Property                    | Domain               | Range                     |
| --------------------------- | -------------------- | ------------------------- |
| `rml:access`                | `rml:Source`         | `URI or Literal`          |
| `rml:encoding`              | `rml:Source`         | `enc:Encoding`            |
| `rml:null`                  | `rml:Source`         | `Literal`                 |
| `rml:compression`           | `rml:Source`         | `comp:Compression`        |
| `rml:query`                 | `rml:Source`         | `Literal`                 |

### Examples {#examples}

The following example show a Source of an CSV file.

<pre class="ex-source">
&lt;#CSV&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a csvw:Table;
            csvw:url "/path/to/data.csv";
        ];
        rml:null "NULL";
        rml:null "";
     ];
     rml:referenceFormulation ql:CSV;
.
</pre>

Note that there is not `rml:iterator` is present because its default is row.
This particular CSV file has 2 different ways to specify a NULL value: `NULL` 
or an empty value. Implementations need to check if a value is equal to on of 
the values defined by `rml:null` to check for NULL values in the data.

The following example shows a Source specified for a MySQL database querying 
the `student` table. The database username and password are provided as well.

<pre class="ex-source">
&lt;#RDB&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a d2rq:Database;
            d2rq:jdbcDSN "jdbc:mysql://localhost/example";
            d2rq:jdbcDriver "com.mysql.jdbc.Driver";
            d2rq:username "user";
            d2rq:password "password";
            d2rq:sqlVersion d2rq:SQL2008; # TODO: better ontology
        ];
        rml:query "SELECT * FROM student;";
     ];
.
</pre>

Note that there is not `rml:iterator` is present because its default is row.

The following example shows a Source of a 
XML file with no compression.

<pre class="ex-source">
&lt;#XML&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ 
            a dcat:Dataset;
            dcat:distribution [ a dcat:Distribution;
                dcat:accessURL &lt;file:///path/to/data.xml&gt;;
            ];
        ];
     ];
     rml:referenceFormulation ql:XPath;
     rml:iterator "/xpath/iterator/expression";
.
</pre>

The following example is GZip compressed JSON file as Source:

<pre class="ex-source">
&lt;#JSON&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a dcat:Dataset;
            dcat:distribution [ a dcat:Distribution;
                dcat:accessURL &lt;file:///path/to/data.json.gz&gt;;
            ];
        ];
        rml:compression comp:gzip;
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
</pre>

Sources can also describe access to SPARQL endpoints with the 
W3C Service Description ontology. SPARQL endpoints need a SPARQL query, 
specified by `rml:query`.

<pre class="ex-source">
&lt;#SPARQLEndpoint&gt; a rml:LogicalSource;
    rml:source [ 
        rml:access [ a sd:Service;
            sd:endpoint  &lt;http://example.com/sparql&gt;;
            sd:supportedLanguage sd:SPARQL11Query;
        ];
        rml:query "CONSTRUCT WHERE { ?s ?p ?o. } LIMIT 100";
    ];
.
</pre>

Web APIs and streams are supported through the W3C Web of Things ontologies:
- HTTP Web API
- MQTT streams
- CoAP
- Kafka
- HTTP Server Sent Events 

The following example is a HTTP JSON Web API with a HTTP header User Agent 
set to 'Processor':

<pre class="ex-source">
&lt;#HTTPWebAPI&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a td:Thing;
            td:hasPropertyAffordance [
                td:hasForm [
                    # URL and content type
                    hctl:hasTarget "http://localhost:4242/";
                    hctl:forContentType "application/json";
                    # Set HTTP method and headers through W3C WoT Binding Template for HTTP
                    htv:methodName "GET";
                    htv:headers ([
                        htv:fieldName "User-Agent";
                        htv:fieldValue "Processor";
                    ]);
                ];
            ];
        ];
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath";
.
</pre>

The following example shows a Source of a
HTTP Server Sent Events stream in XML format without compression:

<pre class="ex-source">
&lt;#HTTPSSEStream&gt; a rml:LogicalSource;
     rml:source [
        rml:access [ a td:Thing;
            td:hasPropertyAffordance [
                td:hasForm [
                    # URL and content type
                    hctl:hasTarget "http://localhost:4242/";
                    hctl:forContentType "text/event-stream";
                ];
            ];
        ];
     ];
     rml:referenceFormulation ql:XPath;
     rml:iterator "/my/xpath";
.
</pre>

The following example shows a Source of a
MQTT stream in JSON format without compression:

<pre class="ex-source">
&lt;#MQTTStream&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a td:Thing;
            td:hasPropertyAffordance [
                td:hasForm [
                    # URL and content type
                    hctl:hasTarget "mqtt://localhost/topic";
                    hctl:forContentType "application/json";
                    # Set MQTT parameters through W3C WoT Binding Template for MQTT
                    mqv:controlPacketValue "SUBSCRIBE";
                    mqv:options ([ mqv:optionName "qos"; mqv:optionValue "1" ] [ mqv:optionName "dup" ]);
                ];
            ];
        ];
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath";
.
</pre>

The following example shows a Source of a
TCP stream in JSON format without compression:

<pre class="ex-source">
&lt;#TCPStream&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a td:Thing;
            td:hasPropertyAffordance [
                td:hasForm [
                    # URL and content type
                    hctl:hasTarget "tcp://localhost:1234/topic";
                    hctl:forContentType "application/json";
                ];
            ];
        ];
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath";
.
</pre>

The following example shows a Target of a
Kafka stream in XML format without compression:

<pre class="ex-source">
&lt;#KafkaStream&gt; a rml:LogicalSource;
     rml:source [ 
        rml:access [ a td:Thing;
            td:hasPropertyAffordance [
                td:hasForm [
                    # URL and content type
                    hctl:hasTarget "kafka://localhost:8089/topic";
                    hctl:forContentType "application/xml";
                    # Kafka parameters through W3C WoT Binding Template for Kafka
                    kafka:groupId "MyAwesomeGroup";
                ];
            ];
        ];
     ];
     rml:referenceFormulation ql:XPath;
     rml:iterator "/my/xpath";
.
</pre>
