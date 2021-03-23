// import java.util.Arrays;
// import java.util.Comparator;

public class ArrayReverse{
  public static void main(String[] args){
int[] arr = {1, 2, 3, 4, 5};
    reverseArray(arr);
    for (int i = 0; i< arr.length; i++){
    System.out.println(arr[i]);
    }
  }
public static int[] reverseArray(int[]arr){
for (int i = 0; i < arr.length/2; i++) {
  int temp = arr[i];
  arr[i] = arr[arr.length -i -1];
  arr[arr.length -i -1] = temp;
System.out.println(arr[i]);
}
return arr;
// public static reverseArray(int[] args){
// Arrays.sort(arr, Comparator.comparing(int::length).reversed());

// }
}
}