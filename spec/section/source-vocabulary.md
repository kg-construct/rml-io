## Logical Source vocabulary {#source-vocabulary}

The Logical Source vocabulary namespace is http://w3id.org/rml/
and its prefix is `rml`.

The Logical Source vocabulary consists of 2 classes:

1. `rml:LogicalSource` describes how data of a source can be referenced.
2. `rml:Source` describes how a source can be accessed, it referenced from a `rml:LogicalSource`.

### Defining Logical Sources {#defining-logical-sources}

A <dfn>Logical Source</dfn> is an <a data-cite="RML-Core#dfn-abstract-logical-source">abstract logical source</a>
which specifies the access to a <a data-cite="RML-Core#dfn-data-source">data source</a> to be used as
input for a <a data-cite="RML-Core#dfn-triples-map">Triples Map</a>.

An [=Logical Source=] (`rml:LogicalSource`) MUST adhere to the properties defined for the
<a data-cite="RML-Core#dfn-abstract=logical-source">abstract logical source</a>.

Furthermore, an [=Logical Source=] MUST have:
- exactly one **source** (`rml:source`) property which specifies how a
<a data-cite="RML-Core#dfn-data-source">data source</a> is using a [=Source=] (`rml:Source`).

The <a data-cite="RML-Core#dfn-reference-formulation">reference formulation</a> MUST be specified in
the case that the <a data-cite="RML-Core#dfn-data-source">data source</a> is a relational database,
CSV, TSV, XML, or JSON data sources.

By default `rml:SQL2008Query` for databases,
`rml:CSV` for CSV and TSV data sources.
XPath for XML and JSONPath for JSON and JSONL data sources.

By default, the <a data-cite="RML-Core#dfn-iterator">iterator</a> is considered a row,
if not specified:
  - In the case of CSV or TSV data sources, the value of
  `rml:iterator` is considered a "row" and must not be specified.
  - In the case of XML and JSON data sources, it is a valid reference
  to an element or an object respectively considering the
  <a data-cite="RML-Core#dfn-reference-formulation">reference formulation</a> specified.
  - In the case of relational databases, the value of `rml:iterator` is either
  a SQL query (`rml:referenceFormulation rml:SQL2008Query`) or the SQL table
  name (`rml:referenceFormulation rml:SQL2008Table`). For SQL table names,
  they can be converted to a SQL query using the following SQL query template:
  `SELECT * FROM {table}` where `{table}` is the table name.

The Logical Source definition requires only the source (`rml:source`)
to be specified, all other properties are optional.
If a property is specified, it MUST only occur once.

| Property      | Domain                    | Range  |
| ------------- | ------------------------- | ------ |
| `rml:source`  | `rml:LogicalSource`  | `IRI`  |

<figure>
  <img src="/resources/images/source-structure.png" alt="Logical Source structure"/>
  <figcaption>The structure of [=Logical Source=]</figcaption>
</figure>

#### Reference formulations

Each [=Logical Source=] has a
<a data-cite="RML-Core#dfn-reference-formulation">reference formulation</a> to define how
to express a reference to elements of the data of the input
<a data-cite="RML-Core#dfn-data-source">data source</a>.
Several <a data-cite="RML-Core#dfn-reference-formulation">reference formulation</a>
(`rml:ReferenceFormulation`) are defined in this specification:

- `rml:CSV`: CSV or TSV data sources
- `rml:JSONPath`: JSON documents
- `rml:XPath`: XML documents with optionally
the definition of XML namespaces used in references.
By default, no namespaces are defined.
- `rml:SQL2008Query`: SQL query for a relational database.
- `rml:SQL2008Table`: Shortcut to select all columns from a SQL table.

`rml:XPath` may specify zero or more
`rml:namespace` properties with a `rml:Namespace`.
A `rml:Namespace` contains the following required properties:
 - `rml:namespacePrefix`: A Literal with the prefix used for the XML namespace.
 - `rml:namespaceURL`: A Literal with the URL identifying the XML namespace.

These reference formulations are defined in the [[RML-IO-Registry]].

<pre class="ex-source">
&lt;#XMLNamespace&gt; a rml:LogicalSource;
     rml:source [ a rml:Source, rml:FilePath;
         rml:path "/path/to/file/data.xml";
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
description for <a data-cite="RML-Core#dfn-data-source">data source</a> that are not
covered by existing vocabularies such as paginated Web APIs which implement pagination
in a Web API specific way.

### Source

A <dfn>Source</dfn> (`rml:Source`) defines how a
<a data-cite="RML-Core#dfn-data-source">data source</a> should be accessed.
It complements other source descriptions
such as SD Service, CSVW Table, DCAT Distribution, etc.
to support encoding, null values, compression, and other access properties.
The properties of a [=Source=] take precedence over the properties of other source
descriptions, for example: `rml:encoding` takes precedence over `csvw:encoding`
if both are specified.

A [=Source=] MUST have the following properties:

- zero or one **`rml:encoding`** property, which specifies the encoding
of the data inside the source. Defaults to `rml:UTF-8` if not specified.
- zero or more **`rml:null`** describes which data values inside the source
should be considered as NULL.<br>
The value for this predicate defaults to the default NULL token
of the underlying data model (e.g., NULL in relational databases
and null in JSON) and are always processed as such.
Some data models have no such default NULL token, such as CSV.
When that is the case, then nothing is considered NULL unless specified by
`rml:null`.<br>
Example: CSV does not have a default NULL character,
so no value is considered NULL.
However, JSON has a NULL character specified: `null`,
this one is used together with the ones specified through `rml:null`.
For a relational database, `rml:null "foo"` results into the following values
considered as NULL: `{NULL, "foo"}` where `NULL` comes from the relational
database model as NULL value.
- zero or one **`rml:compression`** specifies if the source is compressed
and the used compression algorithm. Defaults to no compression.

<pre class="ex-source">
&lt;#JSON&gt; a rml:LogicalSource;
     rml:source [ a rml:Source, rml:FilePath;
       rml:path "/path/to/data.json.gz";
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

Each [=Source=] MAY describe the values that should be considered as NULL
with `rml:null`, similar to `NULL` in relational databases.
By default, standardized NULL values are always considered,
but additional ones can be specified. Multiple NULL values are allowed.
For example, in relational databases `NULL` is always considered as a NULL
value while also an empty column can be considered as a NULL value by
specifying it through `rml:null` in a Source.

#### Compression formats

Each [=Source=] MAY specify the compression with `rml:compression`
to apply when exporting RDF triples to a [=Source=] for saving storage space.
Several compression formats are defined:

- `rml:none`: No compression is applied
- `rml:gzip`: GZip compression
- `rml:zip`: Zip archive with Zip compression
- `rml:tarxz`: Tar archive with Xz compression
- `rml:targz`: Tar archive with GZip compression

If unspecified, the default value is no compression.
This namespace is NOT limited to the listed compression formats
and MAY be extended in the future.

#### Encoding formats

Each [=Source=] MAY describe the encoding format to use when exporting
RDF triples to a Source. Several encoding formats are defined:

- `rml:UTF-8`: UTF-8 encoding
- `rml:UTF-16`: UTF-16 encoding

If unspecified, the default value is `rml:UTF-8`.
This namespace is NOT limited to the listed compression formats
and may be extended in the future.

### Examples {#source-examples}

The following example shows a Source of a CSV file.
RML-IO-Registry provides also support for CSVW which allows more fine-grained control
over CSV files such as delimeters, encoding, etc. but it is not required for
Processors to implement CSVW, only CSV is the minimum to be compliant with 
the RML IO module.

<pre class="ex-source">
&lt;#CSV&gt; a rml:LogicalSource;
     rml:source [ a rml:Source, rml:FilePath;
        rml:path "/path/to/data.csv";
        rml:null "NULL";
        rml:null "";
     ];
     rml:referenceFormulation rml:CSV;
.
</pre>

Note that there is no `rml:iterator` present because its default is row.
This particular CSV file has two different ways to specify a NULL value: `NULL`
or an empty value. Implementations need to check if a value is equal to one of
the values defined by `rml:null` to check for NULL values in the data.

The following example shows a [=Source=] specified for a MySQL database querying
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

Relative paths to files are covered by a source access description included
in this specification which subclasses `rml:Source` as `rml:FilePath`.
This access description allows accessing files relative from:

- `rml:CurrentWorkingDirectory`: relative to the current working directory of the RML processor.
- `rml:MappingDirectory`: relative to the location of the RML mapping.
- A string Literal: a string describing an absolute path against which relative paths are resolved, similar to the Base URI in [RFC3986](https://www.rfc-editor.org/rfc/rfc3986).

If `rml:root` is not specified, it defaults to `rml:CurrentWorkingDirectory`.

| Property    | Domain          | Range                                                              |
| ----------- | --------------- | ------------------------------------------------------------------ |
| `rml:root`  | `rml:FilePath`  | `rml:CurrentWorkingDirectory`, `rml:MappingDirectory` or `Literal` |
| `rml:path`  | `rml:FilePath`  | `Literal`                                                          |

Example of accessing a CSV file relative to the current working directory.
The file's absolute path is `$CURRENT_WORKING_DIR/file.csv` where `$CURRENT_WORKING_DIR` is
the location of the RML mapping.

<pre class="ex-source">
&lt;#RelativePathCWD&gt; a rml:LogicalSource;
  rml:source [ a rml:FilePath, rml:Source;
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
  rml:source [ a rml:FilePath, rml:Source;
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
  rml:source [ a rml:FilePath, rml:Source;
    rml:root "/root";
    rml:path "file.xml";
  ];
  rml:referenceFormulation rml:JSONPath;
  rml:iterator "$";
.
</pre>
