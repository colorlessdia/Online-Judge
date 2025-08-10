# [Gold V] Extrusion - 4751 

[문제 링크](https://www.acmicpc.net/problem/4751) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

기하학, 다각형의 넓이

### 제출 일자

2025년 8월 11일 01:02:17

### 문제 설명

<p>The Acme Extrusion Company specializes in the production of steel bars with custom-designed cross-sections. The manufacturing process involves cutting a hole in a thick metal plate, the shape of the hole being determined by the customer’s specifications.</p>

<p>Molten metal is then forced through the hole to form a long bar. The shape of the hole determines the shape of the cross-section of the resulting bar.</p>

<p>Given a description of a polygonal hole and the volume of molten metal available, determine how long a bar can be formed by this process.</p>

### 입력 

 <p>Input consists of one or more data sets consisting of the following information:</p>

<ul>
	<li>An integer, N, indicating the number of vertices making up the polygon. End of input is signaled by any N less than 3.</li>
	<li>Next are N lines, each containing a pair of floating-point numbers, (x<sub>i</sub>,y<sub>i</sub>), each denoting one vertex of the polygon. Vertices will be presented in clockwise order (relative to the closest interior point) proceeding around the perimeter of the polygon. The x<sub>i</sub> and y<sub>i</sub> values are in units of meters.</li>
	<li>The data set is terminated by a floating point value indicating the amount of molten metal available (in cubic meters).</li>
</ul>

### 출력 

 <p>For each data set, the program should produce a single line of output of the form:</p>

<p>BAR LENGTH: x</p>

<p>where “x” is the maximum bar length, a floating point number expressed with two digits precision. </p>

<p>expressed as a polygon (vertices visited in clockwise order, each vertex described via (x,y) coordinates expressed in units of meters) and the volume of the available molten metal (in cubic<br>
meters),</p>

