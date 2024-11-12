import java.util.Scanner;

class selection_sort {
    public static void main(String args[]) {

        Scanner sacn = new Scanner(System.in);

        void selectionSort(int arr[]) {

            int min_index = 0;
            int temp;
            int n = arr.length;
            for (int i = 0; i < n - 1; i++) {
                min_index = i;
                for (int j = i; j < n; j++) {
                    if (arr[j] < arr[min_index]) {
                        min_index = j;
                    }
                }
                temp = arr[i];
                arr[i] = arr[min_index];
                arr[min_index] = temp;
            }

            return 0;
        }

        System.out.println("Enter length of string :");
        int n = sacn.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sacn.nextInt();
        }

        selectionSort(arr);

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}