<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem">Project Euler #3: Largest prime factor</a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 3 from <a href="https://projecteuler.net/">projecteuler.net</a></p>

<p>The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of a given number N?</p>

<h2>Input Format</h2>
<p>First line contains T which denotes the number of test cases. This is followed by T lines, 
  each containing an integer, N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T&lt;= 10<sup>5</sup></code></li>
	<li><code>10 &lt;= N&lt;= 4 * 10<sup>12</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>For each test case, display the largest prime factor of N.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
10
17
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
5
17
</pre>
<p>&nbsp;</p>

<h1>Explnation</h1>
<p>
  <ol> 
    <li>Prime factors of 10 are {2,5}, largest is 5.</li>
    <li>Prime factor of 17 is 17 itself, hence largest is 17.</li>
  </ol>
</p>


<h1>Solution</h1>
<p><b></b>largest_prime_factor(n) function:</b>
  <ol>
    <li>Defines an inner function max_prime_factor(n) to find the largest prime factor of n</li>
    <li>Initializes <code>max_prime</code> to <code>-1</code></li>
    <li>Checks if the current Fibonacci number is even, and if so, adds it to sum_even.</li>
    <li>Removes all even factors <code>(i.e., factors of 2)</code> from n and updates <code>max_prime</code> accordingly </li>
    <li>Uses a loop to check for factors from 3 to the square root of n, incrementing by 2 to skip even numbers.</li>
    <li>If n is still greater than 2 after the loop, it means n itself is a prime number and the largest prime factor.</li>
    <li>Returns the largest prime factor found.</li>
</ol>
</p>
