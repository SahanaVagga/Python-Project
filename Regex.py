##1.read sentences and extract only line which contain the keywords
import pandas as pd
import re
# open file
keyword = open('Info.txt', 'r', encoding = 'utf-8').readlines()
texts = open('s.txt', 'r', encoding = 'utf-8').readlines()
# define function to read file and remove next line symbol
def read_file(file):
    texts = []
    for word in file:
        text = word.rstrip('\n')
        texts.append(text)
    return texts
# save to variable        
key = read_file(keyword)
corpus = read_file(texts)
#In the script above, the inputs are sentence tokens and the list of keywords stored in a text file. You may tokenize your dataset from documents into paragraphs or sentences, and then extract the paragraphs or sentences which contain the keywords. Sentence tokenization can be done easily with sent_tokenize from nltk.tokenize as below.
from nltk.tokenize import sent_tokenize
text = open('Input/data.txt', 'r', encoding = 'utf-8')
text_file = open("Output/sent_token.txt", "w", encoding='utf-8')
### This part to remove end line break
string_without_line_breaks = ""
for line in text:
    stripped_line = line.rstrip() + " "
    string_without_line_breaks += stripped_line
sent_token = sent_tokenize(string_without_line_breaks)
for word in sent_token:
    text_file.write(word)
    text_file.write("\n")
text_file.close()
#As the text data I used is extracted from a PDF file, there are a lot of line breaks, hence I will remove the line breaks before sentence tokenization.
#2. Write the function to extract the line
# open file to write line which contain keywords
file = open('Output/keyline.txt', 'w', encoding = 'utf-8') 
def write_file(file, keyword, corpus):    
    keyline = []      
    for line in corpus:
        line = line.lower()
        for key in keyword:
            result = re.search(r"(^|[^a-z])" + key + r"([^a-z]|$)", line)
            if result != None:
                keypair = [key, line]
                keyline.append(keypair) 
                file.write(line + " ")                                
                break                 
            else:
                pass                                            
          
    return(keyline)
output = write_file(file,key,corpus)
#The function above is the function I used to extract all the sentences which contain the keywords. A break is added to prevent copy the same line with multiple keywords to lower file size. The key script of doing so is just one line of code.
result = re.search(r"(^|[^a-z])" + key + r"([^a-z]|$)", line)
#The ”(^|[^a-z])” and ”([^a-z]|$)” surrounding the key is to make sure the word is identical with the keyword. For example, without these two part of the script, when we searching for a keyword like “act”, the result return might be the word “act” with prefix or suffix, such as “react” or “actor”.
# create DataFrame using data 
df = pd.DataFrame(output, columns =['Key', 'Line']) 
#After extract the lines, you may create DataFrame from the keywords and the respective line extracted for further analysis. Note that in my example, I do not extract the same line again if it contains multiple keywords. If you need to do so, you may remove the break command from the script above.
#That’s all on how to extract the line of sentences with keywords. Simple right?
#Last but not least, sharing a script I have been using lately, os.listdir.startswith() and os.listdir.endswith() which help you to get all the file you need efficiently. This is sort of a similar concept with Regular Expression, where we define a particular pattern, and then we search for it.
# collect txt file with name start with 'data' 
import os
path = 'C:/Users/Dataset txt'
folder = os.fsencode(path)
filenames_list = []
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.startswith( ('data') ) and filename.endswith( ('.txt') ): 
        filenames1.append(filename)
filenames_list.sort() 
