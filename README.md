# Codecademy Project: Python Gradebook

## Overview
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

## Tasks
### Create Some Lists

1. Create a list called subjects and fill it with the classes you are taking:

* <code>"physics"</code>
* <code>"calculus"</code>
* <code>"poetry"</code>
* <code>"history"</code>

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_1.png)

2. Create a list called grades and fill it with your scores:

* <code>98</code>
* <code>97</code>
* <code>85</code>
* <code>88</code>

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_2.png)

3. Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.

| Name |	Test Score |
|------|-------------|
| <code>"physics"</code>	| <code>98</code> |
| <code>"calculus"</code> |	<code>97</code> |
| <code>"poetry"</code>	| <code>85</code> |
| <code>"history"</code>	| <code>88</code> |

Assign the value into a variable called <code>gradebook</code>.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_3.png)

4. Print <code>gradebook</code>. Does it look how you expected it would?

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_4.png)

See the output from the code as follows:

![""](https://github.com/sarahm44/python-gradebook/blob/main/Output_4.png)

### Add More Subjects

5. Your grade for your computer science class just came in! You got a perfect score, <code>100</code>!

Use the <code>.append()</code> method to add a list with the values of <code>"computer science"</code> and an associated grade value of 100 to our two-dimensional list of <code>gradebook</code>.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_5.png)

6. Your grade for <code>"visual arts"</code> just came in! You got a <code>93</code>!

Use append to add <code>["visual arts", 93]</code> to gradebook.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_6.png)

### Modify The Gradebook:

7. Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.

Access the index of the grade for your visual arts class and modify it to be 5 points greater.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_7.png)

8. You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.

Find the grade value in your <code>gradebook</code> for your poetry class and use the <code>.remove()</code> method to delete it.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_8.png)

9. Use the <code>.append()</code> method to then add a new <code>"Pass"</code> value to the sublist where your poetry class is located.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_9.png)

### One Big Gradebook!

10. You also have your grades from last semester, stored in <code>last_semester_gradebook</code>.

Create a new variable <code>full_gradebook</code> that combines both <code>last_semester_gradebook</code> and <code>gradebook</code> using <code>+</code> to have one complete grade book.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Task_10.png)

Print <code>full_gradebook</code> to see our completed list.

![""](https://github.com/sarahm44/python-gradebook/blob/main/Output_10.png)
