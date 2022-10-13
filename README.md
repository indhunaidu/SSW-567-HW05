# SSW-567-HW05

While pylinting my original triangle program, it was interesting how strictly pylint followed the snake_case naming style. For the function inputs, I simply had a, b, and c as the variables for the sides. To conform to the naming style, I change the variable names to side_a, side_b, and side_c respectfully. Pylint also brought to my attention how common I had trailing white space, with over 10 instances of the error. The most insightful thing I discovered while pylinting the triangle program is that instead of verifying the input using isInstance(side_a, int) or isInstance(side_a, float), I could optimize this by using isInstance(side_a, (int, float)). I thought this was neat, and it made my improved program much more readable.

When checking the coverage of my unit tests using Coverage.py, I was surprised to find that I had already achieved 100% coverage, according to the coverage python module. Reading through the coverage tutorial web page, I was able to generate a web page to better display the results. I put the source code of the web page in this repository as well. Although there is a TestTriangle_Improved.py file, both that and TestTriangle.py outputs a 100% coverage. I created the file to remain consistent with the results of the pylinting.

This is the pylint output of the original program Triangle.py 
<img width="983" alt="Screen Shot 2022-10-12 at 7 58 19 PM" src="https://user-images.githubusercontent.com/42434419/195469005-64c665e4-4f32-4f57-8e1f-dd4b7e6ba4fc.png">

This is the pylint output of the improved program triangle_improved.py
<img width="624" alt="Screen Shot 2022-10-12 at 8 00 22 PM" src="https://user-images.githubusercontent.com/42434419/195469169-5af413c6-1a8e-482c-974a-0ebb7f6f1a4b.png">


This is the HTML output of the coverage test 


<img width="466" alt="Screen Shot 2022-10-12 at 8 02 56 PM" src="https://user-images.githubusercontent.com/42434419/195469390-1a9e28de-4327-4c82-9f02-3f2d1c0ce96b.png">


<img width="1434" alt="Screen Shot 2022-10-12 at 7 41 07 PM" src="https://user-images.githubusercontent.com/42434419/195469650-df5a458f-b1b3-458c-b4b0-09d9350c7a18.png">

