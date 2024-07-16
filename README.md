# python-challenge

This repository is for the module 3 python challenge assignment. There is a folder for both parts of this challenge, `PyBank` and `PyPoll`. Each folder contains its own python script as a `.py` file, as well as `Resource` and `Analysis` folders which contain the input `.csv` files and the output `.txt` files, respectively.

If the repository is cloned or downloaded from this page and the file organization is maintained as it appears here, the file path commands should work properly, finding the `.csv` files from the `Resources` folders and outputting the `.txt` files into the `Analysis` folders for both `PyBank` and `PyPoll`. This `.txt` file, which is exported when running the code, can be deleted for testing purposes. They should be recreated identically as they appear in the repo upon running the code.

I used the Anaconda Prompt on my Windows 10 machine to run and debug my code.

## PyBank

Most of the code for `PyBank` was influenced by the Module 3 Day 2 activities, such as `09-Stu_ReadComicBooksCSV` and `12-Stu_CensusZip`, which detail how to set up csv reading and writing, as well as how to use row indices to find the proper data and manipulate it. I also had some help from ChatGPT for debugging the code, as well as for the syntax on the `textfile.write` sections.

## PyPoll

`PyPoll` similarly draws from the Module 3 activities, such as `03-Stu_HobbyBook-Dictionaries`, which details some of the syntax used in the creation and printing of dictionaries. I did `PyBank` first, so I was also able to draw from that in writing this code. I again here had some help from ChatGPT, which was useful in providing me with the `candidateVotes.items()` method which helped me get my dictionary lookup and printing functions working.

I was having trouble using the `max` function to go through the dictionary and properly determine the winner's name corresponding to the highest vote count, and ChatGPT also helped me fix this by suggesting the `key=candidateVotes.get` argument. This fixed the issue by going through each candidate name, getting the number of votes each has, determining which number is highest, and returning the key--in this case, the candidate name--which corresponds to that value. 
