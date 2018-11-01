Simple File Uploader
====================

* This project is python2.7 compatible

* Install and initialize virtualenv: https://virtualenv.pypa.io/en/stable/installation/

* Activate virtualenv with command
.. code-block:: shell

    source bin/acttivate
    
* Pull code
.. code-block:: shell

    git clone git@github.com:hritik09/simple-file-uploader.git
    
* cd into folder
.. code-block:: shell

    cd simple-file-uploader

* Install dependencies
.. code-block:: shell

    pip install -r requirements.txt

* To run server
.. code-block:: shell

    python main.py

* To upload asset to presigned url
.. code-block:: shell

    curl --request PUT --upload-file <path-to-file> <presigned_url>

* To test util
.. code-block:: shell

    cd tests && python util_tests.py

* To test api run server first and then in another terminal run
.. code-block:: shell

    cd tests && python api_tests.py





