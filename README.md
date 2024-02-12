# Google Foobar

Google foobar is a secret coding challange presented by Google to people who search for programming related questions or topics on Google. Foobar presents a series of coding challenges of increasing difficulty, covering various computer science concepts and problem-solving skills. It is designed to discover and recruit talented developers for potential job opportunities at Google.

However this has been going on for a while so a lot of people see it more as just a cool easter egg on google now. If you want to find out more information about it here is a [medium article by Mohit Gupta](https://itsmohitt.medium.com/things-you-should-know-about-google-foobar-invitation-703a535bf30f) from 2018.

I was lucky enough for this invite to randomly pop-up for me one day which was a pretty cool experience :) this repo contains the problems I was given and my solutions for them. Each problem allows you to solve it in either python or java. For the submissions I choose python mainly because I'm more familiar with it but for this repo I have also completed the challanges in java using gradle as my build tool.

# Repository Structure

This repository is organized into levels (level-1, level-2, etc.), each containing different coding challenges. Each challenge has its own directory, which includes a `README.md` file and a `solution.py` file. 

After completing the challange there is a an encrypted message, the `decrypt.py` file contains the code to decrypt this message, the key being the username for the account which the challange was completed, in my case deanlogan42.

The file `journal.txt` contains the logs after completing each of the challanges.

## Challenge Directories

Each challenge directory contains:

- A `README.md` file: This file contains the problem statement and any specific instructions or constraints for the challenge.
- A `solution.py` file: This file contains the Python code that solves the challenge.

## Running the Code

To run the solution for a specific challenge, run the `solution.py` file using Python by giving the corresponding folder directory. For example, to run the solution for the "braille-translation" challenge in level-1, you would use the following command:

```sh
python ./level-1/braille-translation/solution.py
```