# DAT 202 <br> Best Selling Books Data Analysis #

## About ##

Best-Selling Books (2023-2025) By Malak Lahyani

https://www.kaggle.com/datasets/malaklahyani/best-selling-books-20232025

Contains information on the best-selling books gathered by year.

11 Columns: ID, Book Name, Author, Rating, Review Count, Form, Price, Reading Age, Print Length, Publishing Date, Genre

*It can be used to study trends in book popularity, author recurrence, category dominance, and rank stability across years.* - Malak Lahyani

## Initial Dataset ##
- **Count**: 210
- **Book Name**: 0 Null, 196 Unique
- **Author**: 0 Null, 153 Unique
- **Rating**: 0 Null, 10 Unique
- **Review Count**: 0 Null, 196 Unique
- **Form**: 0 Null, 7 Unique
- **Price**: 0 Null, 168 Unique
- **Reading Age**: 139 Null, 19 Unique
- **Print Length**: 2 Null, 83 Unique
- **Publishing Date**: 0 Null, 176 Unique
- **Genre**: 0 Null, 22 Unique
- **ID_2023**: 110 Null, 100 Unique
- **ID_2024**: 99 Null, 101 Unique
- **ID_2025**: 111 Null, 98 Unique

## Data Quality ##

### Accurate ###

Accuracy was verified through the publicly available Amazon Best Sellers lists hosted on the US Amazon site (2023 List, 2024 List, 2025 List).

### Complete ### 

The *Reading Age* column contains a notable number of null values. Additionally, the columns *Print Length*, *ID_2023*, *ID_2024*, and *ID_2025* contain null values.

**Reading Age**: As it contains over 50% Null values, the column was dropped and unused for further analysis.

**Print Length**: Entries with the Form *Cards* don’t have print length, so the number of cards is entered instead. The entry for *Harry Potter Paperback Box Set* is also missing print length, so the value was pulled from the US Amazon site.

**ID_2023**, **ID_2024**, and **ID_2025**: Used in the total dataset to represent the ID of each entry in their respective yearly datasets. These columns were replaced by the *List Year* column, with entries that appear in multiple lists being added with duplicates.

### Current ### 
Currency of the data in terms of list ranking is confirmed as the dataset represents yearly snapshots from 2023-2025 (rankings don’t update over time). Review Count and Price lack currency as they have updated since the list entries were created.

## Data Preparation ##

### Entry Modifications ###

The entry for *The Complete Summer I Turned Pretty Trilogy (Boxed Set): The Summer I Turned Pretty, It's Not Summer Without You, We'll Always Have Summer* may not format correctly due to the commas in the Amazon book name.

An entry for *The Complete Cookbook for Young Chefs* did not appear on the current 2025 Amazon list. The entry in the .csv was removed.

The Publishing Date for *Fourth Wing* is incorrectly labelled as *17/09/2024*, value corrected to *May 2, 2023*.

## Prepared Dataset ##
- **Count**: 298
- **ID**: 0 Null, 100 Unique
- **Book Name**: 0 Null, 198 Unique
- **Author**: 0 Null, 153 Unique
- **Rating**: 0 Null, 9 Unique
- **Review Count**: 0 Null, 209 Unique
- **Form**: 0 Null, 6 Unique
- **Price**: 0 Null, 172 Unique
- **Print Length**: 0 Null, 86 Unique
- **Publishing Date**: 0 Null, 32 Unique
- **Genre**: 0 Null, 21 Unique
- **List Year**: 0 Null, 3 Unique

### Column Modifications ###

The *Publishing Date* column is recorded in the form of *DD/MM/YYYY* or *Month DD, YYYY*. For easier interactions with the *List Year* column, they were converted into the form *YYYY* (e.g. *28/03/2023* becomes *2023*).

The *Rating* column is recorded in the form of *X out of 5 stars* for ease, they were converted into the form *X* (e.g. *4.8 out of 5 stars* becomes *4.8*).

The *Price* column is recorded in the form of *$X*; for ease, they were converted into the form *X* (e.g. *$26.88* becomes *26.88*).

## Quantitative Information ##

| Column                              | Minimum | Mean   | Maximum |
|-------------------------------------|---------|--------|---------|
| Rating (/5 Stars)                   | 4.10    | 4.67   | 4.90    |
| Review Count (#)                    | 476     | 98,560 | 653,111 |
| Print Length (Pages)                | 12      | 348    | 4167    |
| Price ($)                           | 1.00    | 11.67  | 52.62   |
| List Year - Publishing Date (Years) | -1.0'   | 6.5    | 66.0    |

' See Comments

## Qualitative Information ##

| Column (Count)       | Highest                           | 2nd                    | 3rd                             | Lowest                                      |
|----------------------|-----------------------------------|------------------------|---------------------------------|---------------------------------------------|
| Author               | Sarah J. Mass (13)                | Freida McFadden (11)   | 3+ Entries (1)                  | 3+ Entries (1)                              |
| Genre                | Fiction & Action & Adventure (75) | Reading & Writing (57) | Arts & Music & Photography (28) | 3+ Entries (1)                              |
| Form                 | Paperback (152)                   | Hardcover (111)        | Board book (30)                 | Imitation Leather (1) <br> Spiral-bound (1) |
| Rating (/5 Stars)    | 4.8 (81)                          | 4.7 (68)               | 4.6 (56)                        | 4.1 (1)                                     |
| Print Length (Pages) | 400 (19)                          | 320 (13) <br> 336 (13) | 24 (11) <br> 224 (11)           | 3+ Entries (1)                              |

## Notes ##

- **Rating**: While on average a best selling book is rated 4.67 Stars, they are typically rated 4.8 (81 Occurrences).
- **Review Count**: On average a best selling book has 98560 reviews.
- **Print Length**: While on average a best selling book has 348 pages, they typically have 400 pages (19 Occurrences).
- **Price**: On average a best selling book cost $11.67.
- **Time On Amazon**: On average a book takes 6.5 years to be a best seller.

<br>

- **Author**: *Sarah J. Maas* has the most best selling books (13 Occurrences)
- **Genre**: *Fiction & Action & Adventure* is the best selling genre (75 Occurrences)
- **Form**: *Paperback* is the best selling form (152 Occurrences)

## Comments ##

***All Information taken from the US Amazon site.***

### Released After ###

On the 2023 List, Book #97 *The 5 Love Languages: The Secret to Love that Lasts* was released on June 1, 2024.

On the 2024 List, Book #2 *Onyx Storm (Wing and Claw Collection) (The Empyrean, 3)* was released on January 21, 2025.

### Rare Forms ###

On the 2024 List, Book #58 *KJV Holy Bible, Giant Print Full-size Faux Leather Red Letter Edition - Thumb Index & Ribbon Marker, King James Version, Pink (KJV Full Size GP Editions)* is the only best selling book whose form is *Imitation Leather*.

On the 2025 List, Book #50 “Large Print Easy Color & Frame - Calm (Stress Free Coloring Book)* is the only best selling book whose form is *Spiral-bound*.

### Overlap ###

Sarah J. Maas most recent book *Kingdom of Ash (Throne of Glass, 7)* is a Fantasy novel with 992 Pages and a paperback would cost $12.70 (List Price: $21.00, current -40% discount). Currently 4.8 Stars out of 147641 Reviews

Sarah J. Maas next upcoming book *A Court of Thorns and Roses 6* is a Fantasy novel with 352 Pages, however a paperback cannot be preorder. A hardback would cost $22.40 (List Price: $32.00, current -30% discount) and on Kindle it would cost $9.18 (Digital List Price: $22.40, current -59% discount)

### Lowest Stars ###

On the 2023 List, Book #78 *The Exchange: After The Firm (The Firm Series)* is the only best selling book with 4.1 Stars

## Further Analysis ##

### Input Reading Ages ###

By filling out the reading age section of the dataset, we can improve the data quality but ensuring completeness. For ease, the section may need to be abstracted (e.g. Child, Young Adult, Adult).

### Additional Websites ###

**More Ratings**: Additional websites could be used to gather more ratings. This may undo outliers and would represent a wider range of readers.

**Different Best Sellers**: Non-Amazon best sellers lists could also be add to the dataset, adding more data points to the analysis.

### Separate Countries ###

**Same Language**: By incorporating more English speaking countries we can observe differences in best sellers based on geographical locations.

**Different Languages**: By incorporating Non-English speaking countries, we can observe more world wide trends. This will likely cause a greater increase in the dataset’s size as opposed to same language countries, however it would be interesting if translated versions of best sellers books appeared on other lists.
