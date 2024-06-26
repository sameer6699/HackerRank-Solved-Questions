<h2><a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem">#1 Project Euler #1: Multiples of 3 and 5</a>
</h2><h3>Medium</h3><hr>
<p>This problem is a programming version of Problem 1 from projecteuler.net</p>

<p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below N.</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T&lt;= 10<sup>5</sup></code></li>
	<li><code>1&nbsp;&lt;= N&nbsp;&lt;=10<sup>9</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
10
100
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
23
2318
</pre>
<p>&nbsp;</p>

<h1>Explnation</h1>
<p>For N=10, if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

Similarly for N=100, we get 2318.</p>


<h1>Solution</h1>
<p>To optimize the solution and avoid the "Time limit exceeded" issue, we can use a mathematical approach instead of iterating through all numbers below n. The mathematical approach calculates the sum of multiples using the formula for the sum of an arithmetic series.</p>

<ul>
	<li><b>Class Definition:</b> <p>The <code> Solution</code> class contains the <code> searchRange</code> method, which takes nums and targets as input parameters.</p></li>
	<li><b>Helper Function:</b> <p>find_left: This function finds the leftmost <code>(first)</code> index of the target. It uses binary search to locate the first occurrence of the target by moving right when <code>nums[mid]</code> is greater than or equal to the target.
	find_right: This function finds the rightmost <code>(last)</code> index of the target. It uses binary search to locate the last occurrence of the target by moving left when <code>nums[mid]</code> is less than or equal to the target.</p></li>
	<li><b>Method Implementation:</b> <p>Calculate the <code>left</code> and <code>right</code> indices of the target using the helper functions.
	Check if the indices are valid and if the values at these indices match the target.
	Return the indices if valid; otherwise,<code> return [-1, -1].</code></p></li>
	<li>This approach ensures the algorithm runs in O(log n) time complexity, leveraging binary search to efficiently find the first and last positions of the target in the sorted array.</li>
</ul>
