*****************
Trality Simulator
*****************

Intro
=====
This package is a work in progress. It allows local development of Trality bots in an IDE such as VS Code. The package provides dummy modules and functions so that the IDE does not complain and you can use flake8 and black for code formatting and finding errors before running your bot.

Caveats/Quirks
==============
This package does not interface directly with Trality. You still have to copy and paste your code between your IDE and the browser.

Goals
=====
1. Allow local development with linting and auto formatting
#. Allow local backtesting

   #. With parametric input to determine best results among many variables

Current State
=============
- Allows linting (via flake8 or your chosen linter).
- Allows automatic code formatting (via black or another tool).
- Implements many of the basic Trality functions as dummy (empyt) functions.
 
  * Does not currently implement many of the indicators (as shells)

Getting Started
===============
See dca.py in the examples directory, it shows how to import the proper modules and functions into your code for local development.

Local Installation
==================

Using poetry
------------
| ``$ pip install --user poetry``
| ``$ git clone git@github.com:Cryptrality/trality-simulator.git``
| ``$ cd trality-simulator``
| ``$ poetry install``

Using pip
---------
Not possible yet. Section will be updated when package is on PyPI.

After Install
-------------
1. Create a python file for each one of your Trality bots.
#. At the top of the file, import want you need from trality_simulator.
   
   #. See examples/dca.py for an example.
#. Setup your IDE to do linting and/or auto formatting however you prefer.


