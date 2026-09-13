//package _FInalExam;
//
//import java.io.*;
//
//public class ThreadDemo {
//    public static void main(String[] args) {
//        Runa r = new Runa();
//
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        {
//            try {
//                r.n = Integer.valueOf(br.readLine());
//            } catch (IOException e) {
//                throw new RuntimeException(e);
//            }
//        }
//
//        Thread t = new Thread(r);
//        t.start();
//    }
//}
//
//class Runa implements Runnable{
//    int n = 0;
//    @Override
//    public void run(){
//        long res = 1;
//        for(int i = 0; i < n; ++i){
//            res *= i;
//        }
//        System.out.println(res);
//    }
//}