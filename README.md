

# Create key with Python gnupg (GPG)

[python-gnupg](https://code.google.com/archive/p/python-gnupg/) is a Python package for encrypting and decrypting strings or files using [GNU Privacy Guard (GnuPG or GPG)](https://en.wikipedia.org/wiki/GNU_Privacy_Guard). GPG is an open source alternative to Pretty Good Privacy (PGP). A popular use of GPG and PGP is encrypting email. For more information, see the [python-gnupg documentation](https://pythonhosted.org/python-gnupg/). Another option for encrypting data from Python is [keyczar](https://github.com/google/keyczar).

## Secret Sharing Schemes 


This module implements the Shamir’s secret sharing protocol described in the paper [“How to share a secret”](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.8910&rep=rep1&type=pdf).

The secret can be split into an arbitrary number of shares (n), such that it is sufficient to collect just k of them to reconstruct it (k < n). For instance, one may want to grant 16 people the ability to access a system with a pass code, at the condition that at least 3 of them are present at the same time. As they join their shares, the pass code is revealed. In that case, n=16 and k=3.

In the Shamir’s secret sharing scheme, the n shares are created by first defining a polynomial of degree k-1:

q(x)=a0+a1x+a2x2+…+ak−1xk−1

The coefficient a0 is fixed with the secret value. The coefficients a1…ak−1 are random and they are discarded as soon as the shares are created.

Each share is a pair (xi,yi), where xi is an arbitrary but unique number assigned to the share’s recipient and yi=q(xi).

This implementation has the following properties:

The secret is a byte string of 16 bytes (e.g. an AES 128 key).

Each share is a byte string of 16 bytes.

The recipients of the shares are assigned an integer starting from 1 (share number xi).

The polynomial q(x) is defined over the field GF(2128) with the same irriducible polynomial as used in AES-GCM: 1+x+x2+x7+x128.

It can be compatible with the popular ssss tool when used with the 128 bit security level and no dispersion: the command line arguments must include -s 128 -D. Note that ssss uses a slightly different polynomial:

r(x)=a0+a1x+a2x2+…+ak−1xk−1+xk

which requires you to specify ssss=True when calling split() and combine().

Each recipient needs to hold both the share number (xi, which is not confidential) and the secret (which needs to be protected securely).

## Installation requirements

Pleae find the necessary dependent libraries by running on your IDE: 

'''\ 
pip3 install -r requirements.txt\
'''
## Script Navigation
-   Run file_name.py file to encrypt your file
    -   Once you run this file you might need to give the desired file to be encrypted as input.

-   Run QQQ.py file to decrypt the file
    -   To decrypt a file user must need to set two inputs.
        -   The file path of the file to decrypt (alread encrypted one)
        -   Shared split Key
        


