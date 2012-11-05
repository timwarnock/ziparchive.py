#!/usr/local/bin/python
''' Usage: ziparchive.py [files] [zipfile]

	create/overwrite compressed archive file
'''
import zlib, zipfile, sys, os


def ziparchive(filepath, zfile=None):
	''' create/overwrite a zip archive

		can be a file or directory, and always overwrites the output zipfile if one already exists

		An optional second argument can be provided to specify a zipfile name, 
		by default the basename will be used with a .zip extension

		>>>
		>>> ziparchive('foo/data/')
		>>> zf = zipfile.ZipFile('data.zip', 'r')
		>>> 

		>>> 
		>>> ziparchive('foo/data/', 'foo/eggs.zip')
		>>> zf = zipfile.ZipFile('foo/eggs.zip', 'r')
		>>> 
	'''
	if zfile is None:
		zfile = os.path.basename(filepath.strip('/')) + '.zip'
	filepath = filepath.rstrip('/')
	zf = zipfile.ZipFile(zfile, mode='w')
	if os.path.isfile(filepath):
		zf.write(filepath, filepath[len(os.path.dirname(filepath)):].strip('/'), compress_type=zipfile.ZIP_DEFLATED)
	else:
		for root, dirs, files in os.walk(filepath):
			for name in files:
				file_to_zip = os.path.join(root, name)
				arcname = file_to_zip[len(os.path.dirname(filepath)):].strip('/')
				zf.write(file_to_zip, arcname, compress_type=zipfile.ZIP_DEFLATED)

if __name__ == '__main__':
	ziparchive(*sys.argv[1:])

