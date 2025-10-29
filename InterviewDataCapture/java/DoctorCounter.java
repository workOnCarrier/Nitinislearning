import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.LongAdder;
import java.util.stream.IntStream;

public class DoctorCounter {
    /**
     * A: matrix shape [nHospitals][mSlots], A[i][j] = doctorId on duty
     */
    public static long countDoctorsVisitingMoreThanOneHospital(int[][] A) {
        if (A == null || A.length == 0) return 0;

        int nHospitals = A.length;

        // Phase 1 (parallel): build distinct doctor sets per hospital
        // This removes repeats for the same hospital across different time slots.
        @SuppressWarnings("unchecked")
        Set<Integer>[] perHospitalSets = new Set[nHospitals];

        IntStream.range(0, nHospitals).parallel().forEach(i -> {
            int[] row = A[i];
            // Use a local HashSet: no sharing, so no contention.
            Set<Integer> doctorsHere = new HashSet<>(row.length * 2);
            for (int doc : row) doctorsHere.add(doc);
            perHospitalSets[i] = doctorsHere;
        });

        // Phase 2 (parallel): merge sets into a global map: doctorId -> #distinct hospitals
        ConcurrentHashMap<Integer, LongAdder> doctorHospitalCount = new ConcurrentHashMap<>();

        IntStream.range(0, nHospitals).parallel().forEach(i -> {
            for (int doc : perHospitalSets[i]) {
                doctorHospitalCount.computeIfAbsent(doc, k -> new LongAdder()).increment();
            }
        });

        // Phase 3: count doctors present in more than one hospital
        return doctorHospitalCount.values()
                                  .stream()
                                  .filter(adder -> adder.longValue() > 1)
                                  .count();
    }

    // --- small demo ---
    public static void main(String[] args) {
        // 3 hospitals, 5 slots each
        int[][] A = {
            {1, 2, 3, 1, 4},  // hospital 0: doctors {1,2,3,4}
            {3, 3, 5, 6, 7},  // hospital 1: doctors {3,5,6,7}
            {8, 2, 9, 7, 7}   // hospital 2: doctors {8,2,9,7}
        };
        // doctor 2 -> hospitals {0,2}
        // doctor 3 -> hospitals {0,1}
        // doctor 7 -> hospitals {1,2}
        // others appear in exactly one hospital
        System.out.println(countDoctorsVisitingMoreThanOneHospital(A)); // 3
    }
}
