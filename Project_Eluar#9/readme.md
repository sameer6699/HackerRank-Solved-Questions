<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=true">Project Euler #9: SpecialPythagorean triplet</a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 9 <a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>A Pythagorean triplet is a set of three natural numbers,<code> a < b < c </code> , for which, <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>3</sup></code></p>
<p>For example: <code> 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</code> </p>
<p>Given<code>N</code>, Check if there exists any Pythagorean triplet for which <code> a + b + c = N</code> 
Find the maximum possible value of <code> abc </code> among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1.</p>

<h2>Input Format</h2>
<p>The first line contains an integer T i.e. number of test cases.
The next T lines will contain an integer N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T &lt;= 3000</code></li>
  <li><code>K &lt;= N &lt;= 3000</code></li>
</ul>

<h2> Output Format</h2>
<p>Print the value corresponding to each test case in separate lines.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
12
4
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
60
-1
</pre>
<p>&nbsp;</p>

<h1>Explnation 0</h1>
<p>
  <ol> 
    <li>For <code> N = 12</code>, we have a triplet {3,4,5} whose product is 60.</li>
    <li>For <code>N = 4, we don't have any Pythagorean triple</code></li>
  </ol>
</p>


<h1>Solution</h1>
<p>
  To optimize the solution, we can reduce the number of iterations by utilizing some properties of Pythagorean triplets. Instead of brute-forcing all possible values for a and b, we can use the fact that for any given n,if <code> a + b + c = n</code>
  and <code> a <sup>2</sup>+ b<sup>2</sup>= c <sup>2</sup>, we can calculate b and c directly once a is chosen.</code>
</p>

<p><b>Explanation:</b>
 <ol>
   <li><b>Reduced Iteration:</b>
     <ul>
       <li> Instead of iterating all positive values of a and b, we iterate only a from 1 to n//3. this reduces the number of iterations significantly.</li>
       <li> For each a, we compute b directly using the formula <code>b=(n*(n-2*a))//(2*(n-a))</code>. This is derived from the conditions <code> a + b + c = n</code> and <code>a<sup>2</sup>+b<sup>2</sup>=c<sup>2</sup></code></li>
       <li>Then we compute <code> c as c = n - a -b.</code></li>
     </ul>
     <li><b>Efficiency:</b>
       This approach eliminates the inner loop for b, leading to a single loop for a which runs in <code> O(n)</code> time
     </li>
   </li>
 </ol>
