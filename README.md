# marathon-pace-strategy

## About The Project

### Introduction

This project analyzes marathon pace strategy using data scraped from the 2021 Boston Marathon results. For purposes of this project, "pace strategy" can generally be broken down into three types that will be referred to throughout this project:

* "Even pacing" refers to running the second half of the race about as fast as the first half.
* "Positive splits" refers to running the second half of the race slower than the first half.
* "Negative splits" refers to running the second half of the race faster than the first half.

This project attempts to answer the following questions for runners age 18-39 who finished the 2021 Boston Marathon in less than 5 hours:

1. Is there any relationship between marathon finish time and pace strategy?
2. Is there any relationship between a runner's gender and their marathon pace strategy?
3. Does the relationship of marathon finish time to pace strategy depend on a runner's gender, or does the relationship of gender to pace strategy depend on a runner's finish time?

### Background

Previous research has generally found differences in marathon pacing for runners of different ability levels, but has been mixed on differences in marathon pacing for runners of different genders. Jared Ward, an American runner who placed 6th in the 2016 Olympic Marathon, also wrote a masters thesis on marathon pace strategy. He analyzed split times for runners in the 2013 St. George Marathon. He found that elite runners tend to run more evenly paced races than non-elite runners, who tend to slow more in the second half of the race. He also found that women tend to run more evenly paced races than men, but elite men and women run more similarly to each other [1].

Alejandro Santos-Lozano et al. studied finishers of the New York Marathon from 2006 to 2011 to examine the impact of ability level and gender on marathon pacing. They found that all runners tend to adopt a positive splits strategy, but that faster runners tend to run more evenly paced races regardless of gender. However, they didn't find significant differences between men and women [2]. Daniel March et al. studied runners in the Last Chance Marathon in Dublin, OH from 2005 to 2007. They found that women and faster runners tend to run more evenly paced races than men and slower runners respectively. However, they did not find any statistically significant interactions between gender and runner ability [3].

Finally, it is also worth noting that four of the last six marathon world records and the two fastest (official) marathons ever run were all actually run with a negative splits strategy, though still fairly close to even pacing [4-5].

### Data

The data for this project comes from the [2021 Boston Marathon results](https://boston.r.mikatiming.com/2021/?pid=leaderboard&pidp=leaderboard) on the Boston Athletic Association website. The data was scraped using the scrapy library for Python. The code for the scraper is included in the [marathon_scraper](https://github.com/tommcd09/marathon-pace-strategy/tree/main/marathon_scraper) folder of this project. Unfortunately, the BAA does not allow publishing or reposting Boston Marathon results without expressed written consent from the BAA, so the data is not reproduced with this project. However, the data can be obtained and viewed directly from the BAA website.

The raw data contains the following columns:

* <b>place_overall:</b> The runner's overall placing in the race.
* <b>place_gender:</b> The runner's placing within their gender
* <b>place_division:</b> The runner's placing within their age and gender group.
* <b>sex:</b> The runner's gender. Relabeled "gender" during cleaning.
* <b>age_group:</b> An integer representing the runner's age group. These integers were encoded in the URLs of marathon results pages and were used both to crawl through the results and to label the age groups. The numbers map to the following age groups: 1 = 18-39, 2 = 40-44, 9 = 45-49, 3 = 50-54, 10 = 55-59, 4 = 60-64, 11 = 65-69, 8 = 70-74, 12 = 75-79, 13 = 80+.
* <b>name:</b> The runner's first name, last name, and three letter country code.
* <b>bib:</b> The runner's unique bib number. Relabeled "runner_id" during cleaning.
* <b>half_split:</b> The runner's time for the first half of the marathon. Relabeled "first_half" during cleaning.
* <b>finish_net:</b> The runner's finish time measured from the time they crossed the starting line to the time they crossed the finish line. Relabeled "finish" during cleaning.
* <b>finish_gun:</b> The runner's finish time measured from the time of the starting gun to the time they crossed the finish line.

### Data

The data for this project consists of results from the 2021 Boston Marathon scraped from the BAA website using the code in the marathon_scraper folder. Unfortunately, the BAA does not allow publishing or reposting Boston Marathon results without expressed written consent from the BAA, so the data is not reproduced in this repository. However, the data can be obtained and viewed directly from the [BAA website](https://www.baa.org/races/boston-marathon/results/search-results).

The scraped data I used contains the following columns:
* <b>place_overall:</b> The runner's overall placing in the race.
* <b>place_gender:</b> The runner's place within their sex (M or W). Relabeled "place_sex" during cleaning.
* <b>place_division:</b> The runner's place within their age and sex group.
* <b>sex:</b> The runner's sex (M or W)
* <b>age_group:</b> An integer representing the runner's age group. These integers were scraped from the URLs of results pages and map to the following values: 1 = 18-39, 2 = 40-44, 9 = 45-49, 3 = 50-54, 10 = 55-59, 4 = 60-64, 11 = 65-69, 8 = 70-74, 12 = 75-79, 13 = 80+.
* <b>name:</b> The runner's name and three letter country code in the form "Last Name, First Name (COU)".
* <b>bib:</b> The runner's unique bib number. Relabeled "runner_id" during cleaning.
* <b>half_split:</b> The runner's time for the first half of the marathon.
* <b>finish_net:</b> The runner's finish time measured from the time they crossed the starting line to the time they crossed the finish line.
* <b>finish_gun:</b> The runner's finish time measured from the time of the starting gun to the time they crossed the finish line.

### Project Organization and Methodology

To answer the project questions, this project runs a 2x2 factorial ANOVA on the data for runners age 18-39, breaking them into groups based on gender and whether they ran a Boston Marathon qualifying time during the race.

The project code is broken into several parts:

* The scraper folder contains the code for the scrapy project used to scrape the Boston Marathon data from the results pages. The boston_spider.py file is the code written to scrape the data, while most of the rest of the code is standard scrapy project code.
* The cleaning.ipynb notebook cleans the scraped data.
* The exploratory_data_analysis.ipynb notebook explores the data cleaned in the cleaning notebook.
* The anova.ipnyb notebook contains the experiment setup and the ANOVA itself, along with assumption testing, estimation of effect size, and power analysis. It also contains an alternative analysis using weighted least squares instead of ordinary least squares.
* The cleaningfuncs.py, edafuncs.py, and anovafuncs.py modules contain functions used in the project.
* The requirements.txt file contains the packages required to set up a virtual environment to run the code.

### Results

The ANOVA revealed that there was a statistically significant interaction between the effects of gender and running a Boston qualifying time (F(1, 3940) = 16.17, p = 0.00).

Simple main effects analysis showed that running a Boston qualifying time had a statistically significant effect on split difference for both men (p = 0.00) and women (p = 0.00). The effect sizes of running a Boston qualifying time on men and women were 1.13 and 1.04 standard deviations, respectively. That is, men and women who ran BQ times ran split differences that were 1.13 and 1.04 standard deviations lower respectively than men and women who didn't run BQ times.

Simple main effects analysis showed that gender did not have a statistically significant effect on split difference for runners who ran a Boston qualifying time (p = 0.08), but did have a statistically significant effect for runners who did not run a Boston qualifying time (p = 0.00). The effect size of being male on runners who did not run a Boston qualifying time was 0.26 standard deviations.
