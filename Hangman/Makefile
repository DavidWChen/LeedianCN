.SILENT:

subfiles = README Makefile hangworm.py hangworm two-letter_word_eng.txt

default:
	chmod +x hangworm.py
	chmod +x hangworm
	python -m py_compile hangworm.py
	chmod +x hangworm.pyc
clean:
	rm -rf hangworm.pyc
dist:
	tar -zcvf games.tar.gz $(subfiles)
