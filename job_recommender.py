# Simple Job Recommendation System
# This program takes user skills as input
# and recommends job roles based on matching skills.

# Dictionary that maps job roles to required skills
job_roles = {
    "Data Analyst": ["python", "sql", "excel", "power bi", "tableau"],
    "Web Developer": ["html", "css", "javascript", "react", "node.js"],
    "Software Developer": ["python", "java", "c++", "git", "dsa"],
    "Machine Learning Engineer": ["python", "machine learning", "tensorflow", "pandas", "numpy"],
    "UI/UX Designer": ["figma", "adobe xd", "wireframing", "prototyping"],
    "Digital Marketer": ["seo", "content writing", "social media", "google ads"],
    "Cloud Engineer": ["aws", "azure", "docker", "kubernetes", "linux"]
}

# Take user input
user_input = input("Enter your skills (comma separated): ")

# Convert input into a list of cleaned, lowercase skills
user_skills = [skill.strip().lower() for skill in user_input.split(",")]

# Store recommended jobs with match scores
recommended_jobs = {}

# Check each job role
for job, skills in job_roles.items():
    match_count = 0

    # Count how many skills match
    for skill in skills:
        if skill in user_skills:
            match_count += 1

    # Recommend only if at least one skill matches
    if match_count > 0:
        recommended_jobs[job] = match_count

# Display results
if recommended_jobs:
    print("\nRecommended Job Roles:")
    
    # Sort jobs by highest number of matched skills
    sorted_jobs = sorted(recommended_jobs.items(), key=lambda x: x[1], reverse=True)
    
    for job, score in sorted_jobs:
        print(f"- {job} (matched skills: {score})")
else:
    print("\nNo matching job roles found.")
    print("Try adding more skills.")
