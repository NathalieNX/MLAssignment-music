"""
INSPIRED BY : https://labrosa.ee.columbia.edu/millionsong/sites/default/files/tutorial1.py.txt

Tutorial for the Million Song Dataset

by Thierry Bertin-Mahieux (2011) Columbia University
   tb2332@columbia.edu
   Copyright 2011 T. Bertin-Mahieux, All Rights Reserved

This tutorial will walk you through a quick experiment
using the Million Song Dataset (MSD). We will actually be working
on the 10K songs subset for speed issues, but the code should
transpose seamlessly.

In this tutorial, we do simple metadata analysis. We look at
which artist has the most songs by iterating over the whole
dataset and using an SQLite database.

You need to have the MSD code downloaded from GITHUB.
See the MSD website for details:
http://labrosa.ee.columbia.edu/millionsong/

If you have any questions regarding the dataset or this tutorial,
please first take a look at the website. Send us an email
if you haven't found the answer.

Note: this tutorial is developed using Python 2.6
on an Ubuntu machine. PDF created using 'pyreport'.
"""

import numpy as np

# imports specific to the MSD
import hdf5_getters as GETTERS

def preprocess(filename, all_data, i):
    
    data, all_artist_names = all_data
    # TODO delete this
    #print("preprocess - filename type and value : ", type(filename), filename)
    
    # data = [[]]
    j=0
    
    '''
    def func_to_get_artist_name(filename):
        """
        This function does 3 simple things:
        - open the song file
        - get artist ID and put it
        - close the file
        """
        h5 = GETTERS.open_h5_file_read(filename)
        artist_name = GETTERS.get_artist_name(h5)
        all_artist_names.add( artist_name )
        h5.close()
    '''
    h5 = GETTERS.open_h5_file_read(filename)
    artist_name = GETTERS.get_artist_name(h5)
    all_artist_names.add(artist_name)
    j+=1
    h5.close()


