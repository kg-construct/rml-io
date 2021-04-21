# Data IO in RML Specification

Repository for https://rml.io/specs/target-in-rml

## Quickstart

- Edit dev.html
- Make sure all your local assets are in the `resources` folder, 
  and the links in your `dev.html` file are relative 
  (important because the publishing script creates multiple nested paths)
- Run a HTTP server in this directory: `python3 -m http.server`
- Open `dev.html` with a browser as http://localhost:8000/dev.html
- Save as snapshot to `rendered.html` [using the respec functionality](https://respec.org/docs/#using-browser)
- Run `node publish.js` to get the `index.html` + archived version in the `dist` folder

The `dist` folder contents should mimic the contents on `https://rml.io/specs/target-in-rml`
