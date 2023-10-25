# Import pandas under its usual alias
import pandas as pd
# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt

# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
# Create a dictionary with the two lists
movie_dict = {'years': years, 'durations': durations}
# Print the dictionary
print(movie_dict)



# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)
# Print the DataFrame
print(durations_df)



# Create a figure
fig = plt.figure()
# Draw a line plot of release_years and durations
plt.plot(years, durations)
# Create a title
plt.title("Netflix Movie Durations 2011-2020")
# Show the plot
plt.show()



# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/Netflix Datasets/netflix_data.csv")
# Print the first five rows of the DataFrame
print(netflix_df[:5])


# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type']=='Movie']
# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]
# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset[:5])