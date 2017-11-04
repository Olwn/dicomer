#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import argparse
import dicom

info_deleted = ['PatientName', 'PatientBirthDate']


def de_sensitive(path, write_to):
    dc = dicom.read_file(path, force=True)
    for tag in info_deleted:
        if tag in dc:
            del dc[dc.data_element(tag).tag]
    dicom.write_file(write_to, dc)


def process_case(root, patient):
    new_dir = os.path.join(root, patient + '_cleared')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    for dcm in os.listdir(os.path.join(root, patient)):
        if not dcm.endswith('.dcm'):
            continue
        de_sensitive(os.path.join(root, patient, dcm), os.path.join(root, new_dir, dcm))
    print "Finished processing %s" % patient


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()
    if not args.directory:
        sys.exit("Please specify a root directory containing at least one patient.")
    directory = args.directory
    c = 0
    for name in os.listdir(directory):
        d = os.path.join(directory, name)
        if os.path.isfile(d):
            continue
        if len([f for f in os.listdir(d) if f.endswith('.dcm')]) == 0:
            continue
        process_case(directory, name)
        c += 1
    print "%d cases are found." % c
