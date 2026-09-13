package _4_Implement;

import java.sql.SQLOutput;

public class Test {
    public static void main(String[] args){
//        byte a = 1;
//        byte b = 2;
//
//        byte c = (byte) (2147483647 + 2);
//        System.out.println(c);

        Animal a = new Dog();
        a.run();
        Dog dog = (Dog) a;
        dog.dogrun();
//        a.dogrun();

        System.out.println(a.name);
        System.out.println("=====");
        Test.test(a);
        Animal b = new Cat();
        b.run();
        System.out.println(b.name);

        if(b instanceof Dog){
            Dog cat = (Dog) b;
            cat.run();
        }else{
            System.out.println("不能转换");
        }
//        Dog cat = (Dog) b;
//        cat.run();
    }

    public static void test(Animal a){
        System.out.println(a.name);
    }
}


class Animal {
    public String name = "动物属性";
    void run(){
        System.out.println("Animal");
    }
}


class Dog extends Animal{
    public String name = "狗属性";
    @Override
    public void run(){
        System.out.println("Dogs");
    }

    public void dogrun(){
        System.out.println("Dog自己的run");
    }
}

class Cat extends Animal{
    public String name = "猫属性";
    @Override
    public void run(){
        System.out.println("Cats");
    }
}


