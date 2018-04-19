# -*- coding: utf-8 -*-

import sqlite3

def create_connect_database(database_name):
	conn = sqlite3.connect(database_name)
	print "Opened database successfully"


