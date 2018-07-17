# Table of Contents
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [Instructions](README.md#instructions)
4. [Output](README.md#output)
5. [Runnning the tests](README.md#running-the-tests)



# Problem

This project is to generate a list of all drugs for an online pharmacy, including the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.  

# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Instructions

Python 3.5.2 was used.

# Output 

The output file, `top_cost_drug.txt`, contains comma (`,`) separated fields in each line.

Each line of this file contains these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

# Running the tests

## Repo directory structure

The directory structure looks like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt


## Testing directory structure and output format

The test has been run with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 
passed. 

