report.pdf:	report.tex one.png
	pdflatex	$<

#Statistics
one.png:	bank.csv new_autorank.py
	python3 new_autorank.py

#Dataset
bank.csv:
	kaggle datasets download janiobachmann/bank-marketing-dataset
	unzip bank-marketing-dataset.zip
	rm bank-marketing-dataset.zip	

.PHONY:	clean	almost_clean	

clean:	almost_clean
	rm	report.pdf
	rm	one.png 
	
almost_clean:
	pdflatex	-c

