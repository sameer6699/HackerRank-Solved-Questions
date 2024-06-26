<h2><a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem">Project Euler #2: Even Fibonacci numbers</a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 3 from <a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with  and , the first  terms will be:
1,2,3,5,8,13,21,34,55,89,...
By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.
</p>

<h2>Input Format</h2>
<p>First line contains T which denotes the number of test cases. This is followed by T lines, 
  each containing an integer, N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T&lt;= 10<sup>5</sup></code></li>
  <li><code>10 &lt;= N&lt;= 4 * 10<sup>5</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>Print the required answer for each test case.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
10
100
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
10
44
</pre>
<p>&nbsp;</p>

<h1>Explnation</h1>
<p>
  <ol> 
    <li>For N=10, we have {2,8}, sum is 10.</li>
    <li>For N=100, we have {2,8,34}, sum is 44.</li>
  </ol>
</p>


<h1>Solution</h1>
<p>
  <ol><b></b>sum_of_even_fibonacci(limit) function:</b>
    <li>Initializes the first two Fibonacci numbers, a and b.</li>
    <li>Uses a loop to generate Fibonacci numbers up to the specified limit.</li>
    <li>Checks if the current Fibonacci number is even, and if so, adds it to sum_even.</li>
    <li>Continues generating the next Fibonacci number by updating a and b.</li>
    <li>Continues generating the next Fibonacci number by updating a and b.</li>
    <li>Continues generating the next Fibonacci number by updating a and b.</li>
    <li>Returns the sum of even Fibonacci numbers that do not exceed the limit.</li>
</ol>
</p>