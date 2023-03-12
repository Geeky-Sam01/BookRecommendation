# BookRecommendation

Book Recommendation System using Collaborative Filtering
This is a simple book recommendation system that uses collaborative filtering to recommend books to users. Collaborative filtering is a technique that uses the ratings of users to recommend items to other users who have similar tastes.

Prerequisites
Before running the system, you will need to have Python 3 installed on your computer. You will also need to install the following packages:

pandas
numpy
scikit-learn
You can install these packages using pip by running the following command in your terminal:

Copy code
--pip install pandas numpy scikit-learn
Usage
To use the system, follow these steps:

Download or clone the repository to your computer.Navigate to the directory where the repository is located.
Open the file book_recommendation_system.py in a text editor.
Update the file path for the books.csv and ratings.csv files to the location where you have stored these files on your computer.
Save the changes to the file.
Open a terminal window and navigate to the directory where the repository is located.
Run the command python book_recommendation_system.py.
The system will prompt you to enter a user ID for whom you want to generate book recommendations.
Enter a user ID and press enter.
The system will generate a list of book recommendations for the user based on their ratings and the ratings of other users with similar tastes.
 Data
The system uses two CSV files as input:

books.csv : contains information about the books, including the book ID, title, author, and year of publication.
ratings.csv contains information about the ratings given by users to books. Each row in the file contains a user ID, book ID, and rating.
Algorithm
ratings.csv contains information about the ratings given by users to books. Each row in the file contains a user ID, book ID, and rating.
users.csv : contains information about the users like user ID , Age.
The recommendation system uses the K-nearest neighbors algorithm to find similar users based on their ratings. The system then recommends books to the user based on the ratings of the similar users.

License
This project is licensed under the MIT License - see the LICENSE file for details.
