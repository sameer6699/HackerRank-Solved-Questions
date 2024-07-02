<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem">Project Euler #6: Sum square difference</a></h2>
<h3>Medium</h3>
<p>This problem is a programming version of Problem 6 from <a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>The sum of the squares of the first ten natural numbers is, <code>1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup>= 385 </code>. The square of the sum of the first ten natural numbers is, <code>(1+2+...+10)<sup>2</sup>=55<sup>2</sup>=3025</code>. 
Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the sum is <code>3025 - 358 = 2640</code>.</p>
<p>Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.</p>

<h2>Input Format</h2>
<p>First line contains T which denotes the number of test cases. This is followed by T lines, 
each containing an integer, N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= N &lt;= 10<sup>4</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>Print the required answer for each test case.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
3
10
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
22
2640
</pre>
<p>&nbsp;</p>

<h1>Explnation 0</h1>
<p>
  <ol> 
    <li>For N=3, <code>(1+2+3)<sup>2</sup> - (1<sup>2</sup>+2<sup></sup>2+3<sup>2</sup>) => 22</code></li>
    <li>For N=10, <code>(1+2+...+10)<sup>2</sup> - (1<sup>2</sup>+2<sup>2</sup>+...+10<sup>2</sup>) => 2640</code></li>
  </ol>
</p>


<h1>Solution</h1>
<p>. This problem involves calculating the absolute difference between the sum of the squares and the square of the sum for the first n natural numbers.</p>
<p><b>Explanation:</b>
  <ol><h3><b>Function sum_square_difference(n):</b></h3>
    <li><b>sum_of_squares:</b> This is the sum of the squares of the first n natural numbers. It is calculated using a generator expression inside the sum function:<code> sum(i ** 2 for i in range(1, n + 1)).</code></li>
    <li><b>square_of_sum:</b> This is the square of the sum of the first n natural numbers. The sum is calculated using <code>sum(range(1, n + 1))</code>, and then it is squared.</li>
	  <li><b>Return:</b> The function returns the absolute difference between <code>sum_of_squares</code> and <code>square_of_sum.</code></li>
</ol>
</p>
