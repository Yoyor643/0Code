package _FInalExam;

public class Sell_ {
    public static void main(String[] args){

    }

}

class Ticket implements Runnable{
    int size;
    int number;
    boolean available;

    public Ticket(int size, int number, boolean available){
        this.size = size;
        this.number = number;
        this.available = available;
    }

    public synchronized void sell(){
        while(!available){
            try{
                wait();
            } catch (Exception e){}
        }

        System.out.println("" + (++number));
        available = false;
        notifyAll();
    }

    public synchronized void put(){
        while(available){
            try{
                wait();
            } catch (Exception e){}
        }

        System.out.println("" + (--number));
        available = true;
        notifyAll();
    }


    @Override
    public void run(){
        while(number > 0){
            sell();
        }
    }

}
