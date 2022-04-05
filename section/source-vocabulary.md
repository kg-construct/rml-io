## Source vocabulary {#source-vocabulary}

The Source vocabulary namespace is http://semweb.mmlab.be/ns/rml-source# 
and it's prefix is `rmls`.

The Source vocabulary consists of a single class: `rmls:Source` 
to describe how a source can be accessed.

### Defining Sources {#defining-sources}

A Source is any data source providing data to be mapped to RDF triples.

A Source (`rmls:LogicalSource`) contains the following properties:

- The **source** (`rml:source`) locates the data source.
It is a URI [[RFC3986]] 
or Literal [[RDF-Concepts]]
that represents the input data source's location. 
External vocabulary such as DCAT, VoID, SD is allowed here. 
- The **logical iterator** (`rml:iterator`)
defines the iteration loop used to map the data of the input source. 
- The **reference formulation** (`rml:referenceFormulation`)
defines the reference formulation used to refer to the elements
of a data source.
The reference formulation must be specified in the case of databases,
CSV, TSV, XML, and JSON data sources.
By default `rr:SQL2008` for databases, `ql:CSV` for CSV and TSV data sources.
XPath for XML and JSONPath for JSON and JSONL data sources.
- The **iterator** (`rml:iterator`) defines how to refer to any of the following:
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

The Source definition requires only the source (`rmls:source`) to be specified, 
all other properties are optional.

| Property                    | Domain               | Range                     |
| --------------------        | -------------------- | ------------------        |
| `rmls:source`               | `rmls:LogicalSource` | `URI or Literal`          |
| `rmls:referenceFormulation` | `rmls:LogicalSource` | `ql:ReferenceFormulation` |
| `rmls:iterator`             | `rmls:LogicalSource` | `Literal`                 |

<figure>
  <img src="./resources/images/structure.png" alt="Source structure"/>
  <figcaption>The structure of Source</figcaption>
</figure>

### Examples {#examples}

The following example show a Source of an CSV file.

<pre class="ex-target">
&lt;#CSV&gt; a rmls:LogicalSource;
     rmls:source [ a csvw:Table;
         csvw:url "/path/to/data.csv";
     ];
     rml:referenceFormulation ql:CSV;
.
</pre>

Note that there is not `rml:iterator` is present because its default is row.

The following example shows a Source specified for a database.

<pre class="ex-target">
&lt;#RDB&gt; a rmls:LogicalSource;
     rmls:source [ a d2rq:Database;
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

<pre class="ex-target">
&lt;#XML&gt; a rmls:LogicalSource;
     rmls:source [ a dcat:Dataset;
       dcat:distribution [ a dcat:Distribution;
         dcat:accessURL &lt;file:///path/to/data.xml&gt;;
       ];
     ];
     rml:referenceFormulation ql:XPath;
     rml:iterator "/xpath/iterator/expression";
.
</pre>

<pre class="ex-target">
&lt;#JSON&gt; a rmls:LogicalSource;
     rmls:source [ a dcat:Dataset;
       dcat:distribution [ a dcat:Distribution;
         dcat:accessURL &lt;file:///path/to/data.json&gt;;
       ];
     ];
     rml:referenceFormulation ql:JSONPath;
     rml:iterator "$.jsonpath.expression";
.
</pre>
