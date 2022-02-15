import datetime

# Variables
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = []
date_list = []
answer_list = []

# Read the list of words
with open('wordlist.txt') as f:
    word_list = f.readlines()[0].split(',')

# Print the list of words
puzzle_id = 0
date = datetime.datetime(2021, 6, 19)
for i in range(len(word_list)):
    puzzle_id += 1
    date += datetime.timedelta(days=1)
    formatted_date = date.strftime('%Y-%m-%d')
    year = date.strftime('%Y')
    if year not in years:
        years.append(year)
    date_list.append(formatted_date)
    answer_list.append(f'Wordle {puzzle_id} ({formatted_date}) - {word_list[puzzle_id-1]}')

# Write to file
with open('README.md', 'w') as f:
    # Write the About section
    f.write('# About\n\nThis repo contains the comprehensive list of all Wordle answers, past and future, reverse engineered from the [Wordle](https://www.nytimes.com/games/wordle/index.html) source code and compiled into [Markdown](https://daringfireball.net/projects/markdown/) using [Python](https://www.python.org/). THIS REPO CONTAINS SPOILERS!')

    # Write the Table of Contents section
    # TODO: Link to proper areas
    f.write('\n\n## Table of Contents\n')
    for year in years:
        f.write(f'\n### {year}')
        for month in months:
            f.write(f'\n- {month}')


    # TODO: Write the Answers section
    f.write('\n\n## Answers\n')
    for item in answer_list:
        f.write(f'\n- {item}')
