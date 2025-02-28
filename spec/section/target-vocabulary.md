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
An external vocabulary such as DCAT, SD, etc. is allowed here.
If a target cannot be accessed with existing vocabulary, a custom vocabulary
can be used, for example: handling an authentication flow may be specific
for that specific target. A custom ontology can be used here to describe
this authentication flow such as [W3C Web of Things Security](https://www.w3.org/2019/wot/security).

A Target (`rml:Target`) MAY contain the following properties:

- The **serialization format** (`rml:serialization`) MAY specify
the serialization format for exporting a knowledge graph.
The serialization format is described using the W3C
[formats](http://www.w3.org/ns/formats/) namespace.
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
| `rml:mode`           | `rml:Target`         | `rml:Mode`        |
| `rml:compression`    | `rml:Target`         | `rml:Compression` |
| `rml:encoding`       | `rml:Target`         | `rml:Encoding`    |

<figure>
  <img src="/resources/images/target-structure.png" alt="Logical Target structure"/>
  <figcaption>The structure of Logical Target</figcaption>
</figure>

Logical Targets are the same if they are effectively equal as described in [RML-Core](https://kg-construct.github.io/rml-core/spec/docs/#dfn-effectively-equal).

#### Serialization formats

Each Target MAY describe the serialization format
with `rml:serialization` to use when exporting RDF triples to a Target.
The possible formats are defined in the W3C
[formats](http://www.w3.org/ns/formats/) namespace
such as N-Quads, N-Triples, JSON-LD, Turtle, etc.
If unspecified, the default format is N-Quads [[N-Quads]].

#### Mode

Each Target MAY describe the operation mode when accessing a Target
with `rml:mode` to specify if the Target must be appended, overwritten, etc.
If not specified, defaults to `rml:Write`.
This property accepts the range of `rml:Mode`:

- `rml:Read`: read-only mode (`r`). Start beginning of file. Not useful for targets. File must exist.
- `rml:ReadWrite`: read-write mode (`r+`). Start beginning of file, no truncation.  Only write part is useful for targets. File must exist.
- `rml:Write`: write mode (`w`).  Truncate/create file and start at the beginning to add new data.
- `rml:WriteRead`: write-read mode (`w`).  Truncate/create file and start at the beginning to add new data. Only write part is useful for targets
- `rml:Append`: append-only mode. Existing file is kept and new data is appended at the end. File is created if not exist.
- `rml:AppendRead`: append-read mode. Existing file is kept and new data is appended at the end. File is created if not exist.

#### Compression formats

Each Target MAY specify the compression with `rml:compression`
to apply when exporting RDF triples to a Target for saving storage space.
Several compression formats are specified by the `comp` namespace:

- `rml:none`: No compression is applied
- `rml:gzip`: GZip compression
- `rml:zip`: Zip archive with Zip compression
- `rml:tarxz`: Tar archive with Xz compression
- `rml:targz`: Tar archive with GZip compression

If unspecified, the default value is no compression.
This namespace is NOT limited to the listed compression formats
and MAY be extended in the future.

#### Encoding formats

Each Target MAY describe the encoding format to use when exporting
RDF triples to a Target. Several encoding formats are defined:

- `rml:UTF-8`: UTF-8 encoding
- `rml:UTF-16`: UTF-16 encoding

If unspecified, the default value is UTF-8.
This namespace is NOT limited to the listed compression formats
and MAY be extended in the future.

#### Relative paths

Relative paths to files are covered by a target access description included
in this specification which subclasses `rml:Target` as `rml:FilePath` re-used from the Logical Source.

### Examples {#target-examples}

The following example show a Target of an RDF dump in Turtle [[Turtle]]
format with GZip compression and UTF-8 encoding:

<pre class="ex-target">
&lt;#FileDump&gt; a rml:LogicalTarget;
    rml:target [ a rml:Target, rml:FilePath;
        rml:path "/data/dump.ttl";
        rml:compression rml:gzip;
        rml:encoding rml:UTF-8;
    ];
    rml:serialization formats:Turtle;
.
</pre>
