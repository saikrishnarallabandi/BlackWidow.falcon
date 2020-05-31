import os, sys
from textblob import TextBlob


dump_file = sys.argv[1]
polarity_file = sys.argv[2]
pos_polarity_file = polarity_file + '.pos'
neg_polarity_file = polarity_file + '.neg'


def readNcleanNwrite(dump_file, polarity_file):
   f = open(dump_file)
   g = open(polarity_file, 'w')
   gpos = open(pos_polarity_file, 'w')
   gneg = open(neg_polarity_file, 'w')

   for line in f:
     line = ' '.join(k for k in line.split('\n')[0].split())
     if 'Media' in line:
         continue
     elif len(line) < 2:
         continue
     print(line)
     blob = TextBlob(line)
     polarity = blob.sentiment.polarity
     g.write(line + ' ' + str(polarity) + '\n')
     if polarity > 0.3:
       gpos.write(line + ' ' + str(polarity) + '\n')
     if polarity < -0.2:
       gneg.write(line + ' ' + str(polarity) + '\n')
   g.close()
   f.close()
   gpos.close()
   gneg.close() 

readNcleanNwrite(dump_file, polarity_file)
