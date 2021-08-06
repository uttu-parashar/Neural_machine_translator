#                                                               ** Neural_machine_translator **

## Objective of project :--  Building a machine_translator ,Which can translate an English Sentence to Hindi.
### *Here We will Implement a Custon Endocer_Dedocder(Seq-2-Seq) Model to archive our goal.*

#### <font color='green'>Introduction of the dataset, We will use :</font>
We will use a Coupus published by IIT-Bombay. This corpus contains 1.6 Million santence pairs(Eng-Hindi) of both languages.The IIT Bombay English-Hindi corpus contains parallel corpus for English-Hindi as well as monolingual Hindi corpus collected from a variety of existing sources and corpora developed at the Center for Indian Language Technology, IIT Bombay over the years. This corpus has been used at the Workshop on Asian Language Translation Shared Task since 2016 the Hindi-to-English and English-to-Hindi languages pairs and as a pivot language pair for the Hindi-to-Japanese and Japanese-to-Hindi language pairs. To find more About the corpus ,Please go through the link given bellow : 
           
      https://www.cfilt.iitb.ac.in/~parallelcorp/iitb_en_hi_parallel/

After Unziping the initial Corpus i get two folders :
    
    1 - IITB.en-hi.en.txt (contains 1.6 million English Sentences.)
    2 - IITB.en-hi.hi.txt (contains Hindi translation of each corresponding English Sentence.)
    
#### <font color='green'>Architecture of Encoder_decoder Model We will use :</font>
![model_architecture_2](https://user-images.githubusercontent.com/61959483/128484995-81763a95-f6b1-4de6-8982-73fcda6e9712.gif)

