
from fileposition import FilePosition
from typing import Tuple, Generator, TextIO 

import os
import syntax
import copy
import codecs


class FileWalker : 
   topdir : str  # Python uses strings for representing file names. 
  
   def __init__( self, topdir ) :
      self. topdir = topdir # No checks here. 


   def recDirIterator( self ) -> Generator[ Tuple[ str, str, FilePosition ], None, None ] : 
      if os.path.exists(self.topdir) == False:                             # path does not found
         raise FileExistsError("Not found!")
      else:
          for myDir, subdir, myFiles in os.walk(self.topdir):
            for myFile in myFiles:
               name = os.path.join(myDir, myFile)
               for myWord, myPos in self.fileIterator(open(name, "r", encoding="utf8")):
                  yield name, myWord, myPos   

   @staticmethod 
   def fileIterator( f : TextIO ) -> Generator[ Tuple[ str, FilePosition ], None, None ] :
      myFile, myWord, myPos = f.readlines(), "", FilePosition()                     # initilize 3 variables
      j = 1                                                                         # also use j as tracking column
      for words in myFile:                                                          # read lines as string
         for ch in words:                                                           # read char from string
            if syntax.inWord(ch) == False and myWord != "":                         # if meets not letter and word exits
               yield myWord, copy.copy(myPos)
               myPos.advance(j)
               myWord, j = "", 1                                                    # re initialize myWord
            elif syntax.inWord(ch) == True:                                         # if letter valid add to word
               myWord += ch.lower()
               j += 1
            else:
               myPos.column += 1
         myPos.column = 1
         myPos.line += 1
      if myWord != "":                                                              # at the end if word has content
         yield myWord, myPos                                                        # yield it



   def __repr__( self ) -> str : 
      return "FileWalker: " + self. topdir 

   def __str__( self ) -> str :
      return "FileWalker: " + self. topdir
