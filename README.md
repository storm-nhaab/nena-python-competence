# The Nena Python Course
A course in using python and related tools within the Nena analyst team.

## What this course will cover

This course will basic usage of the python programming language and some of the most popular 
python-related tools. By the end of the course you will know how to use basic python
to automate tasks, do simple mathematical modelling, implement python code in Excel and
how python can be used to communicated with a web API.

We will have 8 sessons, one hour each, once a week. You should already have a scheduled event in your
Outlook calendar.

Here is a preliminary course schedule:

### Week 0 : Before the course starts.
- Read *Chapter 1* of the course book.

### Week 1 (19/04) : Setting up a python environment. 
__Reading before the session__: *Chapter 2* of the course book. Focus on the chapter related to Jupyter Notebook. Please skip sections related to MacOS.
- Set up a working python environment, install necessary tools such as jupyter lab and VS Code.
- We will cover the use of the Windows Terminal to navigate the windows file system.
- Start up Jupyter Lab and VS Code. <br>
- Reading python documentation.
- Using GitHub and basic git with GitHub desktop.

### Week 2 (26/04) : Basic Python syntax.
__Reading before the session__: *Chapter 3 pages 43-67*. Before the session I expect you to know *pages 43-49*. These will not be covered in the session.
- Python data types e.g. Dictionaries, Lists, Tuples.
- For and While loops. If, Elif, Else statements.
- Writing Python Functions.
- What is a python module and how do we import it into a jupyter notebook?
- Writing basic python scripts and run them in Jupyter Notebook and the Windows Terminal.

### Week 3 (3/05) : Using Pandas for data analysis (1 of 2). 
__Reading before the session__: *Chapter 5 pages 85-102  & 119-123. Chapter 4 pages 143-154*
- Go over the Pandas library. What can we use it for.
- How to read various files into Pandas.
- Manipulate dataframes, select columns, slice data by row index.
- Write dataframes to a file, e.g. csv and xlsx.

### Week 4 (10/05) : Using Pandas for data analysis + Numpy (2 of 2).
__Reading before the session__: *Chapter 5 pages 103-119. Chapter 4.*
- Doing computations with Pandas. 
- Do basic statistics with pandas 
- Plot a dataframe
- Working with Numpy for more efficient computations.

### Week 5 (24/05) : Working with Pandas for time series data and regression with Scikit-Learn.
__Reading before the session__. *Chapter 6 and Chapter 3 pages 69-70.*
- The python datetime module.
- How can we work efficiently with time series data using Pandas.
- Using Scikit learn for basic linear regression (Ordinary least-squares, Ridge regression)

### Week 6 (31/05 - 14/06) : Using python with Excel.
__Reading before the session__: Chapter 9, 10, 12.
The rest of the course is devoted to how we can use Python with Excel. Details will be provided shortly.

## The Graduation Project
We will finish this course by everyone doing their own Excel-Python project.
In the final session, each person will present their project for the rest of the class.
In *chapter 11* of the book you will find an example on a projet. However, we will do something
with a smaller scope. I will be around to help you get started and guide you through your project.

Ex. could be:
- Create a simple linear regression model with python and use the python module with Excel.
- Create automation macros in excel to speed up your analysis.
- Write a script which automates a task you are doing repetedly.

## To-Do
Before you take the course you should prepare the following:

1. Create a github user. You use your stormgeo email. Stormgeo uses a username naming convention
   on the form: "storm-XXXX" where XXXX is your stormgeo initials e.g. mine are nhaab so my github username
   is storm-nhaab.
2. Install [Anaconda](https://www.anaconda.com/) on your local machine. The installastion should be done with
   admin privilages. Please use "Request Admin" and obtain access before atempting to install anaconda.
   
   I advise that you add anaconda to your PATH. So choose the RIGHT option!
   ![alt_text](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1528926970/AnacondaOptions_e8jugh.png)

   
3. Install [GitHub desktop](https://desktop.github.com/)
4. Install [Windows Terminal](https://www.microsoft.com/nb-no/p/windows-terminal/9n0dx20hk701) from the Microsoft Store. 
5. Read Chapter 1 of the course book.

## Course literature

This course will have a course book.
The book is called [Python For Excel](https://www.amazon.com/Python-Excel-Environment-Automation-Analysis-ebook-dp-B08Y3TKQ5V/dp/B08Y3TKQ5V/ref=mt_other?_encoding=UTF8&me=&qid=) and every analyst will get a copy. I expect you to do some reading in course book. Prior to each tutorial session I have outlined a reading recommendation for the book.

![alt_text](https://s1.adlibris.com/images/59291723/python-for-excel.jpg)



## Usefull preparation

I recommend everyone to visit this site: https://pbpython.com/
It is a blog about how to do Excel related tasks in Python.

## Inspiration

I advise you to lsiten to the following podcast which talks about how you can use Python with Excel.
  * [Escaping Excel hell with Python](https://talkpython.fm/episodes/show/200/escaping-excel-hell-with-python-and-pandas)
  * [10 tips to move from Excel to Python](https://talkpython.fm/episodes/show/288/10-tips-to-move-from-excel-to-python)
 
Python can do many many things. Where Python shines is as a tool for data exploration, model building, and task automation.

A few usefull python libraries are listed here:

* XLWings - Automate Excel with Python : https://www.xlwings.org/
* Numpy - Work with Matrices and Vectors. A library to do highly efficient computations. : https://numpy.org/
* Scikit-Learn - Create simple linear regression models to state of the art Machine Learning models : https://scikit-learn.org/
* Statsmodels - Covers most features for doing statistical analysis and statistical tests : https://www.statsmodels.org/devel/index.html
* Pandas - Read, Write, and Manipulate large datasets, similar to Excel but much more efficient: https://pandas.pydata.org/
* Seaborn and Matplotlib - Two popular plotting libraries for visualizing data. : https://seaborn.pydata.org/ & https://matplotlib.org/

