

# Create key with Python gnupg (GPG wrapper for python)

[python-gnupg](https://code.google.com/archive/p/python-gnupg/) is a Python package for encrypting and decrypting strings or files using [GNU Privacy Guard (GnuPG or GPG)](https://en.wikipedia.org/wiki/GNU_Privacy_Guard). GPG is an open source alternative to Pretty Good Privacy (PGP). A popular use of GPG and PGP is encrypting email. For more information, see the [python-gnupg documentation](https://pythonhosted.org/python-gnupg/). Another option for encrypting data from Python is [keyczar](https://github.com/google/keyczar).

## Secret Sharing Schemes 


This module implements the Shamir’s secret sharing protocol described in the paper [“How to share a secret”](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.8910&rep=rep1&type=pdf).

The secret can be split into an arbitrary number of shares (n), such that it is sufficient to collect just k of them to reconstruct it (k < n). For instance, one may want to grant 16 people the ability to access a system with a pass code, at the condition that at least 3 of them are present at the same time. As they join their shares, the pass code is revealed. In that case, n=16 and k=3.


This implementation has the following properties:

-   The secret is a byte string of 16 bytes (e.g. an AES 128 key).

-   Each share is a byte string of 16 bytes.

-   The recipients of the shares are assigned an integer starting from 1.

Each recipient needs to hold both the share number (xi, which is not confidential) and the secret (which needs to be protected securely).

## Installation requirements

Pleae find the necessary dependent libraries by running on your IDE: 

````
pip install -r requirements.txt
````
## Script Navigation

To run the programme :
```
py encrypt_decrypt.py
 
```
You will have options:
-   To encrypt the file (Input 1)
    -   Enter absolute file file path with file name
        - Should see the result (found the file inside same directory (given file path) ) and share part inside directory (store_share_code)
        with file name 
        

-   To decrypt the file (Input 2)
    - Enter absolute file file path with file name
    - Enter share part (minimum two)
        - Should see the result and found the file inside same directory (given file path) 
