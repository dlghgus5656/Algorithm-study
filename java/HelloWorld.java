// public class Main {
// 	public static void main(String[] args) {
// 		System.out.print("Hello World!");
        
//         // System.out.println("Hello World!");     - 2번
//         // System.out.printf("Hello World!");      - 3번
//         // System.out.printf("%s","Hello World!"); - 4번
 
// 	}
// }

// import java.io.BufferedWriter;
// import java.io.OutputStreamWriter;
// import java.io.IOException;
 
// public class Main {
// 	public static void main(String[] args) throws IOException {
// 		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 
// 		bw.write("Hello World!");
// 		bw.flush();
// 		bw.close();
// 	}
// }

// public class Main {
// 	public static void main(String[] args){
 
// 		StringBuilder sb = new StringBuilder();
// 		sb.append("Hello World!");
		
// 		System.out.println(sb);
// 	}
// }

public class HelloWorld {
	public static void main(String[] args){
 
		StringBuffer sb = new StringBuffer();
		sb.append("Hello World!");
		
		System.out.println(sb);
	}
}