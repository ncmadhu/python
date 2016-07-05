"""
Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.

There are n chapters in Lisa's workbook, numbered from 1 to n.

The i-th chapter has ti problems, numbered from 1 to ti.

Each page can hold up to k problems. There are no empty pages or unnecessary spaces,
so only the last page of a chapter may contain fewer than k problems.

Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.

The page number indexing starts at 1.

Lisa believes a problem to be special if its index (within a chapter) is the same as the page number
where it's located. Given the details for Lisa's workbook, can you count its number of special problems?

Input Format

The first line contains two integers n and k — the number of chapters and the maximum number of problems per page respectively. 
The second line contains n integers t1,t2,...,tn where ti denotes the number of problems in the i-th chapter.

Constraints

1 <= n,k,ti <= 100

Output Format

Print the number of special problems in Lisa's workbook.

Sample Input

5 3  
4 2 6 1 10

Sample Output

4

Explanation

Lisa's workbook with n = 5 chapters and a maximum of k = 3 problems per page.

There are 4 special problems and thus we print the number 4 on a new line.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

total_chapters, prob_per_chapters = map(int, raw_input().strip().split(" "))
chapter_problems_num = map(int, raw_input().strip().split(" "))
cur_page = 0
special_problem = 0
for i in range(0,total_chapters):
    num_of_problems = chapter_problems_num[i] 
    total_pages = num_of_problems / prob_per_chapters
    if num_of_problems % prob_per_chapters:
        total_pages += 1
    page_list = range(cur_page + 1, cur_page + total_pages + 1)
    cur_page = cur_page + total_pages
    new_list = []
    problem_list = []
    j = 0
    for i in range(1, num_of_problems + 1):
        if j < prob_per_chapters:
            new_list.append(i)
            j += 1
            if j == prob_per_chapters:
                problem_list.append(new_list)
                new_list = []
                j = 0
    if new_list:
        problem_list.append(new_list)
    #print problem_list
    #print page_list
    for i in range(0,len(page_list)):
        if page_list[i] in problem_list[i]:
            special_problem += 1
            #print "increase"
print special_problem