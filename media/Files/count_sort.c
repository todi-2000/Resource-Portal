#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void countsort(int arr[],int b[],int n) {
  int cum[10];
  for (int i = 0; i < 10; ++i) {
    cum[i] = 0;
  }
  for (int i = 0; i < n; i++) {
    cum[arr[i]]++;
  }
  for (int i = 8; i >= 0; --i) {
    cum[i] += cum[i + 1];
  }
    printf("Cumulative Array is: ");
    for (int i = 0; i<10; ++i)
        printf("%d ", cum[i]);
    printf("\n");
  for (int i = 0; i < n; i++) {
    b[cum[arr[i]] - 1] = arr[i];
    cum[arr[i]]--;
  }
}

void main()
{
    FILE *fp ;
    fp = fopen("input5000(0-9).text","r");
    int n;
    fscanf(fp,"%d",&n);
    int arr[n],b[n];
    for(int i=0;i<n;i++)
        fscanf(fp,"%d",&arr[i]);
    clock_t t1=clock();
    countsort(arr,b,n);
    clock_t t2 = clock();
    for(int i=0;i<n;i++)
        printf("%d ", b[i]);
    double time_taken = ((double)(t2-t1))/CLOCKS_PER_SEC;
    printf("\n took %f seconds to execute ", time_taken);

}
