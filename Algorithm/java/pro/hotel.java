import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class hotel {

    public int solution(String[][] book_time) {

        List<SimpleEntry<Long, Integer>> list = new ArrayList<>();

        for (String[] time : book_time) {
            long s_h = Integer.parseInt(time[0].split(":")[0]);
            long s_m = Integer.parseInt(time[0].split(":")[1]);
            long s_time = s_h * 60 + s_m;

            long e_h = Integer.parseInt(time[1].split(":")[0]);
            long e_m = Integer.parseInt(time[1].split(":")[1]);
            long e_time = e_h * 60 + e_m;

            SimpleEntry<Long, Integer> data1 = new SimpleEntry<>(s_time, 1);
            SimpleEntry<Long, Integer> data2 = new SimpleEntry<>(e_time + 10, -1);

            list.add(data1);
            list.add(data2);

        }

        list.sort(Comparator.comparing(SimpleEntry<Long, Integer>::getKey)
                .thenComparing(SimpleEntry<Long, Integer>::getValue));
        int max_rooms = 0;
        int current_rooms = 0;
        for (SimpleEntry<Long, Integer> entry : list) {
            current_rooms += entry.getValue();
            max_rooms = Math.max(current_rooms, max_rooms);
        }

        return max_rooms;
    }
}
