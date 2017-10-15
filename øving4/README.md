## Task D)
To run this code, you have to have following modules for python installed:
- scipy
- matplotlib
- structured
- scipy
- connections (see installing connections)
- pybrain

### Install pybrain
pip install https://github.com/pybrain/pybrain/archive/0.3.3.zip --> this supports python3.

### To install connections modules
if your using wirtuelenvwrapper
`cdsitepackes`
`git clone https://github.com/operetta/connections.git && cd connections`
change `line 283` in `connections.py` to `except SocketError as e`
`python setup.py install`


Make sure to install them in that order
