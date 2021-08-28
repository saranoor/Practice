import re
import string
from unicodedata import normalize
import numpy

# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, mode='rt', encoding='utf-8')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


# split a loaded document into sentences
def to_pairs(doc):
    lines = doc.strip().split('\n')
    pairs = [line.split('\t') for line in  lines]
    return pairs

def clean_data(lines):
    cleaned = list()
    # prepare regex for char filtering
    re_print = re.compile('[^%s]' % re.escape(string.printable))
    # prepare translation table for removing punctuation
    table = str.maketrans('', '', string.punctuation)
    for pair in lines:
        clean_pair = list()
        for line in pair:
            # normalize unicode characters
            line = normalize('NFD', line).encode('ascii', 'ignore')
            line = line.decode('UTF-8')
            # tokenize on white space
            line = line.split()
            # convert to lowercase
            line = [word.lower() for word in line]
            # remove punctuation from each token
            line = [word.translate(table) for word in line]
            # remove non-printable chars form each token
            line = [re_print.sub('', w) for w in line]
            # remove tokens with numbers in them
            line = [word for word in line if word.isalpha()]
            # store as string
            clean_pair.append(' '.join(line))
        cleaned.append(clean_pair)
    return numpy.array(cleaned)

filename=r'C:\New_partition\CS_583\HW_5\deu-eng\deu.txt'
n_train =20000
doc = load_doc(filename)

# split into Language1-Language2 pairs
pairs = to_pairs(doc)

# clean sentences
clean_pairs = clean_data(pairs)[0:n_train, :]
for i in range(3000, 3010):
    print('[' + clean_pairs[i, 0] + '] => [' + clean_pairs[i, 1] + ']')


input_texts = clean_pairs[:, 0]
target_texts = ['\t' + text + '\n' for text in clean_pairs[:, 1]]

print('Length of input_texts:  ' + str(input_texts.shape))
print('Length of target_texts: ' + str(input_texts.shape))
max_encoder_seq_length = max(len(line) for line in input_texts)
max_decoder_seq_length = max(len(line) for line in target_texts)

print('max length of input  sentences: %d' % (max_encoder_seq_length))
print('max length of target sentences: %d' % (max_decoder_seq_length))




# encode and pad sequences



import json

x = {
  "page": 1,
  "per_page": 30,
  "total": True,
  "total_pages": 100,
  "data": [
    {"title": "BMW 23", "story_title": 'lets talk about car'},
    {"title": "", "story_title": 'lets talk about car'},
    {"title": '', "story_title": ''}
    
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
json_y=json.loads(y)

#articles=[]
#data_len=len(json_y['data'])
#for article_record in range (0,data_len):
#    title=json_y['data'][article_record]['title']
#    story_title=json_y['data'][article_record]['story_title']
#    if json_y['data'][article_record]['title']!='null':
#        articles.append(title)
#    elif json_y['data'][article_record]['title']!='null':
#        articles.append(story_title)        
#print(articles)

def get_article_titel(author):
    import requests
    articles=[]
    page=1
    while(True):
        url='https://jsonmock.hackerank.com/api/articles?author='+author+'&page='+str(page)
        if page==1:
            total_pages=json_y['total_pages']
        json_y=requests.get(url)
        ##process
        if page==total_pages:
            break
        else:
            page=page+1
    
        



