// # 백준 1008번 문제 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

// 가장 기초적인 입력방법이다. 그리고 문제에 나와있듯이 오차 범위를 벗어나지 않게 하기 위해서는 반드시 double형으로 출력을 해주어야 한다.
// import java.util.Scanner;
 
// public class A나누기B {
 
// 	public static void main(String[] args) {
 
// 		Scanner in=new Scanner(System.in);
		
// 		double a=in.nextDouble();
// 		double b=in.nextDouble();
		
// 		in.close();
// 		System.out.print(a/b);
 
// 	}
// }


// BufferedReader 을 쓰는 방식이다.
// readLine() 을 통해 입력 받아 연산하는 방법 두 가지를 설명할 것이다.

// 앞서 말했듯이 readLine() 은 한 행을 전부 읽기 때문에 공백단위로 입력해 준 문자열을 공백단위로 분리해주어야 문제를 풀 수 있을 것이다.

// 문자열 분리 방법 두 가지로 풀어보자.

// StringTokenizer 클래스를 이용하여 분리해주는 방법
// split() 을 이용하는 방법

// 그리고 반드시 자료형 타입을 잘 보아야 한다.

// st.nextToken() 은 문자열을 반환하니 Double.parseDouble()로 double 형으로 변환시켜준다.

// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.io.IOException;
// import java.util.StringTokenizer;
 
// public class A나누기B {
 
// 	public static void main(String[] args) throws IOException {
        
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
//  		String str = br.readLine();
// 		StringTokenizer st = new StringTokenizer(str," ");
// 		double a = Double.parseDouble(st.nextToken());
// 		double b = Double.parseDouble(st.nextToken());
		
// 		System.out.println(a/b);
	
/*    
굳이 String 변수 생성 안하고 입력과 동시에 구분자로 분리해줘도 된다.
 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		double a = Double.parseDouble(st.nextToken());
		double b = Double.parseDouble(st.nextToken());
		
		System.out.println(a/b); 
        
*/
// 	}
// }

// 세 번째 방법은 br.readLine() 을 통해 읽어온 것을 split(" ") 하여 공백 단위로 나눠준 뒤 String 배열에 각각 저장하는 방법이다.
// 그렇게 저장된 배열 원소를 하나씩 꺼내 double형으로 변환해주어야 한다.
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class A나누기B {
 
	public static void main(String[] args) throws IOException {
		     
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		double a = Double.parseDouble(str[0]);
		double b = Double.parseDouble(str[1]);
		
		System.out.println(a/b);
 
	}
 
}