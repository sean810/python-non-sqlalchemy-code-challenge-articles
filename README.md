# Phase 3 Code Challenge: Articles - without SQLAlchemy (Updated)
Magazine Article Management System.

Welcome to the Magazine Article Management System! This project allows you to manage the relationships between authors, articles, and magazines. You can create authors, assign articles to them, and link articles to magazines. The system also enables you to explore various features such as searching for authors by their articles, finding contributors to a specific magazine, and much more.
In this code challenge, you will be working with a Magazine domain.

We have three models: `Author`, `Article`, and `Magazine`.

For our purposes, an `Author` has many `Article`s, a `Magazine` has many
`Article`s, and `Article`s belong to both `Author` and `Magazine`.

`Author` - `Magazine` is a many to many relationship.

## Instructions

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You can
run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python lib/debug.py` from the command line. This will start a `ipdb`
session with your classes defined. You can test out the methods that you write
here. You can add code to the `lib/debug.py` file to define variables and create
sample instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Features
Author:

View articles written by the author.
View magazines the author has contributed to.
Add new articles with validation for title and magazine.
Get unique categories of magazines the author has contributed to.

Article:

Each article is linked to an author and a magazine.
The article title is validated and immutable.
Track all created articles globally.

Magazine:

List articles published in the magazine.
Get authors who contributed to the magazine.
Get all article titles in the magazine.
Find authors who wrote more than two articles for the magazine.
Find the magazine with the most articles.

## Setup
Run pipenv install while inside of this directory. Then run pipenv shell to jump into the shell.
Use python lib/debug.py in you're command line to start a ipdb session tehn run pytest to check if you're code is passing the tests or failing the tests. 

### Features
Add New Plants: Users can add new plants to the store with details such as name, image URL, and price.
Search Plants: The app allows users to search for plants by name.
Mark Sold Out: Users can mark plants as sold out or available.
Delete Plants: Users can delete plants from the store.
Responsive Design: The app is mobile-friendly, displaying plant cards in a grid that adjusts for different screen sizes.
Backend Integration: Uses JSON Server to simulate a backend and store plant data.

### Development
If you want to contribute or develop further features, follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature-name.
Commit your changes: git commit -m "Your commit message".
Push to your branch: git push origin feature-name.
Open a pull request with a description of your changes.

### Technologies Used
Python 3.x: The programming language used to build the system.
Classes: Implemented using object-oriented principles to manage the relationships between authors, articles, and magazines.

### Acknowledgments
Python: A versatile programming language for building this system.

Object-Oriented Programming: Used to model the relationships between authors, articles, and magazines.

