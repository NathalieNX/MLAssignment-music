"""
ADAPTED FROM : https://labrosa.ee.columbia.edu/millionsong/sites/default/files/tutorial1.py.txt

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

def get_key_value(dict, key):
    if key in dict :
        return dict[key]
    else :
        i = len(dict)+1
        dict[key]=i
        return i

def preprocess(filename, all_data, i):
    
    data, all_artist_names, all_artist_ids, all_artist_locations, all_titles, all_song_ids, all_years, all_durations, all_modes, all_tempos, all_artist_mbtags = all_data
    # TODO delete this
    #print("preprocess - filename type and value : ", type(filename), filename)
    #print("preprocess - i is : ", i)
    
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
    
    artist_name = GETTERS.get_artist_name(h5).decode("utf-8")
    value = get_key_value(all_artist_names, artist_name)
    data[i,j] = value
    j+=1
    
    artist_id = GETTERS.get_artist_id(h5).decode("utf-8")
    value = get_key_value(all_artist_ids, artist_id)
    data[i,j] = value
    j+=1
    
    artist_location = GETTERS.get_artist_location(h5).decode("utf-8")
    value = get_key_value(all_artist_locations, artist_location)
    data[i,j] = value
    j+=1
    
    title = GETTERS.get_title(h5).decode("utf-8")
    value = get_key_value(all_titles, title)
    data[i,j] = value
    j+=1
    
    song_id = GETTERS.get_song_id(h5).decode("utf-8")
    value = get_key_value(all_song_ids, song_id)
    data[i,j] = value
    j+=1

    year = GETTERS.get_year(h5)
    all_years.add(year)
    data[i,j] = year
    j+=1

    duration = GETTERS.get_duration(h5)
    all_durations.add(duration)
    data[i,j] = duration
    j+=1

    mode = GETTERS.get_mode(h5)
    all_modes.add(mode)
    data[i,j] = mode
    j+=1
    
    tempo = GETTERS.get_tempo(h5)
    all_tempos.add(tempo)
    data[i,j] = tempo
    j+=1
    
    artist_mbtags = GETTERS.get_artist_mbtags(h5)
    k=0
    for artist_mbtag in artist_mbtags :
        if k <= 4 :
            value = get_key_value(all_artist_mbtags, artist_mbtag.decode("utf-8"))
            data[i,j] = value
            j+=1
            k+=1
    
    """
     = GETTERS.get_(h5)
    all_s.add()
    data[i,j] = 
    j+=1
    
     = GETTERS.get_(h5)
    all_s.add()
    data[i,j] = 
    j+=1
    
     = GETTERS.get_(h5)
    all_s.add()
    data[i,j] = 
    j+=1
    """
    
    h5.close()


#Colonnes de flottants : 6, 7 ,8, 9,10
def normalize(M):
    newM=np.zeros(np.shape(M))
    example=M[0]
    #print(np.shape(M))
    for i, elem in enumerate(example):
        col = M[:,i]
        #nonNans=[x if not(np.isnan(x)) for x in col]
        nonNans=[]
        onlyNans=True
        for x in col:
            if not(np.isnan(x)):
                nonNans.append(x)
                onlyNans = False
        if onlyNans:
            nonNans == [0]
        nonNans=np.array(nonNans)
        mean=sum(nonNans)/len(nonNans)
        #.sum()
        col[np.isnan(col)]=mean
        if (i in [6,7,8]):
            col = col/np.max(col)
            #col[col==np.nan] = 0
        newM[:,i] = col
    #print(np.shape(newM))
    return newM
