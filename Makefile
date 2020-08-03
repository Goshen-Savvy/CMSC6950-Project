report.pdf:	report/report.tex mean.png stat_auto_rank.png
	pdflatex	$<

#Statistics
stat_auto_rank.png:	bank.csv new_autorank.py
	python3 new_autorank.py

mean.png:	bank.csv plot.py
	python3 plot.py

#Dataset
bank.csv:
	kaggle datasets download janiobachmann/bank-marketing-dataset
	unzip bank-marketing-dataset.zip
	rm bank-marketing-dataset.zip	

.PHONY:	clean	almost_clean	

clean:	almost_clean
	rm	report.pdf
	rm	mean.png
	rm	stat_auto_rank.png 
	
almost_clean:
	pdflatex	-c

