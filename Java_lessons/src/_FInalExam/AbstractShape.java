//package _FInalExam;
//
//public class AbstractShape {
//    public static void main(String[] args){
//        Circle circle = new Circle();
//        circle.radius = 5;
//        System.out.println(circle);
//
//        Rectangle rectangle = new Rectangle();
//        rectangle.length = 5;
//        rectangle.width = 5;
//        System.out.println(rectangle);
//    }
//
//}
//
//abstract class Shape{
//    public static double PI = 3.14;
//
//    abstract double area();
//}
//
//class Circle extends Shape{
//    int radius;
//
//    @Override
//    public double area(){
//        return Shape.PI * radius * radius;
//    }
//
//    @Override
//    public String toString(){
//        return (
//                "Circle: radius = " + radius
//                + ", area = " + area()
//                );
//    }
//}
//
//class Rectangle extends Shape{
//    int length;
//    int width;
//
//    @Override
//    public double area(){
//        return length * width;
//    }
//
//    @Override
//    public String toString(){
//        return (
//                "length" + length + "..."
//                );
//    }
//}
//
//
//
//
