
from fileposition import FilePosition
from typing import List, Dict, Set, Optional 

class Occurrences : 
   occs : Dict[ str, Dict[ str, Set[ FilePosition ]]] 

   def __init__( self ) :
      self. occs = dict( ) 


   def add( self, word : str, filename : str, pos : FilePosition ) -> None :
      for isWord in self.occs.keys():                       # check does the word in my occs
         if isWord == word:                                 # if it is checks does the word previously occured in filename
            for file in self.occs[word].keys():             
               if file == filename:                         # if it occured adding position to set
                  self.occs[word][file].add(pos)
                  return                                    # breaks function there
            self.occs[word][filename] = {pos}               # if word exists but not occured previously in fname
            return                                          # creates fname pair set and adds pos and breaks function
      self.occs[word] = {filename:{pos}}                    # otherwise creates word in occs and gives as value its fname and position

 
   # Should return the number of distinct words:
 
   def distinctWords( self ) -> int :
      arr = [elem for elem in self.occs.keys()]             # creates list with distinct words
      return len(arr)                                       # returns it length

    
   # Should return the total number of words occurrences: 
 
   def totalOccurrences( self, word : Optional[str] = None, 
                               fname : Optional[str] = None ) -> int :
      totalOcc = 0                                          # track occurences
      if word == None:                                      # if word is not given enough to sum all words occurences
         for isWord in self.occs.keys():                    
            for file in self.occs[isWord].keys():
               totalOcc += len(self.occs[isWord][file])
      elif fname == None and word in self.occs:             # if fname is not given and word is exist in occs as key
         for file in self.occs[word].keys():                # sums all file occurences
            totalOcc += len(self.occs[word][file])
      else:                                                 # if word and fname is given
         for isWord in self.occs.keys():                    # check whether word is in occs
            if word == isWord:
               for file in self.occs[word]:                 # check file in occs value
                  if file == fname:
                     totalOcc = len(self.occs[isWord][file])
      return totalOcc                                       



   # This is for debugging, so it doesn't need to be pretty: 

   def __repr__( self ) -> str : 
      return str( self. occs )

 
   # Here the occurrences must be sorted and shown in a nice way: 

   def __str__( self ) -> str :
      myPrint = ""
      wordList = [word for word in self.occs.keys()]                                         # creates list of words
      for word in sorted(wordList):                                                          # go throught sorted word
         myPrint += "\"{}\" has {} occurence(s):\n".format(word, self.totalOccurrences(word))   
         fileList = [file for file in self.occs[word].keys()]                                # creates list of files
         for file in sorted(fileList):                                                       # go through sorted files
            myPrint += "\tin file {}\n".format(file)
            positionList = [position for position in self.occs[word][file]]                  # creates list of positions
            for loc in sorted(positionList):                                                 # go through sorted positions
               myPrint += "\t\tat line {}, column {}\n".format(loc.line, loc.column)
      return myPrint
 
