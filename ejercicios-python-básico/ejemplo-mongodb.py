#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from pymongo import MongoClient
try:
    conector = MongoClient("192.168.231.132",27017)
    db = conector.deathstar
    troopers = db.troopers
    #print(db.collection_names())
    print(troopers.find_one({"edad":36}))
    """
    troopers.insert_one({
    "nombre":"Victor Doe",
    "edad":36
    })
    """
except Exception as e:
    sys.exit(e)
