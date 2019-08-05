import spacy
import multiprocess

import stopwatch
from spacy.tokenizer import Tokenizer
import time


spacy_nlp = spacy.load('en_core_web_sm')

#print(spacy_nlp.pipe_names)

def test(i):    
    txt_1st = "this is the first sentence of {}".format(i)
    txt_2nd = "this is the second sentence of {}".format(i)
    
    #print(txt_1st)
    parsed_txt_1st = spacy_nlp(txt_1st)
    #print(txt_2nd)
    parsed_txt_2nd = spacy_nlp(txt_2nd)
    return parsed_txt_1st, parsed_txt_2nd

def test2(i):
  def process_test(text_array):

    results = spacy_nlp(text_array)
    return results
      
  text1 = "this is the first sentence of {}".format(i)
  result1 = process_test(text1)
  
  text2 = "this is the second sentence of {}".format(i)
  result2 = process_test(text2)

  
  return result1, result2
  
  
pool = multiprocess.Pool(processes=4)
start_time = time.perf_counter()      # 2

#data = range(100000)
data = range(1)
if True:
  # on 10000 155 seconds
  func = test
if False:
  # on 10000 153 seconds 
  func = test2


if True:
  # for test1 with 100k cycle, time taken is 1500 seconds
  results = [func(i) for i in data]

if False:
  #wrap = stopwatch.timer(pool.map)
  #results = wrap(func, data)
  
  # using this on 10000 is 50.5924 seconds
  # for test1 with 100k cycle, time taken is 452.4128 seconds
  results = pool.map(func,data)
  
end_time = time.perf_counter()

print(results)

run_time = end_time - start_time    # 3
print(f"Finished in {run_time:.4f} secs")



