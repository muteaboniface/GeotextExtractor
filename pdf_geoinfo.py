#!/usr/bin/env python
# coding: utf-8

# ## Extracting Countries, Cities and Regions from pdf
# ###### Text to use is derived from a pdf document.

# In[1]:


import nltk
import spacy
  
# Downloading Essential entity models

nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[2]:


import locationtagger
from PyPDF2 import PdfFileReader
from pdfminer import high_level


# #### Working with Pdf Text

# In[3]:

#Provide_Path_to_the_pdf_document_you_would_like_to_analyse
pdf_path=r"C:\.........\Secret Letters.pdf"
with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        
        print("Author" +': ' + information.author)
        print("Creator" +': ' + information.creator)
        print("Producer" +': ' + information.producer)
        print(f"Number of pages: {number_of_pages}")


# In[4]:


# creating a pdf file object
pdfFileObject = open(pdf_path, 'rb')
# creating a pdf reader object
pdfReader = PdfFileReader(pdfFileObject)


# Reading the text page by page
def readpages(start,end):
    """Extract text from pdf from start page number to end page number and returns the text"""
    text=''
    for i in range(start,end):
        # creating a page object
        pageObj = pdfReader.getPage(i)
        # extracting text from page
        text += pageObj.extractText()
        
        
    if text == '':
        pages = [start,end]
        text = high_level.extract_text(pdf_path, "", pages)
        
    return text


# In[5]:



def geo_loc_limited():
    """
    Gives limited info
    """

    # getting all countries
    print("The countries in text : ")
    print(place_entity.countries)

    # getting all states
    print("\n\nThe states in text : ")
    print(place_entity.regions)

    # getting all cities
    print("\n\nThe cities in text : ")
    print(place_entity.cities)


# #### Extracting Relations of Locations

# In[6]:


def geo_loc_detailed():
    """
    Gives detailed relationship info
    """
    
    print('\n\n Detailed relationship info \n')
    # getting all country regions
    print("The countries regions in text : ")
    print(place_entity.country_regions)

    # getting all country cities
    print("\n\nThe countries cities in text : ")
    print(place_entity.country_cities)

    # getting all other countries
    print("\n\nAll other countries in text : ")
    print(place_entity.other_countries)

    # getting all region cities
    print("\n\nThe region cities in text : ")
    print(place_entity.region_cities)

    # getting all other regions
    print("\n\nAll other regions in text : ")
    print(place_entity.other_regions)

    # getting all other entities
    print("\n\nAll other entities in text : ")
    print(place_entity.other)


# In[7]:


run = True
while run:
    start = int(input('Enter the start page number to read from: '))
    end = int(input('Enter the last page number to read from: '))
    
    sample_text = readpages(start,end)
    #Printing sample textto verify accuracy of pages youre working with
    print(sample_text[:13])
    print(sample_text[-15:])
    
    # extracting entities.
    place_entity = locationtagger.find_locations(text = sample_text)
    
    
    # Displaying the info
    geo_loc_limited()

    geo_loc_detailed()
    
    
    process = int(input('What would you like to do?\n 1. Terminate the process \n 2. Continue\n    >>>> '))
    
    if process == 1:
        run = False

