## Logical Source vocabulary {#source-vocabulary}

The LogicalSource vocabulary namespace is http://w3id.org/rml/
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
By default `rml:SQL2008Query` for databases,
`rml:CSV` for CSV and TSV data sources.
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
  - In the case of databases, CSV or TSV data sources, the value of 
  `rml:iterator` is considered a "row" and must not be specified.
  - In the case of XML and JSON data sources, it is a valid reference
  to an element or an object respectively considering the reference
  formulation specified.

The Logical Source definition requires only the source (`rml:source`)
to be specified, all other properties are optional.
If a property is specified, it MUST NOT be specified multiple times.

| Property                    | Domain               | Range                     |
| --------------------------- | -------------------- | ------------------------- |
| `rml:source`                | `rml:LogicalSource`  | `IRI`                     |
| `rml:referenceFormulation`  | `rml:LogicalSource`  | `rml:ReferenceFormulation` |
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

- `rml:CSV`: CSV or TSV data sources
- `rml:JSONPath`: JSON documents
- `rml:XPath`: XML documents, a shortcut for `rml:XPathReferenceFormulation`
with default parameters
- `rml:XPathReferenceFormulation`: XML documents with optionally
the definition of XML namespaces used in references.
By default, no namespaces are defined.
- `rml:SQL2008Query`: SQL query for a relational database.
- `rml:SQL2008Table`: Shortcut to select all columns from a SQL table.

`rml:XPathReferenceFormulation` may specify zero or more 
`rml:namespace` properties with a `rml:Namespace`.
A `rml:Namespace` contains the following required properties:
 - `rml:namespacePrefix`: A Literal with the prefix used for the XML namespace.
 - `rml:namespaceURL`: A Literal with the URL identifying the XML namespace.

SPARQL queries iterations can be specified by using the W3C Formats namespace:

- `formats:SPARQL_Results_CSV`: SPARQL results as CSV.
- `formats:SPARQL_Results_TSV`: SPARQL results as TSV.
- `formats:SPARQL_Results_JSON`: SPARQL results as JSON.
- `formats:SPARQL_Results_XML`: SPARQL results as XML.

<pre class="ex-source">
&lt;#XMLNamespace&gt; a rml:LogicalSource;
     rml:source [ a rml:Source, dcat:Distribution;
         dcat:accessURL &lt;file:///path/to/data.xml&gt;;
     ];
     rml:referenceFormulation [ a rml:XPathReferenceFormulation;
       rml:namespace [ a rml:Namespace;
         rml:namespacePrefix "ex";
         rml:namespaceURL "http://example.org";
       ];
     ];
     rml:iterator "/xpath/ex:namespace/expression";
.
</pre>

Since `rml:source` is open to any IRI, you can implement your own source access
description for sources that are not covered by existing vocabularies such as
paginated Web APIs which implement pagination in a Web API specific way.

### Source

A Source (`rml:Source`) defines how a data source should be accessed.
It complements other source descriptions 
such as SD Service, CSVW Table, DCAT Distribution, etc.
to support encoding, null values, compression, and other access properties.
The properties of a Source take precedence over the properties of other source
descriptions, for example: `rml:encoding` takes precedence over `csvw:encoding`
if both are specific.

Optionally, the following properties MAY be specified:

- **rml:encoding** specifies the encoding of the data inside the source.
Defaults to `rml:UTF-8` if not specified.
- **rml:null** describes which data values inside the source
should be considered as NULL.
Defaults to the default NULL character if available.
If none is available such as CSV, no values are considered NULL,
unless specified.
- **rml:null** indicate which data values inside the source 
should be considered as NULL values.
The value for this predicate defaults to the default NULL token 
of the underlying data model (e.g., NULL in relational databases 
and null in JSON) and are always processed as such.
Some data models have no such default NULL token, such as CSV.
When that is the case, then nothing is considered NULL unless specified by
`rml:null`.
Example: CSV does not have a default NULL character,
so no value is considered NULL.
However, JSON has a NULL character specified: `null`,
this one is used together with the ones specified through `rml:null`.
For a relational database, `rml:null "foo"` results into the following values
considered as NULL: `{NULL, "foo"}` where `NULL` comes from the relational 
database model as NULL value.
- **rml:compression** specifies if the source is compressed
and the used compression algorithm. Defaults to no compression.

<pre class="ex-source">
&lt;#JSON&gt; a rml:LogicalSource;
     rml:source [ a rml:Source, dcat:Distribution;
       dcat:accessURL &lt;file:///path/to/data.json.gz&gt;;
       rml:null ""; # empty string as NULL besides default null character
       rml:compression rml:gzip; # GZip compression
       rml:encoding rml:UTF-16; # UTF-16 encoding
     ];
     rml:referenceFormulation rml:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
</pre>

| Property                    | Domain               | Range                     |
| --------------------------- | -------------------- | ------------------------- |
| `rml:encoding`              | `rml:Source`         | `rml:Encoding`            |
| `rml:null`                  | `rml:Source`         | `Literal`                 |
| `rml:compression`           | `rml:Source`         | `rml:Compression`         |

#### NULL values

Each Source MAY describe the values that should be considered as NULL
with `rml:null`, similar to `NULL` in relational databases.
By default, standardized NULL values are always considered,
but additional ones can be specified. Multiple NULL values are allowed.
For example, in relational databases `NULL` is always considered as a NULL
value while also an empty column can be considered as a NULL value by
specifying it through `rml:null` in a Source.

#### Compression formats

Each Source MAY specify the compression with `rml:compression`
to apply when exporting RDF triples to a Source for saving storage space.
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

Each Source MAY describe the encoding format to use when exporting
RDF triples to a Source. Several encoding formats are defined by the `enc`
namesapce:

- `rml:UTF-8`: UTF-8 encoding
- `rml:UTF-16`: UTF-16 encoding

If unspecified, the default value is UTF-8.
This namespace is NOT limited to the listed compression formats 
and MAY be extended in the future.

### Examples {#source-examples}

The following example show a Source of an CSV file.

<pre class="ex-source">
&lt;#CSV&gt; a rml:LogicalSource;
     rml:source [ a rml:Source, csvw:Table;
        csvw:url "/path/to/data.csv";
        rml:null "NULL";
        rml:null "";
     ];
     rml:referenceFormulation rml:CSV;
.
</pre>

Note that there is no `rml:iterator` present because its default is row.
This particular CSV file has 2 different ways to specify a NULL value: `NULL` 
or an empty value. Implementations need to check if a value is equal to one of 
the values defined by `rml:null` to check for NULL values in the data.

The following example shows a Source specified for a MySQL database querying 
the `student` table. The database username and password are provided as well.

<pre class="ex-source">
&lt;#RDB&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, d2rq:Database;
        d2rq:jdbcDSN "jdbc:mysrml://localhost/example";
        d2rq:jdbcDriver "com.mysql.jdbc.Driver";
        d2rq:username "user";
        d2rq:password "password";
    ];
    rml:iterator "SELECT * FROM student;";
    rml:referenceFormulation rml:SQL2008Query;
.
</pre>

A shortcut is available to select all columns from a table,
such as in the example above, by using the `rml:SQL2008Table`
as `rml:referenceFormulation`.

The following example shows a Source of a 
XML file with no compression.

<pre class="ex-source">
&lt;#XML&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, dcat:Distribution;
        dcat:accessURL &lt;file:///path/to/data.xml&gt;;
    ];
    rml:referenceFormulation rml:XPath;
    rml:iterator "/xpath/iterator/expression";
.
</pre>

The following example is GZip compressed JSON file as Source:

<pre class="ex-source">
&lt;#JSON&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, dcat:Distribution;
        dcat:accessURL &lt;file:///path/to/data.json.gz&gt;;
        rml:compression rml:gzip;
     ];
     rml:referenceFormulation rml:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
</pre>

Sources can also describe access to SPARQL endpoints with the 
W3C Service Description ontology. SPARQL endpoints need a SPARQL query, 
to iterate over.

<pre class="ex-source">
&lt;#SPARQLEndpoint&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, sd:Service;
        sd:endpoint  &lt;http://example.com/sparql&gt;;
        sd:supportedLanguage sd:SPARQL11Query;
    ];
    rml:iterator "CONSTRUCT WHERE { ?s ?p ?o. } LIMIT 100";
    rml:referenceFormulation formats:SPARQL_Results_CSV;
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
    rml:source [ a rml:Source, td:Thing;
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
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.jsonpath";
.
</pre>

The following example shows a Source of a
HTTP Server Sent Events stream in XML format without compression:

<pre class="ex-source">
&lt;#HTTPSSEStream&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "http://localhost:4242/";
                hctl:forContentType "text/event-stream";
            ];
        ];
    ];
    rml:referenceFormulation rml:XPath;
    rml:iterator "/my/xpath";
.
</pre>

The following example shows a Source of a
MQTT stream in JSON format without compression:

<pre class="ex-source">
&lt;#MQTTStream&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, td:Thing;
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
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.jsonpath";
.
</pre>

The following example shows a Source of a
TCP stream in JSON format without compression:

<pre class="ex-source">
&lt;#TCPStream&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, td:Thing;
        td:hasPropertyAffordance [
            td:hasForm [
                # URL and content type
                hctl:hasTarget "tcp://localhost:1234/topic";
                hctl:forContentType "application/json";
            ];
        ];
    ];
    rml:referenceFormulation rml:JSONPath;
    rml:iterator "$.jsonpath";
.
</pre>

The following example shows a Source of a
Kafka stream in XML format without compression:

<pre class="ex-source">
&lt;#KafkaStream&gt; a rml:LogicalSource;
    rml:source [ a rml:Source, td:Thing;
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
    rml:referenceFormulation rml:XPath;
    rml:iterator "/my/xpath";
.
</pre>

Relative paths to files are covered by a source access description included
in this specification which subclasses `rml:Source` as `rml:RelativePathSource`.
This access description allows accessing files relative from:

- `rml:CurrentWorkingDirectory`: relative to the current working directory of the RML processor.
- `rml:MappingDirectory`: relative to the location of the RML mapping.
- A string Literal: a string describing an absolute path against which relative paths are resolved, similar to the Base URI in [RFC3986](https://www.rfc-editor.org/rfc/rfc3986).

| Property    | Domain                    | Range                                                              |
| ----------- | ------------------------- | ------------------------------------------------------------------ |
| `rml:root`  | `rml:RelativePathSource`  | `rml:CurrentWorkingDirectory`, `rml:MappingDirectory` or `Literal` |
| `rml:path`  | `rml:RelativePathSource`  | `Literal`                                                          |

Example of accessing a CSV file relative to the current working directory.
The file's absolute path is `$CURRENT_WORKING_DIR/file.csv` where `$CURRENT_WORKING_DIR` is
the location of the RML mapping.

<pre class="ex-source">
&lt;#RelativePathCWD&gt; a rml:LogicalSource;
  rml:source [ a rml:RelativePathSource, rml:Source;
    rml:root rml:CurrentWorkingDirectory;
    rml:path "./file.csv";
  ];
.
</pre>

Example of accessing a JSON file relative to the path of the mapping.
The file's absolute path is `$MAPPING_DIR/file.json` where `$MAPPING_DIR` is
the location of the RML mapping.

<pre class="ex-source">
&lt;#RelativePathMapping&gt; a rml:LogicalSource;
  rml:source [ a rml:RelativePathSource, rml:Source;
    rml:root rml:MappingDirectory;
    rml:path "./file.json";
  ];
  rml:referenceFormulation rml:JSONPath;
  rml:iterator "$";
.
</pre>

Example of accessing an XML file relative to an absolute root path
specified by a string Literal. The file's absolute path is `/root/file.xml`.

<pre class="ex-source">
&lt;#RelativePathLiteral&gt; a rml:LogicalSource;
  rml:source [ a rml:RelativePathSource, rml:Source;
    rml:root "/root";
    rml:path "file.xml";
  ];
  rml:referenceFormulation rml:JSONPath;
  rml:iterator "$";
.
</pre>
