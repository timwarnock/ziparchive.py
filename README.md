ziparchive.py
=============

create/overwrite a zip archive

Can be a file or directory, and always overwrites the output zipfile if one already exists

An optional second argument can be provided to specify a zipfile name, 
by default the basename will be used with a .zip extension

Examples:

ziparchive.py files_to_zip/

ziparchive.py files_to_zip/ output.zip
