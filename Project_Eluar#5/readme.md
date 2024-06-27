<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem">Project Euler #5: Smallest multiple</a></h2>
<h3>Medium</h3>
<p>This problem is a programming version of Problem 5 from <a href="https://projecteuler.net/">projecteuler.net</a></p>
<p> 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly <code>divisible(divisible with no remainder)</code> by all of the numbers from 1 to N?</p>

<h2>Input Format</h2>
<p>First line contains T which denotes the number of test cases. This is followed by T lines, 
  each containing an integer, N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T &lt;= 10</sup></code></li>
	<li><code>1 &lt;= N &lt;= 40</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>Print the required answer for each test case in a new line.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
3
10
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
6
2520
</pre>
<p>&nbsp;</p>

<h1>Explnation 0</h1>
<p>
  <ol> 
    <li>You can check 6 is divisible by each of {1,2,3], giving quotient of {6,3,2} respectively.</li>
    <li>You can check 2520 is divisible by each of {1,2,3,4,5,6,7,8,9,10} giving quotient of {2520,1260,840,630,504,420,360,315,280,252} respectively.</li>
  </ol>
</p>


<h1>Solution</h1>
<p>To solve the problem of finding the smallest positive number that is evenly divisible by all numbers from <code>1</code> to a given number <code>𝑛</code>
n, we need to compute the least common multiple (LCM) of the range <code>[1, n].</code> The LCM of a set of numbers is the smallest number that is a multiple of each of the numbers in the set.</p>
<p>The formula for the LCM of two numbers a and 𝑏 b can be derived from their greatest common divisor (GCD):</p>
<p><b>Explanation:</b>
  <ol>
    <li><b>In Python, the math module provides a gcd function, which we can use to implement the LCM function.</b></li>
</ol>
</p>
