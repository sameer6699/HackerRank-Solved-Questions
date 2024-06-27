<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem">Project Euler #3: Largest prime factor</a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 4 from <a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>A palindromic number reads the same both ways. The smallest 6-digit palindrome made from the product of two 3-digit numbers is <code>101101 = 143 * 707<.</code></p>
<p>Find the largest palindrome made from the product of two 3-digit numbers which is less than N.</p>

<h2>Input Format</h2>
<p>First line contains T which denotes the number of test cases. This is followed by T lines, 
  each containing an integer, N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T&lt;= 100</sup></code></li>
	<li><code>101101 &lt;= N&lt;= N < 1000000</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>Print the required answer for each test case in a new line.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
101110
800000
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
101101
793397
</pre>
<p>&nbsp;</p>

<h1>Explnation</h1>
<p>
  <ol> 
    <li>101101 is the product of 143 and 707.</li>
    <li>793397 is the product of 869 and 913.</li>
  </ol>
</p>


<h1>Solution</h1>
<p>o solve this problem, we need to find the largest palindromic number that is a product of two 3-digit numbers and is less than a given number 𝑁
N. For each test case, we'll check all possible products of two 3-digit numbers to determine the largest palindrome less than 𝑁.</p>
<p><b>Explanation:</b>
  <ol>
    <li><b>is_palindrome Function:</b> This function checks if a number is a palindrome by converting it to a string and comparing it to its reverse.</li>
    <li><b>largest_palindrome_less_than Function:</b> This function iterates through all products of two 3-digit numbers in descending order and keeps track of the largest palindrome found that is less than 𝑁.</li>
    <li><b>Main Function:</b> This function reads the input, processes each test case, and prints the results.</li>
</ol>
</p>
