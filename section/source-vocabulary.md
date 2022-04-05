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
  <img src="./resources/images/source-structure.png" alt="Source structure"/>
  <figcaption>The structure of Source</figcaption>
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

### Examples {#examples}

The following example show a Source of an CSV file.

<pre class="ex-source">
&lt;#CSV&gt; a rml:LogicalSource;
     rml:source [ a csvw:Table;
         csvw:url "/path/to/data.csv";
     ];
     rml:referenceFormulation ql:CSV;
.
</pre>

Note that there is not `rml:iterator` is present because its default is row.

The following example shows a Source specified for a database.

<pre class="ex-source">
&lt;#RDB&gt; a rml:LogicalSource;
     rml:source [ a d2rq:Database;
        d2rq:jdbcDSN "jdbc:mysql://localhost/example";
        d2rq:jdbcDriver "com.mysql.jdbc.Driver";
        d2rq:username "user";
        d2rq:password "password";
     ];
     rml:referenceFormulation ql:SQL2008;
.
</pre>

Note that there is not `rml:iterator` is present because its default is row.

The following example shows a Source of a 
XML file

<pre class="ex-source">
&lt;#XML&gt; a rml:LogicalSource;
     rml:source [ a dcat:Dataset;
       dcat:distribution [ a dcat:Distribution;
         dcat:accessURL &lt;file:///path/to/data.xml&gt;;
       ];
     ];
     rml:referenceFormulation ql:XPath;
     rml:iterator "/xpath/iterator/expression";
.
</pre>

<pre class="ex-source">
&lt;#JSON&gt; a rml:LogicalSource;
     rml:source [ a dcat:Dataset;
       dcat:distribution [ a dcat:Distribution;
         dcat:accessURL &lt;file:///path/to/data.json&gt;;
       ];
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
</pre>
