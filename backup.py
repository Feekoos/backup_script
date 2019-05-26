#!/usr/bin/env python
# FileName: backup.py
# Author: Filip Petrinjak
# Date: 18.11.'12.
# Version: 1.0
 
import os, time
 
def main():
	
	conf_file = '/home/fikus/bin/.backup.conf'
	target_dir = '/usr/home/fikus/backups/'

	# The files and directories to be backed up
	source = [line.strip() for line in open(conf_file)]
	print source
       
	# Backup directory
	target = target_dir + time.strftime('%Y_%m_%d') + '.tar.gz'

	# Using the Linux Tar command and gzip to place files in archive
	backup = 'tar -cvzf %s %s' % (target, ' '.join(source))

	# Run Backup
	if os.system(backup) == 0:
		print '\n'
		print 'Successful backup to ', target
		print '*' * 35
	else:
		print 'ERROR: Backup Failed!'
	return 0

if __name__ == '__main__': main()
