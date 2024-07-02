<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem">Project Euler #8: Largest product in a series</a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 8<a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>Find the greatest product of K consecutive digits in the N digit number.</p>

<h2>Input Format</h2>
<p>First line contains T that denotes the number of test cases.
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T &lt;= 100</code></li>
	<li><code>1 &lt;= K &lt;= 7</code></li>
  <li><code>K &lt;= N &lt;= 1000</code></li>
</ul>

<h2> Output Format</h2>
<p>Print the required answer for each test case.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
10 5 
3675356291
10 5 
2709360626
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
3150
0
</pre>
<p>&nbsp;</p>

<h1>Explnation 0</h1>
<p>
  <ol> 
    <li>For <code>367535291</code>and selecting<code>k=5</code> consequetive digits, we have<code>36753,67532,75356,53562,35629 and 56291</code>Where <code>6*7*5*3*5</code> gives maximum product as <code>3150</code></li>
    <li>for <code>2709360626.0</code>lies in all selection of 5 cinsiquetive digits hence maximum product remains 0</li>
  </ol>
</p>


<h1>Solution</h1>

<p><b>Explanation:</b>
  <ol>
    <li><b>Input Handling:</b> The input for the number of test cases <code>t</code> and subsequent values n and k is read using <code>input().strip()</code>.
The n digit integer is read as a string num.</li>
    <li><b>Greatest Product Calculation:</b> The greatest_product function computes the greatest product of k consecutive digits in the n digit number.
It iterates through each possible set of k consecutive digits, calculates their product, and keeps track of the maximum product found.</li>
	  <li><b>output:</b> For each test case, the greatest product is computed and printed.</li>
</ol>
</p>
</p>
<p>This code works directly with the provided driver code structure and efficiently computes the greatest product of k consecutive digits for each test case.</p>
