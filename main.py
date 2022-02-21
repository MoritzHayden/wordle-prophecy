import datetime
from pytz import timezone

# Variables
months_indices = ['01', '02', '03', '04', '05',
                  '06', '07', '08', '09', '10', '11', '12']
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
years = []
date_list = []
answer_list = []

# Read the list of words
with open('wordlist.txt') as f:
    word_list = f.readlines()[0].split(',')

# Assemble and format the answers
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
    formatted_date = date.strftime('%B %d, %Y')
    answer_list.append(
        f'Wordle {puzzle_id} ({formatted_date}) - **{word_list[puzzle_id-1]}**')

# Write to file
with open('README.md', 'w') as f:
    # Write the H1 section
    f.write('# Wordle Prophecy')

    # Write the Recent Answers section
    f.write('\n\n## Recent Answers (Refreshes at 12:00 AM ET)\n\n')
    tz = timezone('US/Eastern')
    originDate = datetime.datetime(2021, 6, 20).replace(tzinfo=tz)
    today = datetime.datetime.now(tz)
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    todayDelta = (today - originDate).days
    f.write('| Date | Answer |\n')
    f.write('| --- | --- |\n')
    f.write(
        f'| Yesterday ({yesterday.strftime("%B %d, %Y")}) | **{word_list[todayDelta-1]}** |\n')
    f.write(
        f'| Today ({today.strftime("%B %d, %Y")}) | **{word_list[todayDelta]}** |\n')
    f.write(
        f'| Tomorrow ({tomorrow.strftime("%B %d, %Y")}) | **{word_list[todayDelta+1]}** |\n')

    # Write the Table of Contents section
    f.write('\n\n## Table of Contents\n')
    for year in years:
        f.write(f'\n### {year}')
        for m in range(len(months)):
            if (not (((year == '2021') and (m in (0, 1, 2, 3, 4))) or (year == '2027' and m in (10, 11)))):
                f.write(f'\n- [{months[m]}](#{year}---{months[m].lower()})')

    # Write the Answers section
    f.write('\n\n## Answers\n')
    for year in years:
        for m in range(len(months)):
            if (not (((year == '2021') and (m in (0, 1, 2, 3, 4))) or (year == '2027' and m in (10, 11)))):
                f.write(f'\n### {year} - {months[m]}')
                for i in range(len(answer_list)):
                    if (f'{year}-{months_indices[m]}' in date_list[i]):
                        f.write(f'\n- {answer_list[i]}')
