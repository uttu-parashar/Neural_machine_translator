#                                                               ** Neural_machine_translator **

## Objective of project :--  Building a machine_translator, Which can translate an English Sentence to Hindi.

### <font color='green'>Introduction of the dataset, We will use :</font>
We will use a Coupus published by IIT-Bombay. This corpus contains 1.6 Million santence pairs(Eng-Hindi) of both languages.The IIT Bombay English-Hindi corpus contains parallel corpus for English-Hindi as well as monolingual Hindi corpus collected from a variety of existing sources and corpora developed at the Center for Indian Language Technology, IIT Bombay over the years. This corpus has been used at the Workshop on Asian Language Translation Shared Task since 2016 the Hindi-to-English and English-to-Hindi languages pairs and as a pivot language pair for the Hindi-to-Japanese and Japanese-to-Hindi language pairs. To find more About the corpus ,Please go through the link given bellow : 
           
      https://www.cfilt.iitb.ac.in/~parallelcorp/iitb_en_hi_parallel/

After Unziping the initial Corpus i get two folders :
    
    1 - IITB.en-hi.en.txt (contains 1.6 million English Sentences.)
    2 - IITB.en-hi.hi.txt (contains Hindi translation of each corresponding English Sentence.)

    
### Here We will Implement a Custon Endocer_Dedocder(Seq-2-Seq) Model to archive our goal.

#### Architecture of Encoder_decoder Model We will use :
![model_architecture_2](https://user-images.githubusercontent.com/61959483/128484995-81763a95-f6b1-4de6-8982-73fcda6e9712.gif)


### <font color='green'>Training Results :</font>
![Screenshot (5)](https://user-images.githubusercontent.com/61959483/128485638-c44be5ca-1b8a-44f7-b6b1-4e0d73a49836.png)

### <font color='green'>Taking whole data pipeline in one predict Function & Translateting some senetnces by our model.</font>
#### Translating English Sentence to hindi_1 :
![Screenshot (9)](https://user-images.githubusercontent.com/61959483/128486877-c64fc5b5-da1d-4b6c-b0d4-e67e6c2fe88d.png)

#### Translating English Sentence to hindi_2 :
![Screenshot (10)](https://user-images.githubusercontent.com/61959483/128486962-071b2916-d71b-4ce8-b5a9-a4430051ff86.png)

#### Translating English Sentence to hindi_3 :
![Screenshot (11)](https://user-images.githubusercontent.com/61959483/128487115-5e2a5f84-51dc-4bec-bde0-224024dccb92.png)



## <font color='green'>See the ipynb file for whole code. Thank You..!! :) </font>

