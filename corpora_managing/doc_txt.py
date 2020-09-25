#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:49:46 2020

@author: pmchozas
"""

import os
import uuid
import textract


source_directory=("german")


training_directory = os.path.join(os.getcwd(), "training_data")


for process_file in  os.listdir(source_directory):
    file, extension = os.path.splitext(process_file)
    
    # We create a new text file name by concatenating the .txt extension to file UUID
    dest_file_path = file + '.txt'
    
    #extract text from the file
    content = textract.process(os.path.join(source_directory, process_file))
    
    # We create and open the new and we prepare to write the Binary Data which is represented by the wb - Write Binary
    write_text_file = open(os.path.join(training_directory, dest_file_path), "wb")
    
    #write the content and close the newly created file
    write_text_file.write(content)
    write_text_file.close()