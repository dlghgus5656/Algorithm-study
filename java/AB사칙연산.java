// 백준 알고리즘 문제 10869번 문제입니다.

// 아래는 기본적인 방법입니다.
// import java.util.Scanner;

// public class AB사칙연산 {
// 	public static void main(String[] args) {
// 		Scanner input = new Scanner(System.in);
// 		int a = input.nextInt(); 
// 		int b = input.nextInt(); 
		
// 		System.out.println(a+b);
// 		System.out.println(a-b);
// 		System.out.println(a*b);
// 		System.out.println(a/b);
// 		System.out.println(a%b);
// 	}
// }

// 아래는 BufferedWriter 을 쓰는 방법입니다.
// 이렇게 버퍼에 문자열을 담아둔 뒤 한번에 출력하는 방법이 있습니다.
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
 
public class AB사칙연산 {
 
	public static void main(String[] args) throws IOException {
		Scanner in = new Scanner(System.in);
		int A = in.nextInt();
		int B = in.nextInt();
 
		in.close();
 
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 
		bw.write((A+B) + "\n");
		bw.write((A-B) + "\n");
		bw.write((A*B) + "\n");
		bw.write((A/B) + "\n");
		bw.write((A%B) + "\n");
 
		bw.flush();
		bw.close();
	}
}