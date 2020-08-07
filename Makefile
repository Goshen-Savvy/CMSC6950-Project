report.pdf:	report/report.tex mean.png stat_auto_rank.png missing_data.png marital_balance.png duration.png
	pdflatex	$<

#Statistics
stat_auto_rank.png:	bank.csv new_autorank.py
	python3 new_autorank.py

#mean distribution
mean.png:	bank.csv plot.py
	python3 plot.py

#missing data
missing_data.png:	bank.csv ml.py
	python3 ml.py

#missing data
marital_balance.png:	bank.csv my_plot.py
	python3 my_plot.py

#distribution of calls
duration.png:	duration.py	
	python3 duration.py	

#Dataset
bank.csv:
	kaggle datasets download janiobachmann/bank-marketing-dataset
	unzip bank-marketing-dataset.zip
	rm bank-marketing-dataset.zip	

.PHONY:	clean	almost_clean	

clean:	almost_clean
	rm *.pdf
	rm *.png
	rm *.csv
	rm *.out
	rm *.aux
	rm *.log
	
almost_clean:
	#pdflatex -c

