#Purpose of this repo
to explore the various ways of parellise codes and which is a better choice

#Instructions
this runs on python3
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements
python -m spacy download en_core_web_sm

python multiprocessing_mp.py

