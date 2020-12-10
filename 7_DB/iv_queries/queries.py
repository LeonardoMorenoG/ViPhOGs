"""
queries
Created on Jan 26 / 2016
Communicate with mySQL viruses database, make queries and create charts
@author: lemoga
"""

# CREATES A CONNECTION TO AN EXISTING DATABASE
from BioSQL import BioSeqDatabase
import sys
"""
usr = sys.argv[1]
xxx = sys.argv[2]
hst = sys.argv[3]
db  = sys.argv[4]
"""

usr = "root"
xxx = "jl201130674mg"
hst = "localhost"
adb = "viruses"

server = BioSeqDatabase.open_database(driver="MySQLdb", user=usr, passwd=xxx, host=hst, db=adb)

#LOAD DATA
from Bio import SeqIO
db = server.new_database("test")
count = db.load(SeqIO.parse(sys.argv[1], "genbank"))
print "Loaded %i records" %count
server.adaptor.commit()

