package _FInalExam;

public class _2020_Data {
    public static void main(String[] args){
        Data data1 = new Data(2026, 6, 29);
        Data data2 = new Data(2026, 6, 30);
        Data data3 = new Data(2026, 6, 30);

        System.out.println(data1.equals(data2));
        System.out.println(data1.equals(data3));
        System.out.println(data2.equals(data3));
    }

}


class Data{
    int year;
    int month;
    int day;

    public Data(int year, int month, int day){
        this.year = year;
        this.month = month;
        this.day = day;
    }

    @Override
    public boolean equals(Object obj){
        if (!(obj instanceof Data)){
            return false;
        }else{
            Data data = (Data) obj;
            return (
                    this.year == data.year
                    && this.month == data.month
                    && this.day == data.day
                    );
        }
    }
}