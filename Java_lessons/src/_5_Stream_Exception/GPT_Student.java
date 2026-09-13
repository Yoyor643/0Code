package _5_Stream_Exception;

import java.util.*;
import java.io.*;

public class GPT_Student {
    public static void main(String[] args){
        // 创建文件对象
        File infile = new File("scores.txt");
        File outfile = new File("report.txt");
        File errorfile = new File("error.log");

        int validCount = 0;
        int javaPassCount = 0;
        int javaFailCount = 0;
        int maxJavaScore = -1;
        String maxJavaName = "";


        // IO流
        try(
                BufferedReader in = new BufferedReader(new FileReader(infile));
                BufferedWriter out = new BufferedWriter(new FileWriter(outfile));
                BufferedWriter error = new BufferedWriter(new FileWriter(errorfile))
        ){
            String line;
            int lineNumber = 0;

            while((line = in.readLine()) != null){
                lineNumber++;

                if (line.trim().isEmpty()) continue;

                String[] info = line.split(",");


                // 判断信息录入是否正确
                if (info.length != 4) {
                    error.write("第" + lineNumber + "行数据错误：" + line);
                    error.newLine();
                    error.write("原因：数据格式错误，应该包含姓名、语文、数学、Java四项");
                    error.newLine();
                    error.newLine();
                    continue;
                }

                String name = info[0];
                int chinese;
                int math;
                int java;
                try{
                    chinese = Integer.parseInt(info[1]);
                    math = Integer.parseInt(info[2]);
                    java = Integer.parseInt(info[3]);

                    checkScore(chinese);
                    checkScore(math);
                    checkScore(java);
                } catch(NumberFormatException e){

                } catch)ScoreOutRangeException e){

                }
                int sum = chinese + math + java;
                double avg = sum / 3.0;

                out.write(name + ", 总分为" + sum + ", 平均分为" + avg);
                out.newLine();

                validCount++;
            }
        }catch(FileNotFoundException e){


        }catch(IOException e){
            e.printStackTrace();
        }
    }
}

class ScoreOutRangeException extends Exception{
    public ScoreOutRangeException(String msg){
        super(msg);
    }
}


//class Utils{
//    // 获取成绩->得到总分、平均分, 分析异常
//    public static double[] getScore(int[] scores) throws ScoreOutRangeException, NumberFormatException{
//        double sum = 0;
//        double avg = 0;
//
//        for (int score : scores)
//            if (score > 100 || score < 0)
//                throw new ScoreOutRangeException("成绩错误，超出范围");
//            else
//                sum += score;
//
//
//        avg = sum / scores.length;
//        return new double[]{sum, avg};
//    }
//}