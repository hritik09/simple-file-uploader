Simple File Uploader
====================

* This project is python2.7 compatible

* Install and initialize virtualenv: https://virtualenv.pypa.io/en/stable/installation/

* Activate virtualenv with command
`source bin/activate`
    
* Pull code
`git clone git@github.com:hritik09/simple-file-uploader.git`
    
* cd into folder
`cd simple-file-uploader`

* Install dependencies
`pip install -r requirements.txt`

* To run server
`python main.py`

* To upload asset to presigned url
`curl --request PUT --upload-file <path-to-file> <presigned_url>`

* To test util
`cd tests && python util_tests.py`

* To test api run server first and then in another terminal run
`cd tests && python api_tests.py`





