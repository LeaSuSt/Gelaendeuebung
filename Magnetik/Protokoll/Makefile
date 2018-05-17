.PHONY: clean pdf clean-aux

vierpole.pdf: Vierpole.tex lit.bib $(shell find chap -type f) $(shell find fig -type f) $(shell find tab -type f) $(shell find include -type f)
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex

deckblatt.pdf: deckblatt.tex lit.bib $(shell find chap -type f) $(shell find fig -type f) $(shell find tab -type f) $(shell find include -type f)
	pdflatex deckblatt.tex
	pdflatex deckblatt.tex

# needed for integration in vim-latex
pdf: vierpole.pdf

clean:
	rm *.aux *.log *.out *.bbl *.blg *.toc *.lof *.lot *.pdf

clean-aux:
	rm *.aux *.log *.out *.bbl *.blg *.toc *.lof *.lot
