# BookRecommendation

### Book Recommendation System using Collaborative Filtering
This is a simple book recommendation system that uses collaborative filtering to recommend books to users. Collaborative filtering is a technique that uses the ratings of users to recommend items to other users who have similar tastes.

Prerequisites
Before running the system, you will need to have Python 3 installed on your computer. You will also need to install the following packages:

- pandas
- numpy
- scikit-learn
You can install these packages using pip by running the following command in your terminal:

Copy code
```
--pip install pandas numpy scikit-learn
```

### Usage
To use the system, follow these steps:

- Download or clone the repository to your computer.Navigate to the directory where the repository is located.
- Open the file book_recommendation_system.py in a text editor.
- Update the file path for the books.csv and ratings.csv files to the location where you have stored these files on your computer.
- Save the changes to the file.
- Open a terminal window and navigate to the directory where the repository is located.
- Run the command python app.py.

### The system uses two CSV files as input:

books.csv : contains information about the books, including the book ID, title, author, and year of publication.
ratings.csv contains information about the ratings given by users to books. Each row in the file contains a user ID, book ID, and rating.

ratings.csv contains information about the ratings given by users to books. Each row in the file contains a user ID, book ID, and rating.
users.csv : contains information about the users like user ID , Age.
<br/>
### Algorithm
The recommendation system uses the K-nearest neighbors algorithm to find similar users based on their ratings. The system then recommends books to the user based on the ratings of the similar users.

### Some Screen shots (Because I haven't deployed it yet..)

 ![image](https://github.com/Geeky-Sam01/BookRecommendation/assets/71366418/37c94d3b-7158-491d-8d49-b98164cf3665)
 ![image](https://github.com/Geeky-Sam01/BookRecommendation/assets/71366418/11b66e28-5376-40aa-ba02-cb5e04c2d381)
 ![image](https://github.com/Geeky-Sam01/BookRecommendation/assets/71366418/1043ed7f-9a69-4746-a0c4-9d5b9cbba6a4)
 ![image](https://github.com/Geeky-Sam01/BookRecommendation/assets/71366418/160c970b-60bc-4a06-aa08-8d0fbfcfbf81)


License
This project is licensed under the MIT License - see the LICENSE file for details.
