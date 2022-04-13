# marathon-pace-strategy

## About The Project

### Introduction

This project analyzes marathon pace strategy using data scraped from the 2021 Boston Marathon results. For purposes of this project, "pace strategy" can generally be broken down into three types that will be referred to throughout this project:

* "Even pacing" refers to running the second half of the race about as fast as the first half.
* "Positive splits" refers to running the second half of the race slower than the first half.
* "Negative splits" refers to running the second half of the race faster than the first half.

This project attempts to answer the following questions for runners age 18-39 who finished the marathon in less than 5 hours:

* Is there any relationship between marathon finish time and pace strategy?
* Is there any relationship between a runner's sex and their marathon pace strategy?
* Does the relationship of marathon finish time to pace strategy depend on a runner's sex, or does the relationship of sex to pace strategy depend on a runner's finish time?

### Background

Jared Ward, an American runner who placed 6th in the 2016 Olympic Marathon, is also an adjunct professor of statistics at Brigham Young University. He wrote his [masters thesis](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwid0biJ-Lz2AhXAkokEHf3sCU8QFnoECAMQAQ&url=http%3A%2F%2Fwww.runblogrun.com%2F2017%2F04%2F17%2FJared%2520Ward%2520Thesis.pdf&usg=AOvVaw1XFwxpzBfqOeB1fHjpMIz9) on marathon pace strategy. He analyzed split times for runners in the 2013 St. George Marathon. He found that elite runners tend to run more evenly paced races than non-elite runners, who tend to slow more in the second half of the race. He also found that women tend to more evenly pace races than men, but elite men and women run more similarly.

[Santos-Lozano et al.](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjq8b_nkvn2AhWHKs0KHVJ9AbYQFnoECAYQAQ&url=https%3A%2F%2Fwww.researchgate.net%2Fpublication%2F260226395_Influence_of_Sex_and_Level_on_Marathon_Pacing_Strategy_Insights_from_the_New_York_City_Race&usg=AOvVaw1MtZH57nVKzPwB5wZUSMH5) studied finishers of the New York Marathon from 2006 to 2011 to examine the impact of ability level and sex on marathon pacing. They found that all runners tend to adopt a positive splits strategy, but that faster runners tend to run more evenly paced races regardless of sex. However, they didn't find significant differences between the sexes. [Daniel March et al.](https://journals.lww.com/nsca-jscr/Fulltext/2011/02000/Age,_Sex,_and_Finish_Time_as_Determinants_of.14.aspx) studied runners in the Last Chance Marathon in Dublin, OH from 2005 to 2007. They found that older runners, women, and faster runners tend to run more evenly paced races than younger runners, men, and slower runners respectively. However, they did not find any statistically significant interactions between age, sex, and runner ability.

Finally, it is also worth noting that four of the last six marathon world records and the two fastest (official) marathons ever run were all actually run with a negative splits strategy, though still fairly close to even pacing (see [here](https://www.runnersworld.com/training/a20819476/what-world-records-teach-about-marathon-pacing/) and [here](https://runningmagazine.ca/sections/runs-races/a-side-by-side-comparison-of-kipchoge-and-bekeles-berlin-marathons/)).

### Project Organization and Methodology

To answer the project questions, I ran a 2x2 factorial ANOVA on the data for runners age 18-39, breaking them into groups based on sex and whether they ran a Boston Marathon qualifying time during the race. Because there were some minor issues with homogeneity of variance between groups, I also ran an alternative analysis using weighted least squares instead of ordinary least squares.

The project code is broken into five parts:

* The marathon_scraper folder contains the code for the scrapy project I used to scrape the Boston Marathon data from the results pages. The boston_spider.py file is the code I wrote to scrape the data, while most of the rest of the code is standard scrapy project code.
* The data folder contains the raw data that was scraped from the Boston Marathon results.
* The cleaning.ipynb file contains the code I used to clean the data that I scraped, along with commentary explaining my reasoning for each cleaning step.
* The exploratory_data_analysis.ipynb file contains my initial exploration of the data I cleaned in the cleaning.ipnyb file, along my observations along the way.
* The ANOVA.ipnyb file contains the experiment setup and the ANOVA itself, along with assumption testing, estimation of effect size, and power analysis. It also contains an alternative analysis using weighted least squares instead of ordinary least squares.

### Results

The ANOVA revealed that there was a statistically significant interaction between the effects of sex and running a Boston qualifying time (F(1, 3932) = 20.79, p = 0.00).

Simple main effects analysis showed that running a Boston qualifying time had a statistically significant effect on split difference for both men (p = 0.00) and women (p = 0.00). The effect sizes of running a Boston qualifying time on men and women were 1.13 and 1.03 standard deviations, respectively. That is, men and women who ran BQ times ran split differences that were 1.13 and 1.03 standard deviations lower respectively than men and women who didn't run BQ times.

Simple main effects analysis showed that sex did not have a statistically significant effect on split difference for runners who ran a Boston qualifying time (p = 0.08), but did have a statistically significant effect for runners who did not run a Boston qualifying time (p = 0.00). The effect size of being male on runners who did not run a Boston qualifying time was 0.29 standard deviations.

A major limitation of this project is the uniqueness of both the Boston Marathon in general and the 2021 Boston Marathon in particular. A larger amount of data, either from more runnings of the Boston Marathon or from a wider cross-section of marathons, would help to determine whether these results hold up generally across all marathons. Another major limitation of this experiment is looking only at runner age 18-39. An interesting follow up to this experiment would be to run a similar experiment on a larger selection of data and also examine the effects of age on pace strategy.
