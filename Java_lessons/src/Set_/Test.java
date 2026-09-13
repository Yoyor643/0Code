package Set_;

import java.util.*;

public class Test {
    public static void main(String[] args){
        new Test().testIterator();
    }

    // TreeMap
    public void testTreeMap() {
        TreeMap<String, String> map = new TreeMap<String, String>();
        map.put("1", "Monday");
        map.put("2", "Tuesday");
        map.put("3", "Wednesday");
        map.put("one", "Monday");

        Set<String> keys = map.keySet();
        Iterator<String> it = keys.iterator();
        while(it.hasNext()){
            String key = it.next();
            System.out.println(key + ": " + map.get(key));
        }

        System.out.println("================");
//        Enumeration<String> e = map.keys(); // TreeMap没有keys方法，HashTable有
//        while(e.hasMoreElements()) {
//            String key = e.nextElement();
//            String value = map.get(key);
//            System.out.println(key + ": " + value);
//        }
    }

    // HashTable
    public void testHashTable() {
         Hashtable<String, String> aPhoneBook = new Hashtable<String, String>();
         aPhoneBook.put("Jim", "123-4567");
         aPhoneBook.put("Mike", "123-4568");
         aPhoneBook.put("Joe", "123-4569");

         System.out.println(aPhoneBook.get("Jim"));
         System.out.println(aPhoneBook.remove("Mike"));
         System.out.println(aPhoneBook.get("Yoyor"));
         System.out.println(aPhoneBook.contains("Yoyor"));

         System.out.println("================");
         Enumeration<String> e = aPhoneBook.elements();
         while (e.hasMoreElements()){
             System.out.println(e.nextElement());
         }

         System.out.println("================");
         Enumeration<String> e1 = aPhoneBook.keys();
         while (e1.hasMoreElements()){
             System.out.println(e1.nextElement());
         }
         aPhoneBook.clear();
         System.out.println(aPhoneBook);
    }

    // Iterator
    public void testIterator() {
        String[] num = {"1", "2", "3", "4", "5"};
//        ArrayList<String> nums = new ()<String>(Arrays.asList(num)); // 这里使用了ArrayList的接收集合的构造方法，因为不能直接把asListde返回的List集合赋给ArrayList
        List<String> nums = Arrays.asList(num);
        ArrayList<String> nums1 = new ArrayList<String>(nums);
        nums1.removeIf(s -> s.equals("4"));

        System.out.println(nums1);
        for (String s : nums1) {
            System.out.println(s);
        }
        nums1.forEach(s -> System.out.println(s));
        // Lambda 语法： (参数，参数。。。) -> {方法体}
        //              仅一个参数 可省括号； 仅一行方法体 可省括号

    }

}
