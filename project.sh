### script to call one at a time the python files and terminal commands for fasttext

DATADIR=/home/tea/Desktop/teaUpdate/Tea


##this will create the text file needed for fasttext
python3 ${DATADIR}/Create_Input.py --input $1  --output ${DATADIR}/reviews_fasttext.txt


##this will call fasttext to create the model given the text file of reviews
./fasttext skipgram -input ${DATADIR}/reviews_fasttext.txt  -output ${DATADIR}/model -dim $2

##this will print the resulting vector for each review in the file 
./fasttext print-sentence-vectors ${DATADIR}/model.bin < ${DATADIR}/reviews_fasttext.txt > ${DATADIR}/out.txt

##now we will extract only the vector for each review (aka json object) and save in a ##final result txt file
python3 ${DATADIR}/Create_Results.py --input ${DATADIR}/out.txt --output ${DATADIR}/vector_results.txt --dim $2
 
