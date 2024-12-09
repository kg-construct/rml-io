#!/usr/bin/env python3

import os
import sys
import glob
import csv

def get_title_description(testcase: str):
    with open ('descriptions.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == testcase:
                return row[1], row[2]

def main(spec: str):
    with open ('metadata.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'title', 'description', 'specification',
                         'mapping', 'input_format1', 'input_format2',
                         'input_format3', 'output_format1', 'output_format2',
                         'output_format3', 'input1', 'input2', 'input3',
                         'output1', 'output2', 'output3', 'error'])
        for testcase in glob.glob('RML*'):
            title, description = get_title_description(testcase)
            error = 'false'
            input1 = ''
            input2 = ''
            input3 = ''
            input_format1 = ''
            input_format2 = ''
            input_format3 = ''
            output1 = ''
            output2 = ''
            output3 = ''
            output_format1 = ''
            output_format2 = ''
            output_format3 = ''

            # Input file
            if os.path.exists(os.path.join(testcase, 'Friends.json')):
                input1 = 'Friends.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'Friends-UTF16.json')):
                input1 = 'Friends-UTF16.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'Friends.json.gz')):
                input1 = 'Friends.json.gz'
                input_format1 = 'application/gzip+json'
            elif os.path.exists(os.path.join(testcase, 'Friends.json.zip')):
                input1 = 'Friends.json.zip'
                input_format1 = 'application/gzip+json'
            elif os.path.exists(os.path.join(testcase, 'Friends.json.tar.xz')):
                input1 = 'Friends.json.tar.xz'
                input_format1 = 'application/tarxz+json'
            elif os.path.exists(os.path.join(testcase, 'Friends.json.tar.gz')):
                input1 = 'Friends.json.tar.gz'
                input_format1 = 'application/targz+json'
            elif os.path.exists(os.path.join(testcase, 'Friends-NULL.csv')):
                input1 = 'Friends-NULL.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'Friends-NULL2.csv')):
                input1 = 'Friends-NULL2.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'Friends.nt')):
                input1 = 'Friends.nt'
                input_format1 = 'application/n-triples'
            elif os.path.exists(os.path.join(testcase, 'Friends.csv')):
                input1 = 'Friends.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'Friends.json')):
                input1 = 'Friends.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'Friends.xml')):
                input1 = 'Friends.xml'
                input_format1 = 'text/xml'
            else:
                input1 = f'http://w3id.org/rml/resources/rml-io/{testcase}/Friends.json'
                input_format1 = 'application/json'

            # Mapping file
            if os.path.exists(os.path.join(testcase, 'mapping.ttl')):
               mapping_file = 'mapping.ttl'
            else:
                raise ValueError('Mapping file missing!')

            # Output files
            if os.path.exists(os.path.join(testcase, 'default.nq')):
                output1 = 'default.nq'
                output_format1 = 'application/n-quads'
            else:
                raise NotImplementedError('output1 is not known, but required')

            if os.path.exists(os.path.join(testcase, 'dump1.nq')):
                output2 = 'dump1.nq'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.nt')):
                output2 = 'dump1.nt'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.n3')):
                output2 = 'dump1.n3'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.jsonld')):
                output2 = 'dump1.jsonld'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.rdfjson')):
                output2 = 'dump1.rdfjson'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.rdfxml')):
                output2 = 'dump1.rdfxml'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.ttl')):
                output2 = 'dump1.ttl'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.nq.gz')):
                output2 = 'dump1.nq.gz'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.nq.zip')):
                output2 = 'dump1.nq.zip'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.nq.tar.xz')):
                output2 = 'dump1.nq.tar.xz'
                output_format2 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'dump1.nq.tar.gz')):
                output2 = 'dump1.nq.tar.gz'
                output_format2 = 'application/n-quads'

            if os.path.exists(os.path.join(testcase, 'dump2.nq')):
                output3 = 'dump2.nq'
                output_format3 = 'application/n-quads'

            writer.writerow([testcase, title, description, spec, mapping_file,
                             input_format1, input_format2, input_format3,
                             output_format1, output_format2, output_format3,
                             input1, input2, input3, output1, output2,
                             output3, error])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./make-metadata.py <IRI OF SPEC>')
        sys.exit(1)
    main(sys.argv[1])
