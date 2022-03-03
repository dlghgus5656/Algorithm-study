// BufferedReader 을 쓰는 방식
// readLine() 을 통해 입력 받아 연산하는 방법 두 가지를 설명할 것이다.
// 앞서 말했듯이 readLine() 은 한 행을 전부 읽기 때문에 공백단위로 입력해 준 문자열을 공백단위로 분리해주어야 문제를 풀 수 있을 것이다.
// 문자열 분리 방법 두 가지로 풀어보자.
// StringTokenizer 클래스를 이용하여 분리해주는 방법
// split() 을 이용하는 방법
 

// 그리고 반드시 자료형 타입을 잘 보아야 한다.

// st.nextToken() 은 문자열을 반환하니 Integer.parseInt()로 int 형으로 변환시켜준다.

// (double 형으로 풀면 나머지가 정수로 나와도 소수점까지 같이 출력되어 오답으로 처리된다.)

// 문제
// (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

// (A*B)%C는 ((A%C) * (B%C))%C 와 같을까?

// 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
public class 백준10430번 {
 
	public static void main(String[] args) throws IOException {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
 		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str," ");
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
        
		System.out.println( (A+B)%C );
		System.out.println( (A%C + B%C)%C );
		System.out.println( (A*B)%C );
		System.out.println( (A%C * B%C)%C );
	
/*    
굳이 String 변수 생성 안하고 입력과 동시에 구분자로 분리해줘도 된다.
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
        
		System.out.println( (A+B)%C );
		System.out.println( (A%C + B%C)%C );
		System.out.println( (A*B)%C );
		System.out.println( (A%C * B%C)%C );
*/
	}
}


// 두 번째 방법은 br.readLine() 을 통해 읽어온 것을 split(" ") 
// 하여 공백 단위로 나눠준 뒤 String 배열에 각각 저장하는 방법이다.
// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.io.IOException;
 
// public class Main {
 
// 	public static void main(String[] args) throws IOException {
		     
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
// 		String[] str = br.readLine().split(" ");
// 		int A = Integer.parseInt(str[0]);
// 		int B = Integer.parseInt(str[1]);
// 		int C = Integer.parseInt(str[2]);
        
// 		System.out.println( (A+B)%C );
// 		System.out.println( (A%C + B%C)%C );
// 		System.out.println( (A*B)%C );
// 		System.out.println( (A%C * B%C)%C );
 
// 	}
 
// }