'''
Created on Dec, 2016

@author: hugo

'''
from __future__ import absolute_import
import argparse
import numpy as np

from autoencoder.testing.classifier import classifier
from autoencoder.utils.io_utils import load_json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('doc_codes', type=str, help='path to the doc codes file')
    parser.add_argument('doc_labels', type=str, help='path to the doc labels file')
    parser.add_argument('-ns', '--n_splits', type=int, default=10, help='num of folds')
    parser.add_argument('-ne', '--n_epoch', type=int, default=100, help='num of epoches (default 100)')
    parser.add_argument('-bs', '--batch_size', type=int, default=100, help='batch size (default 100)')
    args = parser.parse_args()

    doc_codes = load_json(args.doc_codes)
    doc_labels = load_json(args.doc_labels)
    X = np.r_[doc_codes.values()]
    Y = [doc_labels[i] for i in doc_codes.keys()]
    results = classifier(X, Y, n_splits=args.n_splits, nb_epoch=args.n_epoch, batch_size=args.batch_size)
    import pdb;pdb.set_trace()

if __name__ == '__main__':
    main()