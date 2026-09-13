package _4_Implement;

public class _USB {
    public static void main(String[] args){
        Mouse m = new Mouse();
        Keyboard k = new Keyboard();
        Computer c = new Computer(new USB[] {m, k});
        c.work();
    }
}


interface USB{
    void connect();

    void disconnect();
}

class Mouse implements USB{
    @Override
    public void connect(){
        System.out.println("鼠标接入");
    }

    @Override
    public void disconnect(){
        System.out.println("鼠标拔出");
    }

    public void click(){
        System.out.println("鼠标点击");
    }
}

class Keyboard implements USB{
    @Override
    public void connect(){
        System.out.println("键盘接入");
    }

    @Override
    public void disconnect(){
        System.out.println("键盘拔出");
    }

    public void input(){
        System.out.println("键盘输入");
    }
}

class Computer{
    private USB[] usb;

    public Computer(USB... usb){
//        this.usb[0] = usb[0];
//        this.usb[1] = usb[1];
        this.usb = usb;
    }

    public void work(){
        for(USB u: usb){
            if(u instanceof Mouse){
                Mouse m = (Mouse) u;
                m.connect();
                m.click();
                m.disconnect();
            } else if(u instanceof Keyboard){
                Keyboard k = (Keyboard) u;
                k.connect();
                k.input();
                k.disconnect();
            }
        }
    }
}