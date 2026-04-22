# Job Recommendation System using Machine Learning

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Training Data
skills = [
    "python sql",
    "java spring",
    "html css javascript",
    "python machine learning",
    "java backend api"
]

jobs = [
    "Data Analyst",
    "Backend Developer",
    "Frontend Developer",
    "ML Engineer",
    "Backend Developer"
]

# Step 2: Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(skills)

# Step 3: Train model
model = MultinomialNB()
model.fit(X, jobs)

# Step 4: Take user input
user_input = input("Enter your skills: ")

# Step 5: Convert input
user_vector = vectorizer.transform([user_input])

# Step 6: Predict
prediction = model.predict(user_vector)

# Step 7: Output result
print("Recommended Job Role:", prediction[0])
