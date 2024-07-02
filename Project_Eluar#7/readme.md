<h2>
<a href="https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem">Project Euler #7: 10001st prime</a></h2>
<h3>Easy</h3>
<p>This problem is a programming version of Problem 7<a href="https://projecteuler.net/">projecteuler.net</a></p>
<p>By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6<sup>th</sup> prime is 13.
What is the N<sup>th</sup> prime number?</p>

<h2>Input Format</h2>
<p>First line contains T which denotes the number of test cases. This is followed by T lines, each containing an integer, N.</p>


<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= T &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= N &lt;= 10<sup>4</sup></code></li>
</ul>

<h2> Output Format</h2>
<p>Print the required answer for each test case.</p>
<p>&nbsp;</p>
<p><strong class="example">Sample Input 0:</strong></p>
<pre>
2
3
6
</pre>
<p><strong class="example">Sample Output 0:</strong></p>
<pre>
5
13
</pre>
<p>&nbsp;</p>

<h1>Explnation 0</h1>
<p>
  <ol> 
    <li>The first  prime numbers are</li>
    <li><code>{2,3,5,7,11,13,17,19,23,29}</code></li>
    <li>we can see that 3<sup>rd</sup>prime number is 5 and 6<sup>th</sup> prime number is 13.</li>
  </ol>
</p>


<h1>Solution</h1>
<p>To solve this problem, we need to write a Python program that finds the 
𝑛
nth prime number for given values of 
𝑛
n. Here's how we can approach the solution:</p>
<p><b>Explanation:</b>
  <ol><h3><b>Function sum_square_difference(n):</b></h3>
    <li><b>Input Handling:</b> Read the number of test cases and the subsequent values of 𝑛.</li>
    <li><b>PrimeGeneration:</b> Use a prime number generation method, such as the Sieve of Eratosthenes, to find the primes efficiently.</li>
	  <li><b>output:</b> For each test case, output the 𝑛<sup>th</sup> prime number.</li>
</ol>
</p>
<h1>Explnation:</h1>
<p>
  <ol>
    <li><b>sieve_of_eratosthenes(limit):</b>This function generates all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.
It initializes a boolean list where each index represents whether the number is prime. It iteratively marks non-prime numbers (multiples of each prime) as False. Finally, it compiles a list of prime numbers.</li>
<li><b>n<sup>th</sup>_prime(n):</b> This function returns the 
𝑛
nth prime number.
It calls the sieve_of_eratosthenes function with a sufficiently large limit to ensure the <code>n<sup>th</sup></code> prime is within the generated list.
It returns the prime at the position <code>n−1</code> (since list indices start at 0).</li>  
<li><b>main():</b>This function reads input from the standard input.
It extracts the number of test cases and the values for each test case. It computes the <code>n<sup>th</sup></code>prime for each test case and prints the result. </li>
<li><b>Adjustments:</b> The limit in the <code>nth_prime</code> function <code>(set to 125,000)</code> is chosen to cover the range of required primes comfortably. 
  This may need adjustment for significantly larger inputs.</li>
</ol>
  
</p>
<p>By running this program, it reads input from standard input, computes the required prime numbers, and prints them accordingly. 
  This method ensures that the solution is efficient and capable of handling multiple test cases as the problem statement requires.</p>
