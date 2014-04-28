#!/usr/bin/env python
# script used to define word through command line, by querying
# dictionary.com
# @author <bprinty@gmail.com>
# -----------------------------------------------------------------

# imports
# -------
import urllib2
import re
from optparse import OptionParser

# methods
# -------
def urlread( word ):
    """
    opens url and returns source 
    @param word - word to search dictonary.com for
    @param html - html source
    """
    search_url='http://dictionary.reference.com/browse/'
    html = urllib2.urlopen( search_url + word + '?' ).read()
    return html

def correct_misspel( html ):
    """
    checks html to see if word is misspelled,
    and returns the first suggestion
    @param html - html source
    @param html - html source for properly spelled word
    """
    m = re.search( r"<span class=\"bmat\">.*?<a.*?>(.+?)</a>", html )
    if m:
        return get_definition( urlread( m.group(1) ), m.group(1) )
    else:
        return 'error: no definition found'

def get_definition( html, word ):
    """
    retrieves definition for word in html
    @param html - html source
    @return definition - formatted definition
    """
    definition = False
    for l in html.split('\n'):
        if 'google_ad_section_start' in l:
            m = re.search( r"data-syllable=\".+?\">.*?<span class=\"pg\">(.+?)</span>.*?<div class=\"luna-Ent\">(.+?)<span class=\"ital-inline\">(.+?)</span>.*?Synonyms: </span>(.+?)</span>", l )
            if m:
                definition = '\n' + word + ': ' + m.group(1) + '\n\n'
                definition = definition + 'def:\n' + m.group(2) + '\n\n'
                definition = definition + 'examples:\n' + m.group(3) + '\n\n'
                definition = definition + 'synonyms:\n' + m.group(4) + '\n\n' 
    return definition


# execution
# ---------

# grabbing arguments
usage = 'usage: define.py -h <word>'
parser = OptionParser( usage=usage )
params, inputs = parser.parse_args()

# pulling initial url
search_url='http://dictionary.reference.com/browse/'

# searching url
if( len(inputs) == 1 ):
    html = urlread( inputs[0] )
    definition = get_definition( html, inputs[0] )
    if definition == False:
        definition = correct_misspel( html )
    print definition







