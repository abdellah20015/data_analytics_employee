import pandas as pd

# Define the data
data = {
    'Employee Name': ['Kwame Osei', 'Amina Abiola', 'Mpho Ndlovu', 'Ifeoma Okoro', 'Sadio Traore', 'Tariq Juma', 'Aisha Kamara', 'Oluwaseun Adekunle', 'Nia Nkrumah', 'Mounir Diop'],
    'Performance Rating': [8, 6, 9, 7, 6, 9, 8, 7, 9, 8],
    'Training Completion': ['yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no'],
    'Course Name': ['Data Analysis', 'Python Programming', 'Machine Learning', 'Web Development', 'Database Management', 'Cybersecurity', 'Project Management', 'Software Testing', 'Data Visualization', 'Network Security']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Total number of employees
total_employees = df['Employee Name'].count()
print(f"Total number of employees: {total_employees}")

# Average performance rating of the employees who completed the training
average_rating = df[df['Training Completion'] == 'yes']['Performance Rating'].mean()
print(f"Average performance rating of the employees who completed the training: {average_rating}")

# Sum of the performance ratings for employees who completed the Data Analysis course
sum_rating_data_analysis = df[df['Course Name'] == 'Data Analysis']['Performance Rating'].sum()
print(f"Sum of the performance ratings for employees who completed the Data Analysis course: {sum_rating_data_analysis}")

# Number of employees who have a rating of 9 or above
num_employees_high_rating = df[df['Performance Rating'] >= 9]['Employee Name'].count()
print(f"Number of employees who have a rating of 9 or above: {num_employees_high_rating}")


