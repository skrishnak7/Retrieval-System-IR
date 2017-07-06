# Retrieval-System-IR
Implementation of a simple statistical relevance model based on the vector relevance model, using the term-based index.

The system retrieves and ranks the documents that satisfy the queries.

The relevance model 
(1) reads a query
(2) parses by determining the tokens 
(3) discards stop-words
(4) generates the lemmas for the content words (which become the terms of the query)
(5) computes the weights of the query vector.

The vector representations of queries and documents are used to determine scores that
inform the ranking of documents against the queries. The scores are obtained by
computing the cosine similarity for every query-document vector pair.

The weighting functions fro vector representations are provided by W1 and W2:
 
 W1 = (0.4 + 0.6 * log (tf + 0.5) / log (maxtf + 1.0))
 * (log (collectionsize / df)/ log (collectionsize))
 
 W2 = (0.4 + 0.6 * (tf / (tf + 0.5 + 1.5 *
 (doclen / avgdoclen))) * log (collectionsize / df)/
 log (collectionsize))
 
 tf: the frequency of the term in the document
 maxtf: the frequency of the most frequent indexed term in the document
 df: the number of documents containing the term
 doclen: the length of the document, in words, discounting stop-words
 avgdoclen: the average document length in thecollection, considering the doclen of each document
 
 W1 is a variation of older, but well-known, 'max tf' term weighting. 
 W2 is a variation on Okapi term weighting. 
 Both TW1 and TW2 use a fairly standard idf, namely: idf = log (collectionsize/df) 

HW3_IR.py is the file to execute to get results on cranfield collection
