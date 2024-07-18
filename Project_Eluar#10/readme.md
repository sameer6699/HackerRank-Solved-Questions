<h2><a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true">Project Euler #10: Summation of Primes </a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 10 <a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes not greater than given N.</p>

<h2>Input Format</h2>
<p>The first line contains an integer T i.e. number of test cases.
The next T lines will contain an integer N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T &lt;= 10<sup>4</sup></code></li>
  <li><code>K &lt;= N &lt;= 10<sup>6</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>Print the value corresponding to each test case in separate lines.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
5
10
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
10
17
</pre>
<p>&nbsp;</p>

<h1>Explnation 0</h1>
<p>
  <ol> 
    <li>For <code> N = 5</code>, we have prime as {2,3,5} and the sum is 10.</li>
    <li>For <code> N = 10, we have primes as {2,3,5,7} and sum is 17.<li>
  </ol>
</p>


<h1>Solution</h1>
<p>
  To solve this problem, we'll use the Sieve of Eratosthenes to find all prime numbers up to the maximum number in the input. 
  Then, we can precompute the sum of primes up to each number and use this precomputed information to answer each query quickly.
<p>

<p><b>Explanation:</b>
 <ol>
   <li><b>Stive of Eratosthenes:</b>
     <ul>
       <li> We initialize an array is_prime where each index represents whether the number is prime.</li>
       <li> We iterate through the array and mark the multiples of each prime number as not prime.</li>
       <li>We maintain a list of cumulative sums of primes called sum_primes.</li>
     </ul>
     <li><b>Reading Input:</b>
       <ul>
         <li> We read the input using <code>sys.stdin.read()</code> which allows us to read all the input at once.</li>
         <li> We parse the input to get the number of test cases and each query value.</li>
       </ul>
     </li>
   <li><b>Precompute Prime Sums:</b>
   <ul>
     <li> We call the sieve_of_eratosthenes function with the maximum value from the queries to get the precomputed prime sums up to that value.</li>
   </ul>
   </li>
  </li>
 </ol>
