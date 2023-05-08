# RML-IO

Repository for RML-IO specification, ontology, SHACL shapes and test cases.
Deployed to https://w3id.org/rml/io/spec/

## Quickstart

- edit dev.html
  - Makes sure all your local assets are in the `resources` folder, and the links in your dev.html file are relative (important because the publishing script creates multiple nested paths)
- run a HTTP server in this directory: `python3 -m http.server`
- open `dev.html` with a browser as http://localhost:8000/dev.html
- save as snapshot to function.html [using the respec functionality](https://respec.org/docs/#using-browser)
- run `node publish.js` to get the index.html + archived version in the `dist` folder

The `dist` folder contents should mimic the contents on `https://w3id.org/kg-construct/rml-target-source`

## License

RML-IO (c) by W3C Community Group on Knowledge Graph Construction

RML-IO is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this
work.  If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
